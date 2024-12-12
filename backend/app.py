from flask import Flask, jsonify, request
import logging
from gns3_api import GNS3API
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

# Set up logging to capture all actions
logging.basicConfig(filename='logs/gns3_actions.log', level=logging.INFO)

# Initialize GNS3 API client
gns3_api = GNS3API()

@app.route('/')
def index():
    return "Server is running!"

@app.route('/add_device', methods=['POST'])
def add_device():
    try:
        data = request.get_json()
        response = gns3_api.create_node(data)
        logging.info(f"Node added: {data['name']} with ID: {response['node_id']}")
        return jsonify({"message": "Node created successfully", "node_id": response['node_id']}), 200
    except Exception as e:
        logging.error(f"Error adding node: {str(e)}")
        return jsonify({"message": "Error adding node", "error": str(e)}), 500

@app.route('/remove_device', methods=['POST'])
def remove_device():
    try:
        data = request.get_json()
        node_id = data.get('node_id')
        response = gns3_api.remove_node(node_id)
        logging.info(f"Node removed: {node_id}")
        return jsonify({"message": f"Node {node_id} removed successfully"}), 200
    except Exception as e:
        logging.error(f"Error removing node: {str(e)}")
        return jsonify({"message": "Error removing node", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
