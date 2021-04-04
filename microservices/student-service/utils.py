import json
import httpx


from config import Config

configuration = Config()


def register_to_consul():
    consul_host = configuration.CONSUL_HOST
    consul_port = configuration.CONSUL_PORT
    url = f"http://{consul_host}:{consul_port}/v1/agent/service/register"
    data = {
        "Name": "student",
        "Tags": ['student'],
        'Address': configuration.address,
        'Port': configuration.port,
        "Check": {
            "http": f"http://{configuration.address}:{configuration.port}/health",
            'interval': '10s'
        },
        "connect": {
            "sidecar_service": {}
        }
    }
    print('Service registration parameters: ', data)
    res = {"message": "registering"}
    res = httpx.put(url, data=json.dumps(data))
    return res.text

