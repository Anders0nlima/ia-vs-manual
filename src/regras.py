"""Modulo de regras de negocio da biblioteca.

Funcoes:
- F3: calcular_multa
- F4: validar_emprestimo
"""


# Autor: Ale
def calcular_multa(dias_atraso: int, valor_dia: float = 2.0, teto: float = 50.0) -> float:
    """Calcula o valor da multa por atraso na devolucao de um livro.

    Args:
        dias_atraso: Quantidade de dias em atraso (se <= 0, multa e 0.0).
        valor_dia: Valor cobrado por dia de atraso (padrao: R$ 2.00).
        teto: Valor maximo permitido para a multa (padrao: R$ 50.00).

    Returns:
        float: Valor da multa calculado, limitado pelo teto.
    """
    if dias_atraso <= 0:
        return 0.0
    
    multa_calculada = dias_atraso * valor_dia
    if multa_calculada > teto:
        return float(teto)
    
    return float(multa_calculada)


def validar_emprestimo(
    usuario_id: int | str,
    livros_emprestados: int,
    valor_multa_pendente: float,
    limite_livros: int = 3
) -> tuple[bool, str]:
    """Valida se o usuario pode realizar um novo emprestimo.

    Regras:
    1. Se houver qualquer valor de multa pendente (> 0.0), bloqueia.
    2. Se a quantidade de livros emprestados ja atingiu ou superou o limite, bloqueia.
    3. Caso contrario, autoriza.

    Args:
        usuario_id: Identificador do usuario.
        livros_emprestados: Quantidade de livros atualmente emprestados.
        valor_multa_pendente: Total em reais de multas nao pagas.
        limite_livros: Limite maximo de livros simultaneos (padrao: 3).

    Returns:
        tuple[bool, str]: (autorizado, motivo)
        Exemplos:
        - (True, "Emprestimo autorizado")
        - (False, "Usuario possui multa pendente")
        - (False, "Limite maximo de livros atingido")
    """
    raise NotImplementedError("Funcao validar_emprestimo nao implementada ainda.")
