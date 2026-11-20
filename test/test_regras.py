import pytest
from regras import calcular_multa, validar_emprestimo


# ==========================================================
# TESTES PARA F3: CALCULAR MULTA
# ==========================================================

def test_calcular_multa_sem_atraso():
    assert calcular_multa(dias_atraso=0) == 0.0


def test_calcular_multa_dias_negativos():
    assert calcular_multa(dias_atraso=-5) == 0.0


def test_calcular_multa_dentro_do_limite():
    # 5 dias * R$ 2.00 = R$ 10.00
    assert calcular_multa(dias_atraso=5, valor_dia=2.0, teto=50.0) == 10.0


def test_calcular_multa_atinge_teto():
    # 30 dias * R$ 2.00 = R$ 60.00 -> deve limitar a R$ 50.00
    assert calcular_multa(dias_atraso=30, valor_dia=2.0, teto=50.0) == 50.0


def test_calcular_multa_valores_customizados():
    # 4 dias * R$ 3.50 = R$ 14.00 (teto R$ 20.00)
    assert calcular_multa(dias_atraso=4, valor_dia=3.5, teto=20.0) == 14.0


# ==========================================================
# TESTES PARA F4: VALIDAR EMPRESTIMO
# ==========================================================

def test_validar_emprestimo_autorizado():
    autorizado, motivo = validar_emprestimo(usuario_id=1, livros_emprestados=1, valor_multa_pendente=0.0)
    assert autorizado is True
    assert "autorizado" in motivo.lower()


def test_validar_emprestimo_bloqueado_por_multa():
    autorizado, motivo = validar_emprestimo(usuario_id=1, livros_emprestados=0, valor_multa_pendente=10.0)
    assert autorizado is False
    assert "multa" in motivo.lower()


def test_validar_emprestimo_bloqueado_por_limite():
    # Limite padrao e 3
    autorizado, motivo = validar_emprestimo(usuario_id=1, livros_emprestados=3, valor_multa_pendente=0.0)
    assert autorizado is False
    assert "limite" in motivo.lower()


def test_validar_emprestimo_prioridade_bloqueio_multa():
    # Quando ha multa e limite excedido ao mesmo tempo, deve bloquear
    autorizado, motivo = validar_emprestimo(usuario_id=1, livros_emprestados=3, valor_multa_pendente=15.0)
    assert autorizado is False


def test_validar_emprestimo_limite_customizado():
    autorizado, motivo = validar_emprestimo(
        usuario_id=1,
        livros_emprestados=4,
        valor_multa_pendente=0.0,
        limite_livros=5
    )
    assert autorizado is True
