import requests

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload=
{
    "aaaUser":
        {"attributes":
            {
                "name":"admin",
                "pwd":"ciscopsdt"
            }
        }
}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
