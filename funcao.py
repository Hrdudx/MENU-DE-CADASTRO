pessoas = []

def adicionar_pessoa(nome, idade):
    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

def listar_pessoas():
    return pessoas
