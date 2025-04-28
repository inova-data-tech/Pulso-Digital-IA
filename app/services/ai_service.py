from app.ml.ai import chat
from langchain.schema import HumanMessage, SystemMessage

def analisartexto(texto,busca):
    message = [
        SystemMessage(
            content=f"Give me a JSON with the name of the product, followed by a list of aspects about {busca} evaluated in the text provided. Each aspect should contain a name that represents a single thing about the product and an integer score from -1 to 1, with no separation between positive and negative, and an explanation in English, based on the text."
        ),
        SystemMessage(content="""
        {
          "product_name": "",
          "aspects": [
          {
              "name": "",
              "score": 0,
              "explanation": ""
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
