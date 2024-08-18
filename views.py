from flask import Flask, request, jsonify 
from import_data import get_data, parse_data
from description_processing import parse_polish_description

app = Flask(__name__)

@app.route('/boardgames/similarity/',methods=['POST'])
def get_query():
    data = request.get_json()
    description = data.get("description")
    event_id = data.get("event_id") 
    boardagames=parse_data(get_data(event_id))
    print(parse_polish_description(description))


    #similarity model here
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)