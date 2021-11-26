import os
from settings import osc
from api.sendToServer import sendToServer
from states.activate import activate
from states.solved import solved
from states.deactivate import deactivate

# Listen for a server message and detect which state is given.
def listener():

  # Initialise this client's listening osc server
  sock = osc.listen(address=os.getenv('LOCAL_IP'), port=int(os.getenv('LOCAL_PORT')), default=True)

  # this filter activates only when recieving a '/servermessage'
  @osc.address(b'/servermessage')
  def detectState(*values):
    if values[0] == 0:
      print('Going into inactive state')
      deactivate()

    elif values[0] == 1:
      print('Going into active state')
      activate()

    elif values[0] == 100:
      print('Puzzle force solved by server')
      solved()
      
    elif values[0] == 999:
      print('send live state to server')
      sendToServer(999)
      
    else:
      print("got wrong state")
      
    # Add your own states here