# Plano de Implementação: Experimento "IA vs. À Mão" (Engenharia de Software II)

## 1. Contexto Acadêmico e Tema do Seminário

- **Disciplina**: Engenharia de Software II (2026.4)
- **Tema do Grupo**: **13. Produtividade com IA: Mais Código Significa Melhor Desempenho?**
  - **Teoria**: Limitações de métricas superficiais (Linhas de Código - LoC, número de commits, velocidade aparente); retrabalho, densidade de defeitos, manutenibilidade e valor real entregue.
  - **Prática**: Experimento empírico controlado comparando desenvolvimento de um sistema de biblioteca em Python implementado à mão vs. assistido por IA.
- **Estrutura da Apresentação (18 minutos)**:
  - *Contextualização e Problema* (3 min)
  - *Fundamentação Teórica e Evidências* (5 min) - Artigos empíricos (ex: DORA, estudos GitClear sobre qualidade de código com IA, estudos de Copilot).
  - *Demonstração Prática e Experimento* (7 min) - Apresentação do repositório, métricas coletadas, gráficos comparativos e rodada de manutenção.
  - *Análise Crítica e Conclusão* (3 min) - Mais código gerado = melhor desempenho? Discussão das conclusões conflitantes.

---

## 2. Escopo e Estrutura do Sistema de Biblioteca

O sistema é composto por **6 funções em Python**, organizadas em 3 pares de complexidade equivalente:

| Par | Categoria | Integrante Responsável | Função A | Função B |
| :--- | :--- | :--- | :--- | :--- |
| **Par 1** | Cadastro | **Anderson** | **F1**: Cadastrar livro (validar ISBN e título) | **F2**: Cadastrar usuário (validar CPF e e-mail) |
| **Par 2** | Regra de Negócio | **Ale** | **F3**: Calcular multa por atraso (valor/dia + teto) | **F4**: Validar empréstimo (limite livros + bloqueio multa) |
| **Par 3** | Consulta | **Edi** | **F5**: Buscar livro por título ou autor | **F6**: Listar empréstimos atrasados |

### Distribuição Cruzada de Manutenção (Avaliação Às Cegas)
Cada integrante desenvolve 1 função à mão e 1 com IA. Na fase final de manutenção, troca de funções e faz um ajuste sem saber a priori se o código original foi gerado por IA ou feito à mão:
- **Anderson**: Implementa F1 e F2 | Faz manutenção em **F5 e F6**
- **Ale**: Implementa F3 e F4 | Faz manutenção em **F1 e F2**
- **Edi**: Implementa F5 e F6 | Faz manutenção em **F3 e F4**

---

## 3. Estrutura de Pastas e Arquitetura do Repositório

```text
biblioteca-ia-vs-mao/
├── .github/
│   └── workflows/
│       └── ci.yml               # CI opcional para rodar testes e métricas
├── docs/
│   ├── metricas/
│   │   ├── tabela_metricas.csv  # Planilha de dados brutos
│   │   └── relatorio_analise.md # Análise estatística e conclusões
│   └── prompts/
│       ├── f1_prompt.md         # Registro do prompt usado se F1 for IA
│       ├── f2_prompt.md
│       ├── f3_prompt.md
│       ├── f4_prompt.md
│       ├── f5_prompt.md
│       └── f6_prompt.md
├── src/
│   ├── __init__.py
│   ├── cadastro.py              # F1 e F2
│   ├── regras.py                # F3 e F4
│   └── consulta.py              # F5 e F6
├── tests/
│   ├── __init__.py
│   ├── test_cadastro.py         # 4 a 6 testes para F1 e F2
│   ├── test_regras.py           # 4 a 6 testes para F3 e F4
│   └── test_consulta.py         # 4 a 6 testes para F5 e F6
├── PLANO_DE_IMPLEMENTACAO.md    # Este documento
├── PROMPT_CONTEXTO_IA.md        # Prompt portátil para alimentar IAs em outras máquinas
├── README.md                    # Especificação completa dos requisitos de negócio
└── requirements.txt             # pytest, radon, flake8, pylint
```

