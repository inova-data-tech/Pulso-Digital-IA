from app.ml.ai import chat
from langchain.schema import HumanMessage, SystemMessage

def analisartexto(texto,busca):
    message = [
        SystemMessage(
            content="Me retorne um JSON com o nome do produto, seguido de uma lista de aspectos avaliados. Cada aspecto deve conter um nome que representa uma unica coisa do produto e uma nota de valor inteiro de -1 a 1, sem separação entre positivos e negativos e uma explicação em ingles."
        ),
        SystemMessage(content="""
        {
          "nome_do_produto": "",
          "aspectos": [
          {
              "nome": "",
              "nota": 0,
              "explicacao": ""
          }
          ]
        }
        """),
        HumanMessage(
            content=f"O produto é {busca}"
        ),
        HumanMessage(
            content=texto
        )
    ]
    response = chat(message)

    content = response.content

    return content
