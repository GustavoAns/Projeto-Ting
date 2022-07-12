import re


def exists_word(word, instance):
    max_texts = len(instance)
    all_finds = []
    for i in range(max_texts):
        obj = instance.search(i)
        arquivo_caminho = obj["nome_do_arquivo"]
        ocorrencias = []
        for raw_index in range(len(obj["linhas_do_arquivo"])):
            if re.search(
                word, obj["linhas_do_arquivo"][raw_index], re.IGNORECASE
            ):
                ocorrencias.append({"linha": raw_index + 1})
        if len(ocorrencias) > 0:
            all_finds.append(
                {
                    "palavra": word,
                    "arquivo": arquivo_caminho,
                    "ocorrencias": ocorrencias,
                }
            )
    return all_finds


def search_by_word(word, instance):
    max_texts = len(instance)
    all_finds = []
    for i in range(max_texts):
        obj = instance.search(i)
        arquivo_caminho = obj["nome_do_arquivo"]
        ocorrencias = []
        for raw_index in range(len(obj["linhas_do_arquivo"])):
            if re.search(
                word, obj["linhas_do_arquivo"][raw_index], re.IGNORECASE
            ):
                ocorrencias.append(
                    {
                        "linha": raw_index + 1,
                        "conteudo": obj["linhas_do_arquivo"][raw_index],
                    }
                )
        if len(ocorrencias) > 0:
            all_finds.append(
                {
                    "palavra": word,
                    "arquivo": arquivo_caminho,
                    "ocorrencias": ocorrencias,
                }
            )
    return all_finds
