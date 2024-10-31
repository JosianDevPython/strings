nome = "\t  Josian Henrique   \n"

print("nome original com espaços em branco")
print(repr(nome))

nome_sem_espacos_a_direita = nome.rstrip()
nome_sem_espacos_a_esquerda = nome.lstrip()
nome_sem_espacos = nome.strip()

print("\nNome sem espaços a direita")
print(repr(nome_sem_espacos_a_direita))

print("\nNome sem espaços a esquerda")
print(repr(nome_sem_espacos_a_esquerda))

print("\nNome sem espaços")
print(repr(nome_sem_espacos))

"""
nome = "  Josian Henrique  "
print(repr(nome.strip()))
print(repr(nome.lstrip()))
print(repr(nome.rstrip()))
"""


