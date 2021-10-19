from api.sendToServer import sendToServer

def deactivate():
  # deactivation logic

  #after this send inactive state to server
  sendToServer(0)