"""
health check test for hamster
"""

import sys, os
import requests


with open('url') as file:
    url = file.read()
    file.close()

print(url)

result = requests.get(f'http://{url}/health').json()

print(result)

if result['ok']:
    sys.exit(0)
else:
    sys.exit(1)
