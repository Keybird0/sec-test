import json


def handle(req):
    # custom handler func by zpg
    model_result = {"score": 1, "name": "test"}

    params = {"model_result": model_result}

    resp = {"Params": params}

    return json.dumps(resp)
