from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener la API Key desde el .env
api_key = os.getenv("OPENAI_API_KEY")

# Crear cliente con la API Key
client = OpenAI(api_key=api_key)

print("Chat Gpt \n")

while True:
    texto = input("Human: ")
    if texto.lower() in ["salir", "exit", "quit"]:
        print("👋 Adiós!")
        break

    response = client.responses.create(
        model="gpt-5-nano",
        reasoning={"effort": "low"},
        instructions="habla preciso no mas de 5 palabras y en español",
        input=texto,
    )

    print(f"Robot: {response.output_text}")
