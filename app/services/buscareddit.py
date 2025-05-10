import re
import praw
import pandas as pd
import datetime

reddit = praw.Reddit(
    client_id="fS5L5_Mn8HmkE-btm6RqIQ",
    client_secret="fW0ZXQSX6pcGdI2RMCHYbss0Sg8Dhw",
    user_agent="scraper",
    username="Hopeful_Visit_6895",
    password="Luc@s400."
)

def clean_text(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # Remove caracteres de controle ASCII

    return text

def buscarposts(busca):
    posts = []

    for post in reddit.subreddit("all").search(busca, limit=1):
        posts.append({
            "id": post.id,
            "title": post.title,
            "text": post.selftext,
            "score": post.score,
            "url": post.url,
            "post_date": datetime.datetime.fromtimestamp(post.created_utc),
            "num_comments": post.num_comments
        })

    # Criar um DataFrame e exibir os primeiros posts coletados
    df_posts = pd.DataFrame(posts)
    comments = []
    # Iterar sobre os posts coletados e buscar comentários
    for post_id in df_posts["id"]:
        submission = reddit.submission(id=post_id)
        submission.comments.replace_more(limit=1)
        for comment in submission.comments.list():
            post_date = datetime.datetime.fromtimestamp(comment.created_utc)
            # Função para remover caracteres ilegais
            comments.append({
                "post_id": post_id,
                "comment": comment.body,
                "score": comment.score,
                "date": post_date
            })
        df_comments = pd.DataFrame(comments)


    # Aplicar a limpeza nos comentários e posts
    df_posts["title"] = df_posts["title"].apply(clean_text)
    df_posts["text"] = df_posts["text"].apply(clean_text)

    df_comments["comment"] = df_comments["comment"].apply(clean_text)
    return df_posts, df_comments




