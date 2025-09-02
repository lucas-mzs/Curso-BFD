import os
from tkinter.filedialog import askdirectory
import shutil


nome_pasta_selecionada = askdirectory()
print('Pasta selecionada: ', nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada)
print('Itens encontrados: ', lista_arquivos)

nome_pasta_backup = 'backup'
nm_completo_para_backup = os.path.join(nome_pasta_selecionada, nome_pasta_backup)

if not os.path.exists(nm_completo_para_backup):
    os.makedirs(nm_completo_para_backup, exist_ok=True)

for biblioteca in lista_arquivos:
    print('Processado: ',biblioteca)

    caminho_origem = os.path.join(nome_pasta_selecionada, biblioteca)
    caminho_destino = os.path.join(nm_completo_para_backup, biblioteca)

    if biblioteca == 'backup':
        continue

    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
    elif os.path.isdir(caminho_origem):
        if os.path.exists(caminho_destino):
            shutil.rmtree(caminho_destino)
        shutil.copytree(caminho_origem, caminho_destino)