# -*- coding: utf-8 -*-
import requests
import sys
import os # Biblioteca para ler variáveis de ambiente

# ==============================================================================
# CONFIGURAÇÕES (LIDAS DO AMBIENTE DO GITHUB ACTIONS)
# ==============================================================================
# As credenciais agora são lidas dos "Secrets" do repositório
TOKEN_NOTION = os.environ.get("TOKEN_NOTION")
ID_DA_PAGINA = os.environ.get("ID_DA_PAGINA")

# Nome do arquivo que será gerado (pode ser configurado aqui)
NOME_ARQUIVO_SAIDA = "pagina_exportada.md"

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

def converter_bloco(bloco: dict) -> str:
    tipo_bloco = bloco["type"]
    conteudo = bloco.get(tipo_bloco, {})
    texto_convertido = ""
    if "rich_text" in conteudo and conteudo["rich_text"]:
        texto_convertido = converter_rich_text(conteudo["rich_text"])
    if tipo_bloco == "heading_1": return f"# {texto_convertido}"
    elif tipo_bloco == "heading_2": return f"## {texto_convertido}"
    elif tipo_bloco == "heading_3": return f"### {texto_convertido}"
    elif tipo_bloco == "paragraph": return texto_convertido if texto_convertido else ""
    elif tipo_bloco == "bulleted_list_item": return f"- {texto_convertido}"
    elif tipo_bloco == "numbered_list_item": return f"1. {texto_convertido}"
    elif tipo_bloco == "to_do":
        marcado = "x" if conteudo.get("checked") else " "
        return f"- [{marcado}] {texto_convertido}"
    elif tipo_bloco == "quote": return f"> {texto_convertido}"
    elif tipo_bloco == "divider": return "---"
    elif tipo_bloco == "code":
        linguagem = conteudo.get("language", "plaintext")
        return f"```{linguagem}\n{texto_convertido}\n```"
    else: return f"<!-- Bloco do tipo '{tipo_bloco}' não suportado -->"

def main():
    print("Iniciando a exportação da página do Notion...")
    if not TOKEN_NOTION or not ID_DA_PAGINA:
        print("ERRO: As variáveis de ambiente TOKEN_NOTION e ID_DA_PAGINA não foram configuradas.")
        sys.exit(1)
    headers = {
        "Authorization": f"Bearer {TOKEN_NOTION}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    url = f"https://api.notion.com/v1/blocks/{ID_DA_PAGINA}/children"
    parametros = {"page_size": 100}
    blocos_markdown = []
    tem_mais_paginas = True
    while tem_mais_paginas:
        try:
            resposta = requests.get(url, headers=headers, params=parametros)
            resposta.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"ERRO DE CONEXÃO: {e}")
            sys.exit(1)
        dados = resposta.json()
        for bloco in dados.get("results", []):
            blocos_markdown.append(converter_bloco(bloco))
        if dados.get("has_more"):
            parametros["start_cursor"] = dados.get("next_cursor")
        else:
            tem_mais_paginas = False
    print(f"Total de {len(blocos_markdown)} blocos de conteúdo encontrados.")
    try:
        with open(NOME_ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
            f.write("\n\n".join(blocos_markdown))
        print(f"\nSUCESSO! Página exportada para o arquivo '{NOME_ARQUIVO_SAIDA}'")
    except IOError as e:
        print(f"ERRO ao salvar o arquivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

