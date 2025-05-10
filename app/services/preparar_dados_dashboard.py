import pandas as pd
import json
import numpy as np
from app.services.buscareddit import buscarposts
from app.services.analisecompleta import analise_completa

busca = "S25 ultra"
df_post, df_comments = buscarposts(busca)
analise_completa(df_post, df_comments, busca)

# busca="S25 ultra"
# df_posts, df_comments = buscarposts(busca)
# analise_completa(df_posts, df_comments, busca)
# df_comments = pd.read_csv("analise_comments.csv")

df_comments_apenas_analise = df_comments.loc[df_comments.analise.notnull(), :]
df_comments_apenas_analise.reset_index(drop=True, inplace=True)

df_comments_score_2 = df_comments_apenas_analise.loc[df_comments_apenas_analise.loc[:,"score"] > 1, :]
df_comments_score_2.reset_index(drop=True, inplace=True)

df_analise = df_comments_score_2.loc[:,["analise","date"]]

def json_loads(x):
    try:
        return json.loads(x)
    except json.JSONDecodeError:
        return None

df_analise["analise"] = df_analise.loc[:,"analise"].apply(json_loads)
df_analise = df_analise.loc[df_analise.analise.notnull(), :]



df_aspects = pd.DataFrame(columns = [pd.DataFrame(df_analise["analise"].iloc[0]["aspects"]).columns])
df_aspects.columns = [col[0] if isinstance(col, tuple) else col for col in df_aspects.columns]

for i in range(0,len(df_analise["analise"])):
    df_aspects_add = pd.DataFrame(df_analise["analise"].iloc[i]["aspects"])
    df_aspects = pd.concat([df_aspects, df_aspects_add], ignore_index=True)

df_aspects = df_aspects.replace("", np.nan)
df_aspects = df_aspects.dropna()
# print(df_aspects.sort_values(by=["name"], ascending=False))



from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
aspectos = df_aspects["name"].tolist()
# Gera os vetores de embeddings
embeddings = model.encode(aspectos)

# Aplica o agrupamento hierárquico
clustering = AgglomerativeClustering(n_clusters=75, distance_threshold=None)
labels = clustering.fit_predict(embeddings)

# Monta o DataFrame com os grupos
df_resultado = pd.DataFrame({'Aspecto': aspectos, 'Grupo': labels})
df_resultado.sort_values(by='Grupo', inplace=True)

# Exibe o resultado
print(df_resultado.head(20))