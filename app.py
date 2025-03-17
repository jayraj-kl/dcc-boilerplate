from flask import Flask
import socket

app = Flask(__name__)

def get_vm_ip():
    """Gets the VM's IP address."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Could not determine IP address."

@app.route('/')
def hello_world():
    vm_ip = get_vm_ip()
    return f"Hello, World! My IP address is: {vm_ip}"

if __name__ == '__main__':
    app.run(debug=True)