---

## 4. Padrão Rigoroso de Branches e Commits

Para garantir rastreabilidade científica dos dados, as regras abaixo são inegociáveis:

### 4.1. Branches
- `main`: Branch de código integrado (somente recebe PR).
- `setup/estrutura-e-testes`: Branch inicial para o esqueleto do projeto e bateria de testes TDD.
- **Branches de Implementação**:
  - `f1-cadastrar-livro-mao` ou `f1-cadastrar-livro-ia`
  - `f2-cadastrar-usuario-mao` ou `f2-cadastrar-usuario-ia`
  - `f3-calcular-multa-mao` ou `f3-calcular-multa-ia`
  - `f4-validar-emprestimo-mao` ou `f4-validar-emprestimo-ia`
  - `f5-buscar-livro-mao` ou `f5-buscar-livro-ia`
  - `f6-listar-atrasados-mao` ou `f6-listar-atrasados-ia`
- **Branches de Manutenção**:
  - `manut/f1-mao`, `manut/f2-ia`, etc.

### 4.2. Formato de Commit
```text
tipo(escopo): descricao
```
- **Tipos permitidos**: `feat`, `fix`, `test`, `refactor`, `docs`, `chore`.
- **Regras**:
  - Mensagens **sempre sem acento** para evitar conflitos de encoding.
  - **Proibido `git push --force` e `git rebase`** nas branches das funções.
  - **Merge padrão (sem squash)** nos Pull Requests para preservar todos os commits no histórico.

### 4.3. Fluxo de Commits Obrigatório

#### Para funções À MÃO:
1. `chore(fN-mao): inicio` *(Inicia o cronômetro)*
2. Commits pequenos e granulares a cada etapa da implementação:
   - `feat(fN-mao): validacao de isbn`
   - `fix(fN-mao): corrige tratamento de espacos no titulo`
3. `chore(fN-mao): fim` *(Para o cronômetro)*

#### Para funções COM IA:
1. `chore(fN-ia): inicio` *(Inicia o cronômetro)*
2. `docs(fN-ia): prompt v1` *(Salva o prompt exatamente como enviado na pasta docs/prompts/)*
3. `feat(fN-ia): codigo gerado pela IA sem edicao` *(Código bruto colado diretamente)*
4. *Se houver defeito:*
   - `fix(fN-ia): correcao pedida a IA (prompt v2)` *(Máximo de 3 iterações com IA)*
5. *Se a IA não resolver ou precisar de ajuste:*
   - `fix(fN-ia): ajuste manual` *(Qualquer alteração feita manualmente pelo desenvolvedor)*
6. `chore(fN-ia): fim` *(Para o cronômetro)*

#### Para a fase de Manutenção:
1. `chore(manut-fN-modo): inicio`
2. `feat(manut-fN-modo): implementa alteracao solicitada`
3. `fix(manut-fN-modo): ajuste de teste da alteracao` (se necessário)
4. `chore(manut-fN-modo): fim`

---

## 5. Roteiro de Execução Passo a Passo

### Etapa 1: Setup Inicial e TDD (Anderson)
1. Criar branch `setup/estrutura-e-testes`.
2. Criar `requirements.txt` com as ferramentas de teste e métricas:
   ```text
   pytest>=8.0.0
   radon>=6.0.0
   flake8>=7.0.0
   pylint>=3.0.0
   ```
3. Criar `README.md` com a especificação funcional detalhada de cada uma das 6 funções (regras de validação, entradas e saídas esperadas).
4. Implementar a suite de testes unitários em `tests/` (de 4 a 6 testes por função).
5. Validar que todos os testes rodam e falham (ou dão `NotImplementedError`).
6. Abrir PR para `main` e realizar o merge.

### Etapa 2: Sorteio e Divisão
1. Fazer o sorteio (cara ou coroa) para cada integrante definir qual função é à mão e qual é com IA.
2. Atualizar o quadro de branches e atribuir formalmente.

