# Planilha financeira

A WCA distribui um **LatAm Budget Template** no Google Sheets. O delegado copia esse template e preenche uma cópia por competição.

## Estrutura do template

Aba `Budget`, com a tabela de lançamentos nas linhas 2 a 13 e o total na linha 14:

| Coluna | Conteúdo |
| --- | --- |
| A — Item | Nome do lançamento |
| B — Type | `IN` ou `OUT` |
| C — Unit Value (Local) | Valor unitário |
| D — Amount | Quantidade (vazio = 1) |
| E — Total Value (Local) | **fórmula** |
| F — Total Value (USD) | **fórmula** |
| G — Description | Memória de cálculo |
| H — Receipt | Link do comprovante |

À direita, três campos de entrada: moeda local (K3), cotação do dólar (K4) e quem ficou com o lucro (J7, célula mesclada). As abas `Example` e `Example with loss` são referência e ficam como estão.

## Regras que evitam retrabalho

**Um arquivo por competição.** As somas do template apontam para a tabela nomeada `Competition_Budget`. Duplicar a aba `Budget` dentro do mesmo arquivo quebra o total, porque a segunda cópia não carrega a tabela nomeada. Copie o template inteiro quantas vezes forem necessárias.

**Preencha só as colunas de entrada.** A, B, C, D e G. As colunas E e F já têm fórmula e calculam sozinhas, inclusive o sinal negativo a partir do `Type`. Ao escrever com uma ferramenta que aceita valores nulos, passe `null` nas posições de E e F para preservar as fórmulas.

**Limpe as linhas não usadas.** O template vem com `IN` nas linhas 2–3 e `OUT` nas 4–8. Se a competição tem menos lançamentos, apague o `Type` das linhas sobrando.

**Registre a fonte da cotação.** A conversão em USD depende de K4. Se a competição caiu num fim de semana, use o fechamento comercial do último dia útil anterior e deixe a justificativa como nota na própria célula. Assim quem revisar entende de onde veio o número, e trocar o valor recalcula tudo.

**Rateio de custo compartilhado é decisão do delegado, não sua.** Quando duas competições dividem o espaço, pergunte como lançar o aluguel. Seja qual for a escolha, o relatório da competição que ficou sem o custo precisa explicar a ausência — senão parece omissão.

**A base de cálculo da taxa pode diferir da receita.** Inscrito que pagou e não compareceu entra na receita, mas a taxa ABRACM/WCA incide sobre competidores presentes. Confirme a diferença antes de lançar.

## Lançamentos típicos

Receitas: inscrições pelo site, inscrições no local (valor maior), inscrições de staff (valor reduzido), entrada de acompanhantes, venda de camisetas, patrocínio.

Despesas: taxas da ABRACM e da WCA por competidor, certificados de premiação, crachás e material gráfico, aluguel do espaço, lanches da equipe organizadora.

## Ferramentas

Para copiar o template e escrever nele você precisa do conector do **Google Drive** (cópia do arquivo) e do **Google Sheets** (escrita nas células). O Drive sozinho copia mas não escreve. Verifique os dois antes de prometer o serviço — se o de Sheets não estiver ativo, diga ao usuário que ele pode ativá-lo nas configurações de conectores da conversa, ou ofereça montar a planilha localmente e subir convertida.
