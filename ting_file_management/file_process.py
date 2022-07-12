import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    max_texts = len(instance)
    if max_texts > 0:
        for i in range(max_texts):     
            obj = instance.search(i)
            if obj['nome_do_arquivo'] == path_file:
                return
    list_text = txt_importer(path_file)
    new_obj_text = {'nome_do_arquivo': path_file, 'qtd_linhas': len(list_text), 'linhas_do_arquivo': list_text}
    instance.enqueue(new_obj_text)
    sys.stdout.write(str(new_obj_text))

def remove(instance):
    max_texts = len(instance)
    if max_texts == 0:
        return sys.stdout.write('Não há elementos\n')
    
    path_file = instance.search(0)['nome_do_arquivo']
    
    instance.dequeue()
    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        text_obj = instance.search(position)
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
    return sys.stdout.write(str(text_obj))