import requests
import json

baseUrl = 'https://reqres.in'

def parseResponse(response):
    print(response)
    print(json.dumps(response.json(),indent=4))

def getListUsers():
    getListUsers = '/api/users?page=2'
    response = requests.get(baseUrl+getListUsers)
    print('get list users with out params')
    parseResponse(response)

def getListUserswithParameter():
    payload ={'page':2}
    getListUsers = '/api/users'
    response = requests.get(baseUrl+getListUsers, data = payload)
    print('get list users with params')
    #parseResponse(response)
    for key,value in (response.json()).items():
        if key == 'total_pages':
            print(value)
    firstName = [print(fName['first_name']) for fName in (response.json())['data']]
    print(firstName)

def postUser():
    data = {
    "name": "Rakesh",
    "job": "member"
    }
    postUsers = "/api/users"
    response = requests.post(baseUrl+postUsers,data=data)
    parseResponse(response)


def putUser():
    data = {
    "name": "morpheus",
    "job": "zion resident"
    }
    putUsers = "/api/users/2"
    response = requests.post(baseUrl+putUsers,data=data)
    parseResponse(response)

def deleteUser():
    deleteUsers = "/api/users/2"
    response = requests.delete(baseUrl+deleteUsers)
    print(response)


getListUsers()
getListUserswithParameter()
postUser()
putUser()
deleteUser()