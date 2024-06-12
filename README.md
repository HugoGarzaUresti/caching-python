# Caching

This guide demonstrates how to use caching in Python using the `functools.lru_cache` decorator to cache results of expensive computations, and provides a simple web interface using Flask to interact with the cache.

## Requirements

- Python 3.x
- `Flask` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

3. Access the application:
    - Compute a value: `http://127.0.0.1:5000/compute/<value>`
    - Clear the cache: `http://127.0.0.1:5000/clear_cache`

## Code Explanation

### `app/__init__.py`

This module contains the Flask application and the cached function.

- **`expensive_computation`**: A function decorated with `lru_cache` to cache its results.
- **`compute`**: A Flask route that computes the value using `expensive_computation`.
- **`clear_cache`**: A Flask route that clears the cache.

### `run.py`

This script serves as the entry point for the application. It calls the `main` function to start the Flask server.

## Additional Information

- The `lru_cache` decorator caches the results of function calls, which can significantly speed up repeated calls with the same arguments.
- You can adjust the `maxsize` parameter of `lru_cache` to control the cache size.
- Use the `/clear_cache` endpoint to clear the cache.
