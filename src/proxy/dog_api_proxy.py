import os
import urllib.request
import json

class DogApiProxy:
    def __init__(self):
        self.base_url = os.getenv("DOG_API_BASE_URL", "https://dogapi.dog/api/v2")

    def fetch(self, endpoint):
        try:
            with urllib.request.urlopen(f"{self.base_url}{endpoint}") as response:
                data = response.read().decode()
                return json.loads(data)
        except Exception as e:
            return {"error": str(e)}
