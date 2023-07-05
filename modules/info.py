from spin_http import Request, Response

from json import dumps

import os
import sys
import platform


def handle_request(request: Request) -> Response:
    info: dict = {
        "os.pid": os.getpid(),
        # "os.uid": os.getuid(),
        # "os.login": os.getlogin(),
        "os.environ": tuple(os.environ),
        "sys.platform": sys.platform,
        "sys.version": sys.version,
        "platform.node": platform.node(),
        "platform.system": platform.system(),
        "platform.release": platform.release(),
        # "sys.modules": tuple(sys.modules),
        # "sys.thread_info": sys.thread_info,
    }
    return Response(
        200, {"content-type": "application/json"}, bytes(dumps(info), "utf-8")
    )
