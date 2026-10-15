# Estrutura e voz do relatório

Destilado dos seis relatórios em `references/exemplos/`.

## Esqueleto

Sempre esta ordem, com estes títulos em inglês, em negrito dentro do heading:

```markdown
## **Summary**
## **Venue**
### **Equipment**
### **Venue Notes**
### **Setup**
## **Organization**
### **Organization team/Delegates**
### **Schedule**
### **Budget**
## **Incidents**
## **Remarks**
```

Alguns exemplos antigos trazem sufixos como `(\#\#\#)` nos headings — são resíduo de exportação do Google Docs. Não reproduza.

## Padrão bilíngue

Cada seção traz o texto em português e depois em inglês, marcados assim:

```markdown
**PT-BR**  
Primeiro parágrafo em português.

Segundo parágrafo.

**EN-US**  
First paragraph in English.

Second paragraph.
```

Os marcadores terminam com dois espaços (quebra de linha markdown). A versão em inglês é tradução fiel, não resumo: mesma quantidade de parágrafos, mesma informação.

Exceção: **Equipment** é uma lista técnica e aparece só uma vez, em inglês.

## Seção por seção

### Summary

Abre com a proposta da competição — por que ela existiu, que público buscava. Depois os números que importam (competidores, expectativa, estreantes) e os destaques do dia. Fecha com o que foi entregue aos competidores: certificados de participação, crachás, certificados de premiação aos medalhistas, camisa oficial se houve venda.

Quando duas competições dividem dia e local, acrescente um parágrafo dizendo isso.

### Venue > Equipment

Lista em inglês, dividida em dois blocos:

```markdown
**Main Stage**

- Gen 4 Timers: 1  
- Gen 5 Timers: 4  
- SpeedStacks Displays: 5  
- 1 laptop for displaying scrambles

**Data Entry**

- 1 laptop for data entry
```

Inclua só as gerações de timer efetivamente usadas. Se o data entry foi feito em celular, escreva `1 cellphone for data entry, operated by Delegate <nome> (<WCA ID>)`.

### Venue > Venue Notes

Descreve o espaço: climatização, iluminação, ruído ambiente, assentos, equipamento fornecido pelo local (palco, backdrop, telão, impressora, som). Diga se o local era adequado ao porte do evento. Pontos fracos entram aqui com naturalidade — a ausência de microfone, por exemplo, atrapalha as chamadas e merece registro.

### Venue > Setup

Três parágrafos, um por área, nesta ordem: resolução, espera, embaralhamento.

A informação que o avaliador procura é se o embaralhamento ficou fora do campo de visão dos competidores e se quem aguardava não conseguia acompanhar as resoluções. Descreva o que criou a barreira física — faixas, mesas, cortinas, caixas, o vão do palco.

Se não houve área de espera, diga isso em uma linha (`uec26.md` faz assim).

### Organization > Organization team/Delegates

Duas fórmulas consagradas:

> Eu, <nome> (<WCA ID>), fui o principal responsável pela organização do evento, juntamente com os membros da Associação Amazonense de Cubo Mágico (AACM): <nomes com WCA ID>.

> O evento foi coordenado pelo delegado <nome> (<WCA ID>), com o apoio do delegado <nome> (<WCA ID>) e dos membros da Associação Amazonense de Cubo Mágico: <nomes>.

Em inglês a associação vira *Amazonas Rubik's Cube Association (AACM)*, ou o nome em português seguido da tradução entre parênteses.

WCA ID na primeira menção de cada pessoa. Confira a lista contra a página da competição: quem organizou de fato pode não constar lá, e quem consta pode não ter atuado — pergunte em vez de supor.

**Delegado trainee.** Quando há um, acrescente um bloco próprio depois dos parágrafos bilíngues:

```markdown
**Contribuição — <nome> (Delegado Trainee)**  
<o que ele assumiu no evento>
```

Descreva responsabilidades concretas: organizar grupos e chamar competidores, supervisionar runners e juízes, coordenar check-in, montar e desmontar timers, lançar resultados como data entry. Se foi a primeira competição dele na função, diga. Veja `cac26-etapapontanegra.md` para a versão em lista.

### Organization > Schedule

Quanto atrasou, por quê, e como terminou. As causas recorrentes nos exemplos: check-in demorado, emissão de súmulas, problemas de equipamento, transições lentas entre grupos, poucos competidores experientes, formato de limite de tempo em BLD.

Se a programação foi alterada no dia (final antecipada, formato de confronto direto), registre a mudança e o motivo.

Não escreva que os horários foram atualizados no site — é obrigação já coberta pela submissão.

### Organization > Budget

Uma frase com o resultado e quem administra o valor:

> A competição gerou um lucro de R$ <valor>. Esse montante será administrado por <pessoa ou entidade> e será utilizado para financiar futuras competições.

Prejuízo usa a forma espelhada: *apresentou um prejuízo de R$ <valor>, valor que será integralmente coberto por <pessoa>*.

Depois, um parágrafo sobre a composição: além das inscrições, houve venda de camisetas, patrocínio, cobrança de acompanhantes. Despesas típicas: taxas da WCA e da ABRACM, certificados, material gráfico, aluguel do espaço, lanches da equipe.

Fecha sempre com a remissão à planilha, com o link embutido na expressão:

> Informações detalhadas podem ser encontradas na planilha financeira da competição, disponível no [link](URL).

### Incidents

Separe em **Incidentes comuns** e **Incidentes notórios** (*Common incidents* / *Noteworthy Incidents*), usando só os subtítulos que se aplicam.

Comuns são os corriqueiros: troca de puzzle, scramble duplicado, timer G5 desligando ou entrando em modo 4-Pad, cabos falhando. Podem ir em lista.

Notórios pedem narrativa: o que aconteceu, como foi detectado, o que o staff fez, qual foi a decisão de regulamento. `cac26.md` (juiz sem cronometrar a inspeção) e `fac26-sides.md` (embaralhamento de Megaminx fora do padrão) são os modelos. Nomeie os envolvidos com WCA ID e descreva a resolução — nova tentativa com novo scramble, novo embaralhamento.

Sem nada a registrar: *O evento decorreu sem problemas, sem incidentes significativos a registar.*

### Remarks

Avaliação pessoal do delegado. É onde entram os aprendizados: necessidade de repensar divulgação, quantidade de competições no ano, treinamento da equipe, o que se aprendeu delegando em dupla.

Se o trainee mandou observações próprias, entram em bloco separado:

```markdown
**Observações do Delegado Trainee — <nome>**  
<texto dele>
```

## Voz

Primeira pessoa quando o delegado fala de si ("Eu, Thales Souza, fui..."), impessoal no resto. Frases diretas. Nada de adjetivação vaga: em vez de "o espaço era ótimo", diga o que o tornava adequado.

O relatório admite o que deu errado sem dramatizar. "O número de competidores ficou abaixo do esperado, o que reforça a necessidade de repensarmos as estratégias de divulgação" é o tom certo.
