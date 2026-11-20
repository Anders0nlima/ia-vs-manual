"""Modulo de cadastros da biblioteca.

Funcoes:
- F1: cadastrar_livro
- F2: cadastrar_usuario
"""


def cadastrar_livro(titulo: str, autor: str, isbn: str) -> dict:
    """Cadastra um novo livro validando titulo, autor e ISBN (ISBN-10 ou ISBN-13).

    Args:
        titulo: Titulo da obra (obrigatorio, nao vazio).
        autor: Autor da obra (obrigatorio, nao vazio).
        isbn: Codigo ISBN (pode conter tracos/espacos).

    Returns:
        dict com os dados normalizados do livro cadastrado:
        {'id': int | str, 'titulo': str, 'autor': str, 'isbn': str}

    Raises:
        ValueError: Caso titulo ou autor sejam vazios, ou o ISBN seja invalido.
    """
    raise NotImplementedError("Funcao cadastrar_livro nao implementada ainda.")


def cadastrar_usuario(nome: str, cpf: str, email: str) -> dict:
    """Cadastra um novo usuario validando nome, CPF (11 digitos) e e-mail.

    Args:
        nome: Nome completo do usuario (obrigatorio, nao vazio).
        cpf: CPF com ou sem pontuacao (11 digitos numericos, nao repetidos).
        email: Endereco de e-mail valido.

    Returns:
        dict com os dados normalizados do usuario cadastrado:
        {'id': int | str, 'nome': str, 'cpf': str, 'email': str}

    Raises:
        ValueError: Caso nome seja vazio, CPF invalido ou e-mail invalido.
    """
    raise NotImplementedError("Funcao cadastrar_usuario nao implementada ainda.")
