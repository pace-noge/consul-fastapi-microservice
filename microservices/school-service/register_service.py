from time import sleep
from config import Config
import consul


configuration = Config()

def register():
    check_http = consul.Check.http(
        f'http://school_service:8000/health', interval='10s'
    )
    client = consul.Consul(
        host=configuration.CONSUL_HOST, port=configuration.CONSUL_PORT
    )

    while True:
        try:
            client.agent.service.register(
                'school', address='school', port=8000, check=check_http
            )
            break
        except consul.ConsulException:
            print("Retrying to connect to consul ...")
            sleep(0.5)

