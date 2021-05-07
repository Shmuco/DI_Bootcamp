import requests
import time
website = input('Enter a website: ')
start = time.time()
res = requests.get(website)
print (f'{time.time() - start} Seconds')

dir(res)