### Etapa 3: Desenvolvimento e Cronometragem (Anderson, Ale, Edi)
1. Cada membro baixa a `main` atualizada.
2. Cria sua branch respectiva (`fX-...-mao` ou `fX-...-ia`).
3. Dispara o cronômetro no primeiro commit (`inicio`).
4. Segue as regras estritas de commits para IA ou manual.
5. Testa localmente com `pytest`.
6. Finaliza com o commit de encerramento (`fim`).
7. Abre o Pull Request para `main` com o título padronizado (Ex: `F1: cadastrar livro [MAO]`).
8. Realiza merge com commit de merge normal.

### Etapa 4: Extração das Métricas Técnicas
Com todas as 6 funções na `main`, rodar as ferramentas automatizadas:
- **Defeitos e conformidade**:
  ```bash
  pytest
  ```
- **Complexidade ciclomática**:
  ```bash
  radon cc -s -a src/
  radon raw -s src/
  ```
- **Conformidade de estilo e alertas**:
  ```bash
  flake8 src/
  ```
- **Detecção de código duplicado**:
  ```bash
  pylint --disable=all --enable=duplicate-code src/
  ```
- **Linhas de código e commits**:
  - Extrair contagem de commits (`git log --oneline | wc -l`).
  - Extrair LoC das funções.
  - Calcular tempo decorrido entre o commit `inicio` e `fim`.

### Etapa 5: Rodada de Manutenção Cruzada (Às Cegas)
1. Definir uma solicitação de mudança idêntica para cada par de funções:
   - Exemplo Par 1 (Cadastro): Adicionar campo `data_cadastro` com validação de data futura.
   - Exemplo Par 2 (Regras): Adicionar parâmetro de desconto para dias úteis vs fins de semana.
   - Exemplo Par 3 (Consulta): Adicionar ordenação alfabética opcional no retorno.
2. Cada integrante recebe as 2 funções do seu par atribuído de manutenção sem saber qual foi IA e qual foi manual.
3. Cronometrar o tempo necessário para entender o código e implementar a mudança com testes passando.
4. Registrar a pontuação de facilidade subjetiva (1 a 5) e tempo de manutenção.

### Etapa 6: Consolidação e Tabela Final
Consolidar a planilha `docs/metricas/tabela_metricas.csv` com as seguintes colunas:
- `funcao`: F1 a F6
- `metodo`: MAO vs IA
- `autor`: Anderson / Ale / Edi
- `tempo_desenvolvimento_min`: Minutos cronometrados
- `qtd_commits`: Número total de commits da branch
- `qtd_correcoes_retrabalho`: Número de commits `fix` ou rodadas de prompt
- `linhas_codigo_loc`: LoC da implementação
- `complexidade_ciclomatica`: Média Radon
- `alertas_flake8`: Quantidade de warnings/erros
- `testes_falharam_inicial`: Falhas na primeira execução
- `tempo_manutencao_min`: Tempo para aplicar a mudança
- `manutencao_avaliador`: Quem fez a manutenção
- `dificuldade_percebida_1_a_5`: Nota qualitativa

---

## 6. Conexão com o Seminário: "Mais Código Significa Melhor Desempenho?"

O experimento gerará evidências concretas para responder aos pontos centrais da apresentação:
1. **O Mito das Métricas de Volume**:
   - A IA frequentemente gera mais linhas de código e estruturas mais verbosas. Isso resultou em melhor código ou maior custo cognitivo de leitura?
2. **Tempo Bruto vs. Retrabalho**:
   - A IA entregou a primeira versão mais rápido? Mas quanto tempo foi gasto depurando alucinações, prompts de correção ou ajustes manuais?
3. **A Armadilha da Manutenibilidade (Código que outros precisam alterar)**:
   - Na rodada de manutenção às cegas, foi mais fácil alterar o código feito por um colega à mão ou o código gerado por IA?
4. **Conclusões Científicas**:
   - Articular os resultados com literatura acadêmica (ex: papers sobre *AI-generated code quality decay*, *Technical Debt in the era of LLMs*).
