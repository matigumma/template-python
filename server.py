import os
from flask import Flask, send_from_directory, render_template, redirect, request, jsonify
from flask_cors import CORS, cross_origin
import stream_chat
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

port = int(os.environ.get("PORT", 5000))

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/<path:path>')
def all_routes(path):
    return redirect('/')

@app.route('/apiv1/getstream/token', methods=['GET'])
@cross_origin()
def get_stream_token():
    try:
        data = request.get_json()

        if 'user_id' not in data or not data['user_id']:
            return {"error": "Missing user_id"}

        server_client = stream_chat.StreamChat(os.environ.get("app_id"), os.environ.get("stream_secret"))
        token = server_client.create_token(data['user_id'])

        return {"token": token}
    except Exception:
        return None;

@app.route('/apiv1/api/me', methods=['GET'])
@cross_origin()
def get_user():
    try: 
        return {
            "id": "Matias_7c7edd68-9a31-45e5-904f-4f9d84d0bf0b",
            "name": "Matias",
            "created_at": "",
            "updated_at": ""
        }
    except Exception:
        return None;


if __name__ == "__main__":
    app.run(port=port)