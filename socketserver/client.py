import json
import socket


def printDict(data: dict, prefix: str = ''):
    # copiado de ../utils
    for k, v in data.items():
        if type(v) == dict:
            print(f"{prefix}{k}")
            printDict(v, f"{prefix}\t")
        else:
            print(f"{prefix}{k}\t{v}")


HOST, PORT = "localhost", 55555
data = dict(
    type="property",
    data=dict(
        xpto=dict(
            name="Plaza",
            city="Niteroi",
            country="Brazil",
            full_address="Elm Street 14"
        )
    )
)

message = json.dumps(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(message + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

# print(f"Sent:     {data}")
resp = json.loads(received)
print("Received:")
printDict(resp)
