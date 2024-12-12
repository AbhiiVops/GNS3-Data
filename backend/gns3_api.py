import requests
import json

class GNS3API:
    def __init__(self):
        self.gns3_url = "http://localhost:3080/v2"
        self.project_id = "f86dd854-7aef-470f-97cd-0ab87207ddd4"  # Update with your project ID

    def create_node(self, data):
        url = f"{self.gns3_url}/projects/{self.project_id}/nodes"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create node: {response.text}")
    
    def remove_node(self, node_id):
        url = f"{self.gns3_url}/projects/{self.project_id}/nodes/{node_id}"
        response = requests.delete(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to remove node: {response.text}")
