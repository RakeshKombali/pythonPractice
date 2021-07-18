import requests
import json 

baseUrl = "https://reqres.in"
def parseResponse(response):
    print(response)
    print(json.dumps(response.json(),indent=4))

def getListUserswithoutParams():
    getListUsers = "/api/users?page=2"
    response = requests.get(baseUrl+getListUsers)
    parseResponse(response)

def getListUserswithParams():
    params = {'page':2}
    getListUsers = "/api/users"
    response = requests.get(baseUrl+getListUsers,params=params)
    #parseResponse(response)
    for key,value in (response.json()).items():
        if key == 'total_pages':
            print(value)
    firstName = [fName['first_name'] for fName in (response.json())['data']]
    print(firstName)


def postUsers():
    data = {
    "name": "Rakesh",
    "job": "member"
    }
    postUsers="/api/users"
    response = requests.post(baseUrl+postUsers,data=data)
    parseResponse(response)

def putUsers():
    putUsers = "/api/users/2"
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    response = requests.put(baseUrl+putUsers,data= data)
    parseResponse(response)


def deleteUsers():
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    deleteUsers = "/api/users/2"
    response = requests.delete(baseUrl+deleteUsers,data=data)
    print(response)

#     
#getListUserswithoutParams()
#getListUserswithParams()
#postUsers()
#putUsers()
#deleteUsers()

apikey = "a85dc8ebdd75ac45d90d4ca5da40f612"
url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid='+apikey
response = requests.get(url)
parseResponse(response)