"""Modulo de consultas da biblioteca.

Funcoes:
- F5: buscar_livros
- F6: listar_emprestimos_atrasados
"""


def buscar_livros(termo: str, acervo: list[dict]) -> list[dict]:
    """Busca livros no acervo por titulo ou autor (busca parcial e case-insensitive).

    Args:
        termo: Termo a ser pesquisado (nao pode ser vazio ou apenas espacos).
        acervo: Lista de dicionarios de livros, contendo ao menos 'titulo' e 'autor'.

    Returns:
        list[dict]: Lista com os livros que contem o termo no titulo ou no autor.

    Raises:
        ValueError: Caso o termo seja vazio ou nulo.
    """
    if not termo or not termo.strip():
        raise ValueError("Termo de busca obrigatorio")

    termo_normalizado = termo.strip().lower()
    resultado = []

    for livro in acervo:
        titulo = livro.get("titulo", "").lower()
        autor = livro.get("autor", "").lower()
        if termo_normalizado in titulo or termo_normalizado in autor:
            resultado.append(livro)

    return resultado


def listar_emprestimos_atrasados(emprestimos: list[dict], data_referencia: str) -> list[dict]:
    """Filtra emprestimos ativos cuja data prevista de devolucao e anterior a data de referencia.

    Args:
        emprestimos: Lista de dicionarios de emprestimos, contendo:
                     'id', 'usuario_id', 'livro_id', 'data_prevista' (YYYY-MM-DD), 'status' ('ativo'|'devolvido')
        data_referencia: Data de corte no formato 'YYYY-MM-DD'.

    Returns:
        list[dict]: Lista de emprestimos que continuam 'ativo' e com 'data_prevista' < 'data_referencia'.

    Raises:
        ValueError: Caso a data de referencia nao esteja no formato ISO YYYY-MM-DD valido.
    """
    raise NotImplementedError("Funcao listar_emprestimos_atrasados nao implementada ainda.")
