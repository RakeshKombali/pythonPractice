import requests
import json
baseUrl = "https://reqres.in"

def parserResponse(response):
    print(response)
    print(json.dumps(response.json(),indent=4))

def getListUserswithoutParams():
    getListUsers = "/api/users?page=2"
    response = requests.get(baseUrl+getListUsers)
    print('GET Operation without passing params')
    parserResponse(response)
   
def getListUserswithParams():
    #parametering the payload after the question mark in the URL.
    params = {
        'page':2
    }     
    getListUsers = "/api/users"
    response = requests.get(baseUrl+getListUsers, params=params)
    print('GET Operation while passing params')
    parserResponse(response)
    resp = response.json()
    for key, value in ((response.json()).items()):
        if key=='total_pages':
            print(value)
    first_name = [fName['first_name'] for fName in resp['data']]
    print(first_name)

def postUser():
    data = {
    "name": "Rakesh",
    "job": "member"
    }
    postUsers = "/api/users"
    response = requests.post(baseUrl+postUsers, data=data)
    print('POST operation')
    parserResponse(response)
 
def putUsers():
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    putUsers = "/api/users/2"
    response = requests.put(baseUrl+putUsers, data=data)
    print('PUT Operation')
    parserResponse(response)
 
def deleteUser():
    #usually you require an ID to identify which resource to delete
    #here inthis case '2' at the end is the id 
    deleteUsers = "/api/users/2"
    response = requests.delete(baseUrl+deleteUsers)
    print('DELETE Operation')
    print(response)


getListUserswithoutParams()
getListUserswithParams()
postUser()
putUsers()
deleteUser()