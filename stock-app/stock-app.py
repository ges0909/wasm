from spin_http import Request, Response

from json import dumps

def handle_request(request: Request) -> Response:
    # print("'handle_request' called")
    stock = [
    {
        "name": "Laptop",
        "price": 559.0,
        "quantity": 20
    },
    {
        "name": "Bouncy Ball",
        "price": 2.49,
        "quantity": 198
    },
    {
        "name": "Toilet",
        "price": 99.0,
        "quantity": 74
    },
    {
        "name": "The Notebook DVD",
        "price": 19.99,
        "quantity": 12
    },
    {
        "name": "Corn",
        "price": 1.49,
        "quantity": 856
    }
    ]
    return Response(
        200,
        {"content-type": "application/json"},
        bytes(dumps(stock), "utf-8"))
