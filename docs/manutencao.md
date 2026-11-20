# Instruções da Rodada de Manutenção (Avaliação Às Cegas)

## Objetivo
Avaliar a **manutenibilidade** do código gerado por IA vs. feito à mão. Cada integrante receberá 2 funções implementadas por outro colega e aplicará a mesma alteração pedida, **sem saber previamente qual foi feita por IA e qual foi à mão**.

---

## Escala de Troca de Funções
- **Anderson**: Realiza a manutenção nas funções **F5 e F6** (feitas por Edi).
- **Ale**: Realiza a manutenção nas funções **F1 e F2** (feitas por Anderson).
- **Edi**: Realiza a manutenção nas funções **F3 e F4** (feitas por Ale).

---

## Alterações Solicitadas para Cada Par

### Par 1: Cadastro (F1 e F2) - Avaliado por Ale
- **F1 (cadastrar_livro)**: Adicionar campo opcional `ano_publicacao: int | None = None`. Se fornecido, deve ser um ano válido (entre 1500 e o ano corrente). Se inválido, lançar `ValueError("Ano de publicacao invalido")`.
- **F2 (cadastrar_usuario)**: Adicionar campo opcional `telefone: str | None = None`. Se fornecido, deve ter entre 10 e 11 dígitos numéricos após remover formatação. Se inválido, lançar `ValueError("Telefone invalido")`.

### Par 2: Regra de Negócio (F3 e F4) - Avaliado por Edi
- **F3 (calcular_multa)**: Adicionar parâmetro booleano `is_estudante: bool = False`. Se for estudante, aplicar 50% de desconto sobre o valor calculado da multa antes de conferir o teto.
- **F4 (validar_emprestimo)**: Adicionar parâmetro `bloqueado_judicialmente: bool = False`. Se for `True`, bloquear imediatamente com motivo `"Usuario bloqueado judicialmente"`.

### Par 3: Consulta (F5 e F6) - Avaliado por Anderson
- **F5 (buscar_livros)**: Adicionar parâmetro booleano `ordenar_titulo: bool = False`. Se `True`, retornar a lista de livros encontrados ordenada alfabeticamente pelo título.
- **F6 (listar_emprestimos_atrasados)**: Adicionar parâmetro opcional `dias_minimos_atraso: int = 1`. Filtrar apenas os empréstimos com atraso igual ou superior a essa quantidade de dias.

---

## Como Registrar a Manutenção
1. Crie a branch de manutenção: `manut/fN-mao` ou `manut/fN-ia`.
2. Commit de início: `chore(manut-fN-modo): inicio` (Dispare o cronômetro).
3. Implemente a alteração e ajuste os testes unitários.
4. Commit de conclusão: `chore(manut-fN-modo): fim` (Pare o cronômetro).
5. Preencha os dados de tempo e nota de dificuldade (1 a 5) em `docs/metricas.csv`.
