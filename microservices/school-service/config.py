import socket
import os


class Config:
    port = os.getenv('PORT', 8000)
    address = os.getenv('ADDRESS') or 'school_service'


