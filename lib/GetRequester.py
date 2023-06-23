import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url
    
    def get_response_body(self):
        response = requests.get(self.url)
        return response.text
    
    def load_json(self):
        response_body = self.get_response_body()
        parsed_data = None
        
        while not parsed_data:
            try:
                parsed_data = json.loads(response_body)
                if not isinstance(parsed_data, (list, dict)):
                    print("The response body is not a valid JSON.")
            except json.JSONDecodeError:
                pass
        
        return parsed_data

url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
requester = GetRequester(url)
data = requester.load_json()
print(data)

