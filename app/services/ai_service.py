from app.ml.ai import chat
from langchain.schema import HumanMessage, SystemMessage

def analisartexto(texto,busca):
    message = [
        SystemMessage(
            content=f"Give me a JSON with the name of the product, followed by a list of aspects about {busca} evaluated in the text provided.Each aspect must represent a distinct and concrete feature of the product itself (such as battery life, screen quality, or 5G performance) and an integer score from -1 to 1, with no separation between positive and negative, and an explanation in English, based on the text."
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

teste = analisartexto("Eu gosto muito do S25 ultra, a tela é ótima e a bateria dura muito tempo", "S25 ultra")

print(teste)