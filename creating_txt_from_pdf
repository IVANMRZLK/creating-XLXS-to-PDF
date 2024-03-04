import pdfminer.high_level
import os

pdf_directory_path = 'Директория для конвертируемых PDF'

pdf_list = os.listdir(pdf_directory_path)

print('Началась конвертация pdf в txt')
for pdf in pdf_list:
    with open(f'pdf/{pdf}', 'rb') as file:
        name_txt = pdf[:-4]
        print(name_txt)
        file1 = open(f'ptxt/{name_txt}', 'a+')
        pdfminer.high_level.extract_text_to_fp(file, file1)
        file1.close()
print('Конвертация pdf в txt завершена')
