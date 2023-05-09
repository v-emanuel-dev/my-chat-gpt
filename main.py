import requests
import json
from config import API_KEY, API_URL

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

def ask_question(question):
    data = {
        'prompt': f'Responda à seguinte pergunta em português: {question}',
        'max_tokens': 500,
        'n': 1,
        'stop': None,
        'temperature': 0.5,
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

    response_data = response.json()
    return response_data['choices'][0]['text'].strip()

def main():
    while True:
        question = input("Faça uma pergunta para o ChatGPT (digite 'sair' para encerrar): ")
        if question.lower() == 'sair':
            break

        answer = ask_question(question)
        if answer:
            print(f'Resposta do ChatGPT: {answer}')
        else:
            print("Não foi possível obter uma resposta.")

if __name__ == '__main__':
    main()
