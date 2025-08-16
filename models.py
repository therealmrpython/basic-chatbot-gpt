from openai import OpenAI

client = OpenAI(api_key="***REMOVED***")


# Listar modelos
models = client.models.list()

for model in models.data:
    print(model.id)
