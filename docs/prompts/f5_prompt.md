Implemente em Python a seguinte função no arquivo src/consulta.py para o sistema de biblioteca:

Função: Buscar livros no acervo por titulo ou autor (busca parcial e case-insensitive).

Requisitos e regras:
- termo: Termo a ser pesquisado (nao pode ser vazio ou apenas espacos).
- acervo: Lista de dicionarios de livros, contendo ao menos 'titulo' e 'autor'.

Returns:
list[dict]: Lista com os livros que contem o termo no titulo ou no autor.

Raises:
ValueError: Caso o termo seja vazio ou nulo.