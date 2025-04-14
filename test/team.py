import http.client
import ssl

# Create a custom SSL context that doesn't verify certificates
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

conn = http.client.HTTPSConnection("v3.football.api-sports.io", context=context)

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "a8e4d2b94d9ebbdbd2530a1ed4e4969e"
    }

conn.request("GET", "/teams?id=33", headers=headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
