from transformers import AutoModel, AutoTokenizer
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model_name = os.getenv("MODEL")
temperature = os.getenv("TEMPERATURE")

# Configuração do modelo
chat = ChatOpenAI(
    base_url = base_url,
    api_key = api_key,
    model = model_name,
    temperature=temperature
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, device_map="auto")