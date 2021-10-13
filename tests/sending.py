from oscpy.client import OSCClient

address = "192.168.1.31"
port = 57111

osc = OSCClient(address, port)

osc.send_message(b'/client-01', [1])