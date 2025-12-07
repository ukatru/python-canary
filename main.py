#!/usr/bin/env python3
"""
Simple Python web application for kpack build demonstration.
"""
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        'message': 'Hello from kpack-built Python app!',
        'version': '1.0.0',
        'environment': os.getenv('ENV', 'development')
    }

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
