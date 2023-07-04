from spin_http import Request, Response, http_send


def handle_request(request: Request) -> Response:

    response = http_send(
        Request("GET", "https://demo-xtzjs1xt.fermyon.app/simple", {}, None)
    )

    return Response(
        200,
        {"content-type": "text/plain"},
        response.body,
    )
