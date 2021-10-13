# State 0 = reset
# State 1 = active
# State 2 - 99 = extra states if neccesary
# State 100 = solved

import os
from dotenv import load_dotenv
from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

# load dotenv
load_dotenv()

# Initialise this client's osc server
client = OSCThreadServer()
sock = client.listen(address=os.getenv('LOCAL_ADDRESS'), port=int(os.getenv('LOCAL_PORT')), default=True)

# Define server
server = OSCClient(os.getenv('SERVER_ADDRESS'), int(os.getenv('SERVER_PORT')))

# Create send function
# Use this function every time your state updates -> send(statenumber)
def send(state):
  # Automatically add the client-id and convert it back to bytes format
  server.send_message(bytes("/client-{}".format(os.getenv('CLIENT_ID')), encoding='utf8'), [state])


# Listen for a server message and detect which state is given.
@client.address(b'/servermessage')
def detectState(*values):
  if values[0] == 0:
    print('Going into inactive state')
    # Inactive state logic

  elif values[0] == 1:
    print('Going into active state')
    # Active state logic

  elif values[0] == 100:
    print('Puzzle force solved by server')
    # Active state logic

print('Script running')

# Send mesage to server at startup
send(999)

# Ensure script keeps running
while True:
  pass