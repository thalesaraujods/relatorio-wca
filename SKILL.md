---
name: relatorio-wca
description: Escreve o relatório pós-competição que um Delegado da WCA envia junto com os resultados — em PT-BR e EN-US, na estrutura Summary / Venue / Organization / Incidents / Remarks. Use sempre que o usuário mencionar relatório de competição, delegate report, "relatório da WCA", o nome de uma competição da WCA junto com relatar/escrever/documentar, ou pedir ajuda com planilha financeira de competição (template LatAm Budget), marcação das áreas de resolução/embaralhamento/espera em fotos do local, ou prestação de contas de um evento de speedcubing. Use mesmo quando o usuário não disser a palavra "relatório" — descrever como foi a competição, quantos competidores vieram, o que deu errado no dia, ou mandar um áudio contando o evento já é matéria-prima de relatório.
---

# Relatório de competição da WCA

Este skill produz o relatório que o Delegado envia à WCA depois de cada competição. O leitor é outro delegado ou o WCA Delegates Committee: alguém que vai cruzar o texto com a página oficial da competição e com a planilha financeira. Ele quer saber se a competição seguiu o regulamento, o que deu errado e o que foi aprendido — não quer prosa.

Os seis relatórios reais em `references/exemplos/` são a referência de forma e de voz. Leia pelo menos dois antes de escrever, escolhendo os mais parecidos com a competição em questão (`uec26.md` para evento pequeno em auditório, `cac26-etapapontanegra.md` para evento grande com delegado trainee, `fac26-speed.md` para evento de side events).

## Como conduzir

**Um relatório por competição.** Duas competições no mesmo dia e local geram dois arquivos independentes. Cada um precisa fazer sentido para quem não leu o outro: nada de "a chuva também afetou a tarde". Quando o espaço foi compartilhado, cada Summary diz isso explicitamente — é o que explica ao avaliador por que o equipamento se repete e por que o aluguel aparece em apenas um orçamento.

**Levante os dados objetivos antes de perguntar qualquer coisa.** Peça o link da competição no site da WCA e extraia de lá: data, endereço completo, modalidades, número de competidores, limite de inscrições, organizadores e delegados com WCA ID, pódios e tempos. Devolva isso em tabela antes de pedir o relato. Economiza o tempo do delegado e evita que ele repita o que já está registrado.

**Aponte o que chama atenção nos números.** Público muito abaixo do limite, contraste entre competições irmãs, estreia de um trainee, modalidade com participação inédita. Esses são os ganchos que viram Summary e Remarks. Levantar isso é parte do trabalho, não um extra.

**Colete o relato seção por seção e revise antes de seguir.** O delegado costuma responder por áudio ou texto corrido. Escreva a seção nos dois idiomas, mostre, e só avance quando ele aprovar. Correções pegas cedo não contaminam o resto do texto — numa sessão real, "comunidade consolidada" com 7 competidores foi corrigido no Summary e teria se repetido no Remarks.

**Transcrição de voz erra nome próprio.** Florença virou "Floresta", Thales virou "Thaís", Big & Blind virou "Beacon Blind". Confira todo nome de pessoa, local e competição contra a página da WCA antes de escrever.

**Divergência entre o relato e o registro oficial vira pergunta.** Se o delegado diz 16 competidores e o site diz 15, pergunte — pode ser um não comparecimento, e isso muda a base de cálculo da taxa ABRACM/WCA. Nunca escolha um dos números sozinho.

## Estrutura e voz

A estrutura exata das seções, o padrão bilíngue e as fórmulas recorrentes estão em `references/estrutura.md`. Leia antes de escrever a primeira seção.

Três regras de corte que valem repetir aqui, porque são as que mais aparecem na revisão:

- **Nada de redundância processual.** "Todos os horários foram atualizados no site da WCA" sai: o envio do cronograma atualizado já é obrigatório na submissão. "A rodada única também servia como final" sai: se havia uma rodada só, isso é óbvio para o leitor.
- **Detalhe só onde cumpre função.** A rodada única pode aparecer se justifica um atraso proposital no início ou explica um encerramento adiantado. Fora disso, não.
- **Não afirme maturidade que os números não sustentam.** Com 7 competidores não se escreve "comunidade consolidada". Registre o avanço real e a ressalva.

## Orçamento

O Budget depende do número final, então monte a planilha antes de escrever a seção. O processo com o template LatAm Budget da WCA está em `references/orcamento.md`.

Pergunte junto com os dados financeiros, não depois: a cotação do dólar a usar, quem fica com o lucro, e se há comprovantes para a coluna Receipt.

## Fotos das áreas

Relatórios costumam incluir fotos do salão com as áreas de resolução, embaralhamento e espera marcadas. `scripts/marcar_areas.py` desenha os retângulos e a legenda; `scripts/gerar_editor.py` monta um editor em que o delegado arrasta e redimensiona as áreas; `scripts/grade_referencia.py` gera a versão com grade.

Identificar as áreas por estimativa visual é a parte mais cara do processo — numa sessão real custou cinco rodadas de correção, porque "cadeiras de costas para a área de resolução" é claro para quem esteve no salão e ambíguo numa foto em perspectiva. Faça uma primeira marcação, e na **segunda** correção (ou quando o delegado pedir para editar) pare de adivinhar: publique o editor com a sua marcação como ponto de partida. O delegado ajusta na própria foto e cola o resultado, que já é o config de `marcar_areas.py`. Se ele preferir responder por texto, use a grade ("espera vai de D5 até H8"). Detalhes em `references/fotos.md`.

## Entregas

- Um arquivo `.md` por competição, nomeado com a sigla curta do evento e o ano (`mbb26.md`, `uec26.md`), seguindo o padrão da pasta `relatorios-wca` do delegado.
- A planilha financeira, uma por competição.
- As fotos marcadas, na resolução original.

Antes de entregar, confira que "disponível no link" foi substituído pelo link real de cada planilha — é o detalhe que mais escapa.
