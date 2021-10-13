from oscpy.server import OSCThreadServer
from time import sleep

osc = OSCThreadServer()
sock = osc.listen(address='192.168.1.31', port=57112, default=True)


@osc.address(b'/servermessage')
def callback(*values):
    print("got values: {}".format(values))

while True:
  pass