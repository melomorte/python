#escrevendo arquivos
arq = open('arquivo.txt', 'w'
arq.write('python para hackers')
arq.close()

#leitura de arquivos
arq = open('arquivo.txt', 'r')
texto = arq.read()
arq.close()

print(type(texto))
print(texto)