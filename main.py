import openai
import os
from dotenv import load_dotenv
import time

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verificar se a chave foi carregada
print("Chave da API:", openai.api_key)

try:
    # Criar uma conclusão de chat com um modelo válido
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # ou o modelo que você tem acesso
        messages=[{"role": "user", "content": "Hello world"}]
    )

    # Exibir a resposta
    print(response.choices[0].message['content'])

except openai.error.RateLimitError as e:
    print(f"Erro de limite de taxa: {e}")
    # Pode adicionar um atraso ou lógica de reintento aqui, se necessário
except openai.error.InvalidRequestError as e:
    print(f"Erro de solicitação inválida: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
