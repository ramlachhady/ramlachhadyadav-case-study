import requests

def query_phi3(prompt: str) -> str:
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'phi3',
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()['response'].strip()
