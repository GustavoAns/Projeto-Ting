import sys

def txt_importer(path_file):
    formato = path_file.split('.')[-1]
    if formato != 'txt':
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r', encoding='utf-8') as arquivo:
            return arquivo.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
