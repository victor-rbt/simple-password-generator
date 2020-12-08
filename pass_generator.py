import random

tamanho = 16
caracteres = 'abcdefghijklmnopqrstuvwxyz123456789^~´ç}{][)(-=+!#$%¨&><'

def gerar_senha(tamanho, caracteres):
	"""Cria uma senha de acordo com o tamanho e os caracteres aceitaveis"""
	senha = []
	for tam in range(tamanho):
		senha.append(random.choice(caracteres))

	return "".join(senha)

gerar_senha(tamanho=tamanho, caracteres=caracteres)
