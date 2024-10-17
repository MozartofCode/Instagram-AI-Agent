# @Author: Bertan Berker
# @Language: Python
#
#

from flask import Flask, request, jsonify, render_template
from main import create
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/process-prompt', methods=['POST'])
def process_data():
    data = request.json
    
    prompt = data.get('prompt', 'Unknown')
    
    create(prompt)

    # Return a JSON response
    return jsonify({"message": "Finished posting on X!"})


if __name__ == '__main__':
    app.run(debug=True)
