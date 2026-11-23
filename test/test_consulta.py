import pytest
from consulta import buscar_livros, listar_emprestimos_atrasados


# ==========================================================
# FIXTURE PARA O ACERVO E EMPRESTIMOS
# ==========================================================

@pytest.fixture
def acervo_exemplo():
    return [
        {"id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin", "isbn": "9780132350884"},
        {"id": 2, "titulo": "The Pragmatic Programmer", "autor": "Andy Hunt, Dave Thomas", "isbn": "9780201616224"},
        {"id": 3, "titulo": "Padroes de Projetos", "autor": "Erich Gamma et al.", "isbn": "9788573076103"},
        {"id": 4, "titulo": "Entendendo Algoritmos", "autor": "Aditya Y. Bhargava", "isbn": "9788575225639"},
    ]


@pytest.fixture
def emprestimos_exemplo():
    return [
        {"id": 101, "usuario_id": 1, "livro_id": 1, "data_prevista": "2026-11-10", "status": "ativo"},
        {"id": 102, "usuario_id": 2, "livro_id": 2, "data_prevista": "2026-11-25", "status": "ativo"},
        {"id": 103, "usuario_id": 3, "livro_id": 3, "data_prevista": "2026-11-05", "status": "devolvido"},
        {"id": 104, "usuario_id": 1, "livro_id": 4, "data_prevista": "2026-11-15", "status": "ativo"},
    ]


# ==========================================================
# TESTES PARA F5: BUSCAR LIVROS
# ==========================================================

def test_buscar_livros_por_titulo(acervo_exemplo):
    resultado = buscar_livros("Clean", acervo_exemplo)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Clean Code"


def test_buscar_livros_por_autor(acervo_exemplo):
    resultado = buscar_livros("Martin", acervo_exemplo)
    assert len(resultado) == 1
    assert resultado[0]["autor"] == "Robert C. Martin"


def test_buscar_livros_case_insensitive(acervo_exemplo):
    resultado = buscar_livros("algoritmos", acervo_exemplo)
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Entendendo Algoritmos"


def test_buscar_livros_nao_encontrado(acervo_exemplo):
    resultado = buscar_livros("Livro Inexistente", acervo_exemplo)
    assert resultado == []


def test_buscar_livros_termo_vazio(acervo_exemplo):
    with pytest.raises(ValueError, match="Termo"):
        buscar_livros("   ", acervo_exemplo)

def test_buscar_livros_ordenado_por_titulo(acervo_exemplo):
    resultado = buscar_livros("e", acervo_exemplo, ordenar_titulo=True)
    titulos = [l["titulo"] for l in resultado]
    assert titulos == sorted(titulos)

# ==========================================================
# TESTES PARA F6: LISTAR EMPRESTIMOS ATRASADOS
# ==========================================================

def test_listar_emprestimos_atrasados_sucesso(emprestimos_exemplo):
    # Data de referencia: 2026-11-20
    # Emprestimos com data_prevista < 2026-11-20 e status ativo: 101 (2026-11-10) e 104 (2026-11-15)
    resultado = listar_emprestimos_atrasados(emprestimos_exemplo, "2026-11-20")
    ids_atrasados = [e["id"] for e in resultado]
    assert len(resultado) == 2
    assert 101 in ids_atrasados
    assert 104 in ids_atrasados


def test_listar_emprestimos_ignora_devolvidos(emprestimos_exemplo):
    # O emprestimo 103 tem data prevista 2026-11-05 mas ja foi devolvido
    resultado = listar_emprestimos_atrasados(emprestimos_exemplo, "2026-11-20")
    ids_atrasados = [e["id"] for e in resultado]
    assert 103 not in ids_atrasados


def test_listar_emprestimos_nenhum_atrasado(emprestimos_exemplo):
    # Em data anterior a todos os vencimentos, nenhum deve estar atrasado
    resultado = listar_emprestimos_atrasados(emprestimos_exemplo, "2026-11-01")
    assert resultado == []


def test_listar_emprestimos_limite_mesmo_dia(emprestimos_exemplo):
    # Emprestimo que vence hoje nao esta atrasado (atraso ocorre quando data_prevista < data_referencia)
    resultado = listar_emprestimos_atrasados(emprestimos_exemplo, "2026-11-10")
    ids_atrasados = [e["id"] for e in resultado]
    assert 101 not in ids_atrasados


def test_listar_emprestimos_data_invalida(emprestimos_exemplo):
    with pytest.raises(ValueError, match="Data"):
        listar_emprestimos_atrasados(emprestimos_exemplo, "20-11-2026")

def test_listar_emprestimos_atrasados_dias_minimos(emprestimos_exemplo):
    resultado = listar_emprestimos_atrasados(
        emprestimos_exemplo, "2026-11-20", dias_minimos_atraso=7
    )
    ids_atrasados = [e["id"] for e in resultado]
    assert len(resultado) == 1
    assert 101 in ids_atrasados
    assert 104 not in ids_atrasados