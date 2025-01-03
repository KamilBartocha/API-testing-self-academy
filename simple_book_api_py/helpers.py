import requests
import uuid

BASE_URL = "https://simple-books-api.glitch.me"
API_TOKEN = None

def get_api_token():
    global API_TOKEN
    if API_TOKEN is None:
        url = f"{BASE_URL}/api-clients/"
        unique_id = uuid.uuid4().hex
        payload = {
            "clientName": f"api_client-{unique_id}",
            "clientEmail": f"api_client-{unique_id}@example.com"
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        API_TOKEN = response.json()['accessToken']
    return API_TOKEN

def get_status():
    return requests.get(f"{BASE_URL}/status")

def list_books():
    return requests.get(f"{BASE_URL}/books")

def list_books_with_params(type=None, limit=None):
    params = {}
    if type:
        params["type"] = type
    if limit:
        params["limit"] = limit
    return requests.get(f"{BASE_URL}/books", params=params)

def get_single_book(book_id):
    return requests.get(f"{BASE_URL}/books/{book_id}")

def create_order(token, book_id, customer_name):
    url = f"{BASE_URL}/orders"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "bookId": book_id,
        "customerName": customer_name
    }
    return requests.post(url, json=payload, headers=headers)

def get_all_orders(token):
    url = f"{BASE_URL}/orders"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return requests.get(url, headers=headers)

def get_single_order(token, order_id):
    url = f"{BASE_URL}/orders/{order_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return requests.get(url, headers=headers)

def update_order(token, order_id, customer_name):
    url = f"{BASE_URL}/orders/{order_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "customerName": customer_name
    }
    return requests.patch(url, json=payload, headers=headers)

def delete_order(token, order_id):
    url = f"{BASE_URL}/orders/{order_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return requests.delete(url, headers=headers)
