from spin_http import Request, Response

from json import dumps, loads
from os import environ


#
# The 'handle_request' function is the entry point to the Spin component.
# The component returns a 'spin_http.Response'.
# The source code for a Python HTTP component is compiled into a `.wasm`
# module by the `py2wasm` plugin.
#
def handle_request(request: Request) -> Response:
    url = environ["URL"]
    print(f">> environ['URL'] = {url}\n")

    headers = dict(request.headers)
    print(f">> headers = {headers}\n")

    if request.body:
        body = loads(request.body)
        print(f">> body = {body}\n")

    stock = [
        {"name": "Laptop", "price": 559.0, "quantity": 20},
        {"name": "Bouncy Ball", "price": 2.49, "quantity": 198},
        {"name": "Toilet", "price": 99.0, "quantity": 74},
        {"name": "The Notebook DVD", "price": 19.99, "quantity": 12},
        {"name": "Corn", "price": 1.49, "quantity": 856},
    ]
    return Response(
        200, {"content-type": "application/json"}, bytes(dumps(stock), "utf-8")
    )
