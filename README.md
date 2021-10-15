# 2244 - Python client

This is a python client for the WOT 2244 project.

## Instal dependencies:

```Bash
pip3 install oscpy
pip3 install python-dotenv
```

https://pypi.org/project/oscpy/

https://pypi.org/project/python-dotenv/

## TODO after install:

- Create .env file.

## Run client:

```Bash
python3 app.py
```

## Scripting

To send a state to server:

```
from api.send import send

send(<yourStateHere>)
```

Write your state logic under states/_yourStateName_
