arquivo = open('14.arquivo.txt', 'w')  # Abre o arquivo em modo de escrita

arquivo.write("Curso Python Fundação bradesco \n")
arquivo.write("Aula Prática de manipulação de arquivos")
arquivo.close()  # Fecha o arquivo

#leitura do arquivo
leitura = open("14.arquivo.txt", "r")  # Abre o arquivo em modo de leitura
print(leitura.read())  # Lê o conteúdo do arquivo e imprime na tela
leitura.close()  # Fecha o arquivo

#Modo	Descrição
# r	Abre o arquivo somente para leitura.
# O arquivo deve já existir.

# r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
# A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.

# w	Abre o arquivo somente para escrita, no início do arquivo.
# Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.

# w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
# a	Abre o arquivo para escrita no final do arquivo.

# Não apaga o conteúdo preexistente.
# a+	Abre o arquivo para escrita no final do arquivo e leitura.