from flask import Flask, request, jsonify, send_file
from  flask_cors import CORS, cross_origin
import os
import json
from URLfilter import filtered_urls
from scraper import *
from jsonConvert import *
from urlFind import *
from jsonCombiners import *
import schedule
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])

def serve():
    return jsonify({'response': 'this is my app'})


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'no selected file'})
    if file:
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return jsonify({'message': 'file uploaded successfully', 'filename': filename}), 200
    

@app.route('/data', methods=['GET'])
def get_data():
    
    with open(os.path.join(os.getcwd(), 'combined.json'), 'r') as file:
        data = json.load(file)

    return jsonify(data)

@app.route('/imgs/<filename>', methods=['GET'])
def get_image(filename):
    return send_file(os.path.join('./imgs/', filename), mimetype='image/jpeg')
    

def main():
    # nature_all = nature_links()
    yale_all = yale_links()
    snex_all = snex_links()
    
   
    snex_converter(snex_scraper(filtered_urls(snex_all))) 
    yale_converter(yale_scraper(filtered_urls(yale_all))) 
    #nature_converter(nature_scraper(filtered_urls(nature_all)))
    combiner()

if __name__ == '__main__':
    app.run()

    
