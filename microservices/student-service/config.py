import socket
import os


class Config:
    port = os.getenv('PORT', 8000)
    address = os.getenv('ADDRESS') or 'student_service'
    CONSUL_HOST = os.getenv('CONSUL_HOST') or 'consul'
    CONSUL_PORT = os.getenv('CONSUL_PORT') or 8500



