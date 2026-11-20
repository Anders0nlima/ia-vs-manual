Implemente em Python a seguinte função no arquivo src/cadastro.py para o sistema de biblioteca:

Função: cadastrar_livro(titulo: str, autor: str, isbn: str) -> dict

Requisitos e Validações:

titulo: obrigatório, não pode ser vazio ou conter apenas espaços. Caso inválido, lançar ValueError("Titulo obrigatorio").
autor: obrigatório, não pode ser vazio ou conter apenas espaços. Caso inválido, lançar ValueError("Autor obrigatorio").
isbn: aceita ISBN-10 (10 caracteres, os 9 primeiros dígitos e o último dígito ou 'X'/'x') ou ISBN-13 (13 dígitos numéricos). Espaços e traços devem ser limpos/removidos. Caso não atenda a esses formatos, lançar ValueError("ISBN invalido").
Retorno: dict normalizado com: {'id': 1, 'titulo': str, 'autor': str, 'isbn': str} (com titulo e autor sem espaços extras nas pontas e isbn apenas com os caracteres limpos).