import time
from functools import lru_cache
from flask import Flask, jsonify

app = Flask(__name__)

@lru_cache(maxsize=32)
def expensive_computation(x):
    time.sleep(2)  # Simulate a time-consuming computation
    return x * x

@app.route('/compute/<int:x>')
def compute(x):
    result = expensive_computation(x)
    return jsonify({'input': x, 'result': result})

@app.route('/clear_cache')
def clear_cache():
    expensive_computation.cache_clear()
    return "Cache cleared!"

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
