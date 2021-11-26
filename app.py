import os
from dotenv import load_dotenv
from api.listener import listener

# load dotenv
load_dotenv()

# Initialise listener
# Via the listener you can filter and react to the incoming states
listener()

print('Script running')

# Ensure script keeps running
input("Press enter to end script")