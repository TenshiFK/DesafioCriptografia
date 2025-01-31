import os
import pyaes

## abrir o arquivo criptografado
file_name = "arquivoTexto.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## descriptografia
key = b"textoRansomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo normal
new_file = "arquivoTexto.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()