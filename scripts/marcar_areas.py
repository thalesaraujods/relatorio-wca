#!/usr/bin/env python3
"""Desenha as areas de uma competicao da WCA sobre as fotos do local.

Uso:
    python3 marcar_areas.py config.json

O JSON tem a forma:

    {
      "saida": "/caminho/de/saida",
      "fotos": {
        "/caminho/foto.jpeg": [
          {"cor": "amarelo",  "caixa": [0.52, 0.35, 0.86, 0.50]},
          {"cor": "vermelho", "caixa": [0.13, 0.33, 0.43, 0.54]},
          {"cor": "laranja",  "caixa": [0.30, 0.50, 0.80, 1.00]}
        ]
      }
    }

"caixa" e [x0, y0, x1, y1] em coordenadas normalizadas (0 a 1), medidas da
esquerda para a direita e de cima para baixo. Usar fracoes em vez de pixels
deixa a mesma configuracao valida para qualquer resolucao da mesma foto.
"""

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CORES = {
    "amarelo": (255, 208, 0),
    "vermelho": (228, 30, 38),
    "laranja": (255, 133, 0),
}

LEGENDA = [
    ("amarelo", "Solving area"),
    ("vermelho", "Scramble area"),
    ("laranja", "Waiting area"),
]

FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def _fonte(tamanho):
    try:
        return ImageFont.truetype(FONTE, tamanho)
    except OSError:
        return ImageFont.load_default()


def desenhar_legenda(im, draw):
    """Painel escuro no canto inferior direito com as tres cores."""
    w, h = im.size
    corpo = int(h * 0.028)
    fonte = _fonte(corpo)

    margem_interna = int(h * 0.018)
    entre_linhas = int(h * 0.013)
    amostra = int(corpo * 1.15)
    respiro = int(corpo * 0.6)

    largura_texto = max(draw.textlength(t, font=fonte) for _, t in LEGENDA)
    largura = int(margem_interna * 2 + amostra + respiro + largura_texto)
    altura = int(
        margem_interna * 2 + len(LEGENDA) * amostra + (len(LEGENDA) - 1) * entre_linhas
    )

    margem = int(h * 0.022)
    x1, y1 = w - margem, h - margem
    x0, y0 = x1 - largura, y1 - altura

    painel = Image.new("RGBA", (largura, altura), (0, 0, 0, 185))
    im.paste(painel, (x0, y0), painel)
    draw.rectangle([x0, y0, x1, y1], outline=(255, 255, 255),
                   width=max(2, int(h * 0.0012)))

    y = y0 + margem_interna
    for nome, texto in LEGENDA:
        draw.rectangle([x0 + margem_interna, y,
                        x0 + margem_interna + amostra, y + amostra],
                       fill=CORES[nome])
        bbox = draw.textbbox((0, 0), texto, font=fonte)
        altura_texto = bbox[3] - bbox[1]
        draw.text((x0 + margem_interna + amostra + respiro,
                   y + (amostra - altura_texto) // 2 - bbox[1]),
                  texto, font=fonte, fill=(255, 255, 255))
        y += amostra + entre_linhas


def marcar(origem, areas, saida):
    im = Image.open(origem).convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)
    borda = max(6, int(h * 0.004))

    for area in areas:
        cor = CORES[area["cor"]]
        x0, y0, x1, y1 = area["caixa"]
        caixa = [x0 * w, y0 * h, x1 * w, y1 * h]
        # mantem o traco inteiro dentro da imagem
        caixa[0] = max(caixa[0], borda / 2)
        caixa[1] = max(caixa[1], borda / 2)
        caixa[2] = min(caixa[2], w - borda / 2)
        caixa[3] = min(caixa[3], h - borda / 2)
        draw.rectangle(caixa, outline=cor, width=borda)

    desenhar_legenda(im, draw)

    destino = Path(saida) / (Path(origem).stem + "-areas.jpg")
    destino.parent.mkdir(parents=True, exist_ok=True)
    im.save(destino, quality=92)
    return destino


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    config = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    saida = config.get("saida", ".")

    for origem, areas in config["fotos"].items():
        destino = marcar(origem, areas, saida)
        print(f"gravado: {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
