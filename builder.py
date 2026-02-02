import requests

class OpenAI_API:
    def __init__(self, api_key, api_base_url):
        self.api_key = api_key
        self.api_base_url = api_base_url

    def generate_code(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        data = {
            'prompt': prompt,
            'max_tokens': 150,
            'temperature': 0.7,
        }

        response = requests.post(f'{self.api_base_url}/v1/engines/davinci-codex/completions',
                                  headers=headers,
                                  json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['choices'][0]['text']

# Example usage:
# api = OpenAI_API(api_key='YOUR_API_KEY', api_base_url='YOUR_API_BASE_URL')
# code = api.generate_code('Create a sorting algorithm in Python')
# print(code)