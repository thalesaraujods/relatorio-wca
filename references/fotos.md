# Marcação das áreas nas fotos

As fotos do salão entram no relatório com as três áreas destacadas e uma legenda. Convenção de cores, em inglês:

- **amarelo** — Solving area
- **vermelho** — Scramble area
- **laranja** — Waiting area

## Scripts

`scripts/marcar_areas.py` desenha os retângulos e a legenda. As caixas são definidas em coordenadas normalizadas (0 a 1), então o mesmo arquivo de configuração serve para qualquer resolução:

```bash
python3 scripts/marcar_areas.py config.json
```

O JSON tem esta forma:

```json
{
  "saida": "/caminho/para/saida",
  "fotos": {
    "/caminho/foto1.jpeg": [
      {"cor": "amarelo",  "caixa": [0.52, 0.355, 0.86, 0.498]},
      {"cor": "vermelho", "caixa": [0.13, 0.33, 0.43, 0.54]},
      {"cor": "laranja",  "caixa": [0.30, 0.50, 0.80, 0.998]}
    ]
  }
}
```

`caixa` é `[x0, y0, x1, y1]`, da esquerda para a direita e de cima para baixo.

`scripts/grade_referencia.py` gera a mesma foto com uma grade de 10 colunas (A–J) por 8 linhas, com o rótulo de cada célula impresso:

```bash
python3 scripts/grade_referencia.py foto.jpeg --saida pasta/
```

Converter células em coordenadas: coluna A começa em x=0.0 e cada coluna vale 0.1; linha 1 começa em y=0.0 e cada linha vale 0.125. "D5 até H8" vira `[0.3, 0.5, 0.8, 1.0]`.

`scripts/gerar_editor.py` monta o **editor de áreas**: uma página em que o delegado arrasta e redimensiona os retângulos sobre as fotos, liga e desliga cada área e escolhe quais fotos entram no relatório.

```bash
python3 scripts/gerar_editor.py foto1.jpeg foto2.jpeg --saida editor/ \
    --titulo "Áreas do <competição>" --config config.json --saida-marcadas fotos-marcadas/
```

Ele grava `editor/editor.html` e `editor/fotos/<n>.jpg` (cópias reduzidas a 2400 px, só para a página ficar leve). `--config` é opcional: com ele, a sua marcação atual vira o ponto de partida e só as fotos presentes no config começam como "no relatório".

Publique a página como Artifact, passando as fotos em `files` com o mesmo caminho relativo que o HTML usa:

```
file_path: editor/editor.html
files: {"fotos/1.jpg": "editor/fotos/1.jpg", "fotos/2.jpg": "editor/fotos/2.jpg", ...}
```

O botão **Copiar resultado** devolve um JSON já no formato de `marcar_areas.py`, com os caminhos das fotos **originais** e a pasta de saída. Quando o delegado colar o texto no chat, salve em um arquivo e rode `marcar_areas.py` com ele: a marcação final sai na resolução original, não na cópia reduzida do editor. O editor guarda o rascunho no navegador do delegado, então ele pode fechar e voltar depois.

## Como conduzir

**Trabalhe na resolução original.** Fotos de celular chegam com 5000 px ou mais no lado maior. A largura da borda e o tamanho da legenda nos scripts são proporcionais à altura, então não há motivo para reduzir.

**Marque só o que aparece.** Uma foto tirada de dentro da área de embaralhamento pode não mostrar nenhuma estação de resolução. Nesse caso ela fica sem o retângulo amarelo, e você diz isso ao delegado em vez de inventar uma posição.

**Retângulos não se sobrepõem.** Quando duas áreas se encostam na perspectiva, recue uma das bordas e avise qual ajuste foi feito.

**Pare de adivinhar na segunda correção.** Identificar área por estimativa visual é a parte mais cara de todo o processo. Critérios como "as cadeiras de costas para a área de resolução" são claros para quem esteve no salão e ambíguos numa foto em perspectiva, principalmente quando há vários blocos de cadeiras. Numa sessão real isso custou cinco rodadas.

Na segunda correção — ou logo de início, se o delegado pedir para editar as fotos — ofereça uma das duas saídas:

1. **Editor de áreas** (preferível). Gere com `gerar_editor.py`, usando a sua marcação atual como `--config`, e publique como Artifact. O delegado ajusta tudo direto na foto e cola o resultado de volta; você roda `marcar_areas.py` sem nenhuma conversão. Funciona no celular.
2. **Grade de referência.** Gere a foto com grade, peça o intervalo de cada área e aplique. Útil quando o delegado prefere responder por texto ou áudio. Como as células têm os mesmos nomes em todas as fotos, confirme a qual foto o intervalo se refere antes de aplicar — intervalos de uma foto aplicados a outra produzem marcações absurdas.

Fotos de competidores costumam mostrar menores de idade: o Artifact do editor nasce privado, e não há motivo para compartilhá-lo.

**Confirme antes de replicar.** Acertar a marcação em uma foto não significa que a mesma área está no mesmo lugar nas outras — são ângulos diferentes do mesmo salão. Trate cada foto separadamente.
