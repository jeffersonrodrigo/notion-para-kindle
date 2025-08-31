# -*- coding: utf-8 -*-
import requests
import sys
import os

# ==============================================================================
# CONFIGURAÇÕES
# ==============================================================================
TOKEN_NOTION = os.environ.get("TOKEN_NOTION")
ID_DA_PAGINA = os.environ.get("ID_DA_PAGINA")
NOME_ARQUIVO_SAIDA = "pagina_exportada.md"
HEADERS = {
    "Authorization": f"Bearer {TOKEN_NOTION}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

# ==============================================================================
# FUNÇÕES DE CONVERSÃO
# ==============================================================================

def converter_rich_text(rich_text_array: list) -> str:
    partes_markdown = []
    for fragmento in rich_text_array:
        texto = fragmento.get("plain_text", "")
        anotacoes = fragmento.get("annotations", {})
        link = fragmento.get("href")
        if anotacoes.get("bold"): texto = f"**{texto}**"
        if anotacoes.get("italic"): texto = f"*{texto}*"
        if anotacoes.get("strikethrough"): texto = f"~~{texto}~~"
        if anotacoes.get("code"): texto = f"`{texto}`"
        if anotacoes.get("underline"): texto = f"<u>{texto}</u>"
        if link: texto = f"[{texto}]({link})"
        partes_markdown.append(texto)
    return "".join(partes_markdown)

def converter_bloco(bloco: dict, nivel: int) -> str:
    """Converte um bloco do Notion para Markdown, considerando o nível de aninhamento."""
    tipo_bloco = bloco["type"]
    conteudo = bloco.get(tipo_bloco, {})
    texto_convertido = ""
    if "rich_text" in conteudo and conteudo["rich_text"]:
        texto_convertido = converter_rich_text(conteudo["rich_text"])
    
    # Lógica recursiva para buscar blocos filhos, se existirem
    if bloco.get("has_children"):
        blocos_filhos = buscar_e_converter_blocos(bloco["id"], nivel + 1)
        # Os filhos são juntados abaixo do texto do pai. A indentação é tratada por cada filho.
        filhos_formatados = "\n".join(blocos_filhos)
        texto_convertido += "\n" + filhos_formatados

    recuo = "  " * nivel

    if tipo_bloco == "heading_1": return f"# {texto_convertido}"
    elif tipo_bloco == "heading_2": return f"## {texto_convertido}"
    elif tipo_bloco == "heading_3": return f"### {texto_convertido}"
    elif tipo_bloco == "paragraph": return f"{recuo}{texto_convertido}" if nivel > 0 else texto_convertido
    elif tipo_bloco == "bulleted_list_item":
        return f"{recuo}- {texto_convertido}"
    elif tipo_bloco == "numbered_list_item":
        return f"{recuo}1. {texto_convertido}"
    elif tipo_bloco == "to_do":
        marcado = "x" if conteudo.get("checked") else " "
        return f"{recuo}- [{marcado}] {texto_convertido}"
    elif tipo_bloco == "quote":
        # Formata a citação e indenta as linhas seguintes se for aninhada
        linhas = texto_convertido.split('\n')
        return f"{recuo}> " + f"\n{recuo}> ".join(linhas)
    elif tipo_bloco == "divider": return "---"
    elif tipo_bloco == "callout":
        # Formata o callout como um bloco de citação, indentando corretamente
        linhas = texto_convertido.split('\n')
        return f"{recuo}> " + f"\n{recuo}> ".join(linhas)
    elif tipo_bloco == "code":
        linguagem = conteudo.get("language", "plaintext")
        # Bloco de código não deve ter seu conteúdo aninhado recursivamente
        texto_codigo = converter_rich_text(conteudo['rich_text'])
        return f"{recuo}```{linguagem}\n{texto_codigo}\n{recuo}```"
    else: return f"<!-- Bloco do tipo '{tipo_bloco}' não suportado -->"


def buscar_e_converter_blocos(id_do_bloco_pai: str, nivel: int) -> list:
    """Busca os filhos de um bloco, passando o nível de profundidade para a conversão."""
    url = f"https://api.notion.com/v1/blocks/{id_do_bloco_pai}/children"
    parametros = {"page_size": 100}
    blocos_markdown = []
    tem_mais_paginas = True
    while tem_mais_paginas:
        try:
            resposta = requests.get(url, headers=HEADERS, params=parametros)
            resposta.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"ERRO DE CONEXÃO ao buscar blocos filhos: {e}")
            return []
        
        dados = resposta.json()
        for bloco in dados.get("results", []):
            blocos_markdown.append(converter_bloco(bloco, nivel))
            
        if dados.get("has_more"):
            parametros["start_cursor"] = dados.get("next_cursor")
        else:
            tem_mais_paginas = False
            
    return blocos_markdown

def main():
    print("Iniciando a exportação da página do Notion...")
    if not TOKEN_NOTION or not ID_DA_PAGINA:
        print("ERRO: As variáveis de ambiente TOKEN_NOTION e ID_DA_PAGINA não foram configuradas.")
        sys.exit(1)

    # A chamada inicial começa com nível 0
    blocos_markdown = buscar_e_converter_blocos(ID_DA_PAGINA, nivel=0)
    
    print(f"Total de blocos de conteúdo processados (incluindo aninhados).")
    try:
        with open(NOME_ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
            f.write("\n\n".join(blocos_markdown))
        print(f"\nSUCESSO! Página exportada para o arquivo '{NOME_ARQUIVO_SAIDA}'")
    except IOError as e:
        print(f"ERRO ao salvar o arquivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
