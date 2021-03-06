import os
from settings import osc

# Use this function every time your state updates -> send(statenumber)
def sendToServer(state):
  clientAddress = bytes("/Client-{}".format(os.getenv('CLIENT_ID')), encoding='utf8')
  serverIp = os.getenv('SERVER_IP')
  serverPort = int(os.getenv('SERVER_PORT'))

  osc.send_message(clientAddress, [state], serverIp, serverPort)
