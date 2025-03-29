from app.ml.ai import tokenizer, model
import pandas as pd
import json
import torch

analise_comments= pd.read_csv("analise_comments.csv")
analise_posts= pd.read_csv("analise_posts.csv")
jsons = analise_comments.loc[1,"analise"]
dict = json.loads(jsons)




# Função para gerar embeddings
def gerar_embedding(texto):
    inputs = tokenizer(texto, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Pegamos a última camada oculta (último hidden state da primeira posição, "pooling")
    embedding = outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
    return embedding

# Teste com um texto
texto_teste = "A câmera do celular é excelente!"
embedding = gerar_embedding(texto_teste)

print("Embedding gerado:", embedding[:5])  # Mostrando apenas os primeiros valores
