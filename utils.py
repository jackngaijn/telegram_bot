import requests
import config as cfg


def chat_request(prompt):
    headers = {
        "Authorization": f"Bearer {cfg.API_KEY}",
        "Content-Type": "application/json"
    }

    template = ("Answer as concisely as possible, make sure your answer does not exceed 4000 characters, "
            "and respond in the language in which the question is asked. The question is below:")

    data = {
        "model": cfg.MODEL,
        "messages": [
            {"role": "system", "content": template},  # Инструкции для модели
            {"role": "user", "content": prompt}  # Запрос от пользователя
        ],
        "stream": False  # off stream
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            response_json = response.json()
            if "choices" in response_json:
                return response_json["choices"][0]["message"]["content"]
            else:
                print("Response hasn't 'choices' field.")
        else:
            print(f"API Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Request Error: {e}")

    return ""
