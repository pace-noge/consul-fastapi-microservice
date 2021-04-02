import json
import httpx


from config import Config

configuration = Config()


def register_to_consul():
    url = "http://consul:8500/v1/agent/service/register"
    data = {
        "Name": "StudentService",
        "Tags": ['student'],
        'Address': configuration.address,
        'Port': configuration.port,
        "Check": {
            'http': f'http://{configuration.address}:{configuration.port}/health',
            'interval': '10s'
        }
    }
    print('Service registration parameters: ', data)
    res = {"message": "registering"}
    res = httpx.put(url, data=json.dumps(data))
    return res.text

