from flask import Flask, request, send_file
from google.cloud import storage
import os

app = Flask(__name__)
storage_client = storage.Client()
bucket_name = 'Orders'
bucket = storage_client.bucket(bucket_name)

@app.get('/orders')
def get_orders():
    return []

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)