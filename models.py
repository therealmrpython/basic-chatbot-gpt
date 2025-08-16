from openai import OpenAI
import os
from dotenv import load_dotenv
# load variables from file .env
load_dotenv()

# Get API Key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Create client with the API Key
client = OpenAI(api_key=api_key)

# Listar modelos
models = client.models.list()

for model in models.data:
    print(model.id)
