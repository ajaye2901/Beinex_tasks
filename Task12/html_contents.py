# 4.Create a program that attempts to connect to a website and prints the HTML content if successful. 
# Use a try-except-else block to handle the requests.exceptions.RequestException exception and 
# display an error message if the connection fails.

import requests

try:   
    data =requests.get("https://www.ajay.com")

except requests.exceptions.RequestException :
    print("Connection Request Failed")

else:
        content = data.text
        print(content)
