# relatorio-wca

Skill do Claude para escrever o relatório pós-competição que um Delegado da WCA envia junto com os resultados.

A skill cobre as três partes do trabalho:

- **O relatório** em PT-BR e EN-US, na estrutura padrão (Summary, Venue, Organization, Incidents, Remarks), escrito seção por seção a partir do relato do delegado.
- **A planilha financeira** no template LatAm Budget da WCA, a partir da planilha própria do delegado.
- **As fotos do setup** com as áreas de resolução, embaralhamento e espera marcadas, com legenda.

## Instalação

Clone o repositório dentro da pasta de skills do Claude:

```bash
git clone https://github.com/thalesaraujods/relatorio-wca ~/.claude/skills/relatorio-wca
```

Ou baixe `relatorio-wca.skill` e instale pela interface do Claude.

## Uso

Com a skill instalada, basta começar a conversa falando da competição:

> Preciso escrever o relatório do Manaus Beginners 2026, o link é https://www.worldcubeassociation.org/competitions/ManausBeginners2026

A skill levanta os dados objetivos na página da WCA — data, local, modalidades, número de competidores, organizadores e delegados — e depois pede o relato de cada seção. Você pode responder por texto ou áudio; ela escreve nos dois idiomas e mostra para revisão antes de seguir para a próxima seção.

## Estrutura

```
SKILL.md                    instruções principais
references/
  estrutura.md              esqueleto das seções, padrão bilíngue e fórmulas recorrentes
  orcamento.md              template LatAm Budget e as armadilhas da planilha
  fotos.md                  marcação das áreas nas fotos do local
  exemplos/                 seis relatórios reais, usados como referência de forma e voz
scripts/
  marcar_areas.py           desenha os retângulos e a legenda sobre as fotos
  gerar_editor.py           monta o editor em que o delegado arrasta e redimensiona as áreas
  grade_referencia.py       gera a foto com grade nomeada, para apontar as áreas sem estimativa
assets/
  editor_areas.html         modelo da página do editor de áreas
```

## Scripts

Marcar as áreas, com as caixas em coordenadas normalizadas (0 a 1):

```bash
python3 scripts/marcar_areas.py config.json
```

```json
{
  "saida": "saida/",
  "fotos": {
    "foto.jpeg": [
      {"cor": "amarelo",  "caixa": [0.52, 0.355, 0.86, 0.498]},
      {"cor": "vermelho", "caixa": [0.13, 0.33, 0.43, 0.54]},
      {"cor": "laranja",  "caixa": [0.30, 0.50, 0.80, 0.998]}
    ]
  }
}
```

Gerar o editor de áreas, para o delegado ajustar os retângulos direto na foto (publicado como Artifact, junto com a pasta `fotos/` que o script cria):

```bash
python3 scripts/gerar_editor.py foto1.jpeg foto2.jpeg --saida editor/ --titulo "Áreas da competição" --config config.json
```

O botão "Copiar resultado" do editor devolve um JSON já no formato de `marcar_areas.py`, apontando para as fotos originais.

Gerar a foto com grade de referência, quando for mais prático apontar as áreas por célula:

```bash
python3 scripts/grade_referencia.py foto.jpeg --saida saida/
```

A grade tem 10 colunas (A–J) por 8 linhas (1–8). "Espera vai de D5 até H8" vira a caixa `[0.3, 0.5, 0.8, 1.0]`.

Os scripts dependem apenas de [Pillow](https://pypi.org/project/Pillow/).

## Sobre os exemplos

Os relatórios em `references/exemplos/` são de competições reais realizadas em Manaus em 2026 e servem como referência de forma e de voz. Contêm nomes e WCA IDs de organizadores e competidores, todos já públicos no site da WCA.
