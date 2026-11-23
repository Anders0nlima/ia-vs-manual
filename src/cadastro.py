"""Modulo de cadastros da biblioteca.

Funcoes:
- F1: cadastrar_livro
- F2: cadastrar_usuario
"""
#aceitar emails validos
from datetime import date
import re


def cadastrar_livro(
    titulo: str,
    autor: str,
    isbn: str,
    ano_publicacao: int | None = None,
) -> dict:
    """Cadastra um novo livro validando titulo, autor, ISBN e ano de publicacao.

    Args:
        titulo: Titulo da obra (obrigatorio, nao vazio).
        autor: Autor da obra (obrigatorio, nao vazio).
        isbn: Codigo ISBN (pode conter tracos/espacos).
        ano_publicacao: Ano de publicacao opcional (entre 1500 e o ano corrente).

    Returns:
        dict com os dados normalizados do livro cadastrado:
        {'id': int | str, 'titulo': str, 'autor': str, 'isbn': str, 'ano_publicacao': int | None}

    Raises:
        ValueError: Caso titulo/autor vazios, ISBN invalido ou ano de publicacao invalido.
    """

    if not titulo or not titulo.strip():
        raise ValueError("Titulo obrigatorio")
    if not autor or not autor.strip():
        raise ValueError("Autor obrigatorio")
    # Limpeza de espacos e tracos do ISBN
    isbn_limpo = isbn.replace("-", "").replace(" ", "").strip()
    # Validacao de ISBN-10 (9 digitos + 1 digito ou 'X')
    is_isbn10 = (
        len(isbn_limpo) == 10
        and isbn_limpo[:9].isdigit()
        and (isbn_limpo[9].isdigit() or isbn_limpo[9].upper() == "X")
    )
    # Validacao de ISBN-13 (13 digitos numericos)
    is_isbn13 = len(isbn_limpo) == 13 and isbn_limpo.isdigit()
    if not (is_isbn10 or is_isbn13):
        raise ValueError("ISBN invalido")

    if ano_publicacao is not None:
        ano_atual = date.today().year
        if (
            isinstance(ano_publicacao, bool)
            or not isinstance(ano_publicacao, int)
            or ano_publicacao < 1500
            or ano_publicacao > ano_atual
        ):
            raise ValueError("Ano de publicacao invalido")

    return {
        "id": 1,
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "isbn": isbn_limpo,
        "ano_publicacao": ano_publicacao,
    }


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
    if not nome or not nome.strip():
        raise ValueError("Nome obrigatorio")

    if not cpf:
        raise ValueError("CPF invalido")
    cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit() or len(set(cpf_limpo)) == 1:
        raise ValueError("CPF invalido")

    if not email or not re.match(r"^[^@\s]+@[^@\s\.]+(\.[^@\s\.]+)+$", email.strip()):
        raise ValueError("Email invalido")

    return {
        "id": 1,
        "nome": nome.strip(),
        "cpf": cpf_limpo,
        "email": email.strip().lower(),
    }