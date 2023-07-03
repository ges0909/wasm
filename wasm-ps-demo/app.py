from spin_http import Response

import json

# def handle_request(request):
#     return Response(200,
#                     {"content-type": "text/plain"},
#                     bytes(f"Hello from the Python SDK", "utf-8"))

def handle_request(request):
    content = ['A', 'B', 'C']
    return Response(
        200, 
        {"content-type", "application/json"},
        json.dumps(f"{content}")
        )
