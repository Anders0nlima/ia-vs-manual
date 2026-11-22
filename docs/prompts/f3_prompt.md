Implemente em Python a seguinte funcao no arquivo src/regras.py para o sistema de biblioteca:

Funcao: calcular_multa(dias_atraso: int, valor_dia: float = 2.0, teto: float = 50.0) -> float

Requisitos e Regras:
- Se dias_atraso <= 0, retornar 0.0.
- Caso contrario, multa = dias_atraso * valor_dia.
- Se a multa ultrapassar o teto, retornar o valor do teto.
- Retornar sempre um float.
- Manter docstring completa e tipagem.
- Adicionar o comentario "# Autor: Ale" imediatamente acima da definicao da funcao.
