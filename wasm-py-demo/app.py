from spin_http import Request, Response

from json import dumps

def handle_request(request: Request) -> Response:
    name = "Gerrit"
    return Response(200,
                    {"content-type": "application/json"},
                    bytes(dumps({"message": f"Hello from the Python SDK, {name}!"}), "utf-8"))
