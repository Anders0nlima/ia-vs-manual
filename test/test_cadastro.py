import pytest
from cadastro import cadastrar_livro, cadastrar_usuario


# ==========================================================
# TESTES PARA F1: CADASTRAR LIVRO
# ==========================================================

def test_cadastrar_livro_sucesso_isbn10():
    livro = cadastrar_livro("Dom Casmurro", "Machado de Assis", "0-306-40615-2")
    assert livro["titulo"] == "Dom Casmurro"
    assert livro["autor"] == "Machado de Assis"
    assert livro["isbn"] == "0306406152"
    assert "id" in livro


def test_cadastrar_livro_sucesso_isbn13():
    livro = cadastrar_livro("O Cortico", "Aluisio Azevedo", "978-85-359-0277-8")
    assert livro["titulo"] == "O Cortico"
    assert livro["autor"] == "Aluisio Azevedo"
    assert livro["isbn"] == "9788535902778"
    assert "id" in livro


def test_cadastrar_livro_titulo_vazio():
    with pytest.raises(ValueError, match="Titulo"):
        cadastrar_livro("   ", "Autor Valido", "9788535902778")


def test_cadastrar_livro_autor_vazio():
    with pytest.raises(ValueError, match="Autor"):
        cadastrar_livro("Titulo Valido", "", "9788535902778")


def test_cadastrar_livro_isbn_invalido():
    with pytest.raises(ValueError, match="ISBN"):
        cadastrar_livro("Titulo Valido", "Autor Valido", "12345")


# ==========================================================
# TESTES PARA F2: CADASTRAR USUARIO
# ==========================================================

def test_cadastrar_usuario_sucesso():
    usuario = cadastrar_usuario("Maria Silva", "123.456.789-01", "maria@email.com")
    assert usuario["nome"] == "Maria Silva"
    assert usuario["cpf"] == "12345678901"
    assert usuario["email"] == "maria@email.com"
    assert "id" in usuario


def test_cadastrar_usuario_nome_vazio():
    with pytest.raises(ValueError, match="Nome"):
        cadastrar_usuario("  ", "12345678901", "maria@email.com")


def test_cadastrar_usuario_cpf_invalido_tamanho():
    with pytest.raises(ValueError, match="CPF"):
        cadastrar_usuario("Maria Silva", "12345", "maria@email.com")


def test_cadastrar_usuario_cpf_digitos_iguais():
    with pytest.raises(ValueError, match="CPF"):
        cadastrar_usuario("Maria Silva", "111.111.111-11", "maria@email.com")


def test_cadastrar_usuario_email_invalido():
    with pytest.raises(ValueError, match="Email"):
        cadastrar_usuario("Maria Silva", "12345678901", "maria_sem_arroba.com")


def test_cadastrar_usuario_com_telefone_valido_10_digitos():
    usuario = cadastrar_usuario(
        "Maria Silva", "123.456.789-01", "maria@email.com", "(11) 3456-7890"
    )
    assert usuario["telefone"] == "1134567890"


def test_cadastrar_usuario_com_telefone_valido_11_digitos():
    usuario = cadastrar_usuario(
        "Maria Silva", "123.456.789-01", "maria@email.com", "(11) 98765-4321"
    )
    assert usuario["telefone"] == "11987654321"


def test_cadastrar_usuario_telefone_invalido():
    with pytest.raises(ValueError, match="Telefone invalido"):
        cadastrar_usuario(
            "Maria Silva", "123.456.789-01", "maria@email.com", "12345"
        )
