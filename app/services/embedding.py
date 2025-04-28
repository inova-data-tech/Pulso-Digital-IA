from sentence_transformers import SentenceTransformer
import pandas as pd
import spacy

import json

analise_comments= pd.read_csv("analise_comments.csv")
analise_posts= pd.read_csv("analise_posts.csv")
print(analise_posts.loc[0,"analise"])



#
# # Carregar o modelo de embeddings
# model = SentenceTransformer("all-MiniLM-L6-v2")
# nlp = spacy.load("en_core_web_lg")
#
#
#
# # Função para gerar embeddings para cada comentário
# def gerar_embeddings(comentario):
#     # Dividir o comentário em sentenças (pode usar spaCy ou outra abordagem)
#     doc = nlp(comentario)
#     sentencas = [sent.text.strip() for sent in doc.sents]
#     # Gerar embeddings para cada sentença
#     embeddings = model.encode(sentencas)
#     return embeddings
#
#
# analise_comments['embedding'] = None
# for i,line in analise_comments.iterrows():
#     try:
#         product_json = analise_comments.loc[i,"analise"]
#         product_dict = json.loads(product_json)
#         aspects = product_dict['aspects']
#         embedding_list = []
#         for aspect in aspects:
#             explanation = aspect['explanation']
#             embedding = gerar_embeddings(explanation)
#             embedding_list.append(embedding)
#         analise_comments.loc[i,"embedding"] = embedding_list
#         print(analise_comments.loc[i,"analise"])
#     except Exception as e:
#         ...
#
# print(analise_comments)

