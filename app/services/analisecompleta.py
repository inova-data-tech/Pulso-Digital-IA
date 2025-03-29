from concurrent.futures import ThreadPoolExecutor, as_completed
from ai_service import *
from string_proces import *
from buscareddit import buscarposts

def analise_post(df_posts, busca, i):
    title = df_posts.iloc[i, 1]
    text = df_posts.iloc[i, 2]
    analise = analisartexto(title + text, busca)
    analise = string_proces(analise)
    df_posts.loc[i, "analise"] = analise

def analise_comment(df_comments, busca, i):
    comment = df_comments.iloc[i, 1]
    analise = analisartexto(comment, busca)
    analise = string_proces(analise)
    df_comments.loc[i, "analise"] = analise

def analise_posts(df_posts, busca):
    with ThreadPoolExecutor(max_workers=20) as executor:  # Ajuste o número de threads conforme necessário
        futures = {executor.submit(analise_post, df_posts, busca, i): i for i in range(len(df_posts))}
        for future in as_completed(futures):
            future.result()  # Garante que exceções sejam levantadas

def analise_comments(df_comments, busca):
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(analise_comment, df_comments, busca, i): i for i in range(len(df_comments))}
        for future in as_completed(futures):
            future.result()

def analise_completa(df_posts, df_comments, busca):
    analise_posts(df_posts, busca)
    analise_comments(df_comments, busca)

    df_posts.to_csv("analise_posts.csv", index=False)
    df_comments.to_csv("analise_comments.csv", index=False)

busca="iphone"
df_posts, df_comments = buscarposts(busca)
analise_completa(df_posts, df_comments, busca)