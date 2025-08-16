from openai import OpenAI
import os
from dotenv import load_dotenv

# load variables from file .env
load_dotenv()

# Get API Key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Create client with the API Key
client = OpenAI(api_key=api_key)

print("Chat Gpt")

while True:
    texto = input("Human: ")
    if texto.lower() in ["salir", "exit", "quit"]:
        print("👋 Adiós!")
        break

    response = client.responses.create(
        model="gpt-5-nano",
        reasoning={"effort": "low"},
        instructions="habla preciso no mas de 5 palabras y en español si te habla español , ingles si te habla en ingles",
        input=texto,
    )

    print(f"Robot: {response.output_text}")
