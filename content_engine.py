import requests

class ContentEngine:
    def __init__(self, api_key, custom_url=None):
        self.api_key = api_key
        self.custom_url = custom_url or 'https://api.openai.com/v1/engines/davinci-codex/completions'

    def generate_blog_content(self, topic, length='medium'):
        prompt = f'Generate a {length} blog post about {topic}.'
        response = requests.post(
            self.custom_url,
            headers={
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'prompt': prompt,
                'max_tokens': 500
            }
        )

        if response.status_code == 200:
            return response.json()['choices'][0]['text']
        else:
            return f'Error: {response.status_code} {response.text}'