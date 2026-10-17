#!/usr/bin/env python3
"""Sobrepoe uma grade nomeada a uma foto, para o delegado apontar as areas.

Uso:
    python3 grade_referencia.py foto.jpeg [outra.jpeg ...] --saida pasta/

A grade tem 10 colunas (A a J) por 8 linhas (1 a 8) e imprime o nome de cada
celula no seu canto superior esquerdo. O delegado responde algo como
"espera vai de D5 ate H8" e a marcacao sai exata, sem estimativa visual.

Conversao de celula para as coordenadas de marcar_areas.py:
    coluna A comeca em x=0.0, cada coluna vale 0.1
    linha 1 comeca em y=0.0, cada linha vale 0.125
    "D5 ate H8" -> [0.3, 0.5, 0.8, 1.0]
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

COLUNAS = "ABCDEFGHIJ"
LINHAS = 8
# Primeira fonte em negrito encontrada (Linux, macOS, Windows). Sem nenhuma,
# o Pillow cai numa fonte bitmap minuscula e a legenda fica ilegivel.
FONTES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def _fonte(tamanho):
    for caminho in FONTES:
        try:
            return ImageFont.truetype(caminho, tamanho)
        except OSError:
            continue
    return ImageFont.load_default(size=tamanho)


def agradar(origem, saida):
    im = Image.open(origem).convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im, "RGBA")

    largura_col = w / len(COLUNAS)
    altura_lin = h / LINHAS
    traco = max(3, int(h * 0.0015))
    fonte = _fonte(int(h * 0.030))

    for i in range(1, len(COLUNAS)):
        x = i * largura_col
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 210), width=traco)
    for j in range(1, LINHAS):
        y = j * altura_lin
        draw.line([(0, y), (w, y)], fill=(255, 255, 255, 210), width=traco)

    for j in range(LINHAS):
        for i, letra in enumerate(COLUNAS):
            rotulo = f"{letra}{j + 1}"
            x = i * largura_col + largura_col * 0.06
            y = j * altura_lin + altura_lin * 0.05
            bbox = draw.textbbox((x, y), rotulo, font=fonte)
            draw.rectangle([bbox[0] - 10, bbox[1] - 8, bbox[2] + 10, bbox[3] + 8],
                           fill=(0, 0, 0, 150))
            draw.text((x, y), rotulo, font=fonte, fill=(255, 255, 255))

    destino = Path(saida) / (Path(origem).stem + "-grade.jpg")
    destino.parent.mkdir(parents=True, exist_ok=True)
    im.save(destino, quality=88)
    return destino


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fotos", nargs="+")
    ap.add_argument("--saida", default=".")
    args = ap.parse_args()

    for foto in args.fotos:
        print(f"gravado: {agradar(foto, args.saida)}")


if __name__ == "__main__":
    main()
