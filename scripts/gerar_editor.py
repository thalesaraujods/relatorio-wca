#!/usr/bin/env python3
"""Gera o editor de areas: uma pagina em que o delegado arrasta e redimensiona
os retangulos de resolucao, embaralhamento e espera sobre as fotos do local.

Uso:
    python3 gerar_editor.py foto1.jpeg foto2.jpeg ... --saida pasta/ \
        [--titulo "Areas do Plaza ao Cubo"] [--config config.json] [--saida-marcadas fotos-marcadas/]

Gera, dentro de --saida:
    editor.html      a pagina, para publicar como Artifact
    fotos/<n>.jpg    copias reduzidas das fotos, publicadas junto com a pagina

--config aceita um JSON no formato de marcar_areas.py: as caixas dele viram a
marcacao inicial do editor, e so as fotos que aparecem nele comecam marcadas
como "no relatorio". Sem --config, todas as fotos comecam incluidas e vazias.

O botao "Copiar resultado" do editor devolve um JSON pronto para
marcar_areas.py, com os caminhos das fotos originais. Basta salvar o texto
colado pelo delegado num arquivo e rodar marcar_areas.py com ele: a marcacao
final sai na resolucao original, nao na copia reduzida do editor.
"""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps

MODELO = Path(__file__).resolve().parent.parent / "assets" / "editor_areas.html"
LADO_MAXIMO = 2400  # suficiente para posicionar as caixas; mantem a pagina leve


def copia_web(origem, destino):
    im = ImageOps.exif_transpose(Image.open(origem)).convert("RGB")
    im.thumbnail((LADO_MAXIMO, LADO_MAXIMO))
    destino.parent.mkdir(parents=True, exist_ok=True)
    im.save(destino, quality=85)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fotos", nargs="+")
    ap.add_argument("--saida", required=True, help="pasta onde ficam editor.html e fotos/")
    ap.add_argument("--titulo", default="Áreas da competição")
    ap.add_argument("--config", help="JSON de marcar_areas.py com a marcacao inicial")
    ap.add_argument("--saida-marcadas", default="fotos-marcadas",
                    help="valor de 'saida' no JSON que o editor devolve")
    args = ap.parse_args()

    saida = Path(args.saida)
    iniciais = {}
    if args.config:
        cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
        iniciais = {str(Path(k).resolve()): v for k, v in cfg["fotos"].items()}

    fotos = []
    for i, caminho in enumerate(args.fotos, start=1):
        origem = str(Path(caminho).resolve())
        web = f"fotos/{i}.jpg"
        copia_web(origem, saida / web)
        areas = iniciais.get(origem)
        fotos.append({
            "id": f"Foto {i}",
            "web": web,
            "origem": origem,
            "incluir": areas is not None if iniciais else True,
            "caixas": {a["cor"]: a["caixa"] for a in (areas or [])},
        })

    chave = "editor-areas-" + hashlib.sha1(
        "|".join(f["origem"] for f in fotos).encode()).hexdigest()[:10]
    dados = {
        "titulo": args.titulo,
        "chave": chave,
        "saida": str(Path(args.saida_marcadas).resolve()),
        "fotos": fotos,
    }
    js = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    html = MODELO.read_text(encoding="utf-8")
    html = html.replace("__TITULO__", args.titulo).replace("/*__DADOS__*/null", js)

    pagina = saida / "editor.html"
    pagina.write_text(html, encoding="utf-8")
    print(f"gravado: {pagina}")
    for f in fotos:
        print(f"gravado: {saida / f['web']}  <- {f['origem']}")


if __name__ == "__main__":
    main()
