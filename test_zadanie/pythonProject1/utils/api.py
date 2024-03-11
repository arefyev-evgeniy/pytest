import requests
import json
import unittest
class Test_place():

    def metod_get(self, page_number):

        url = "https://reqres.in/api/users?page=2"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    def metod_post(self):
        url = "https://reqres.in/api/register"

        payload = json.dumps({
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response


    def metod_put(self):

        url = "https://reqres.in/api/users/2"

        payload = json.dumps({
            "name": "morpheus",
            "job": "leaderw"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        return response

    def metod_delete(self):

        url = "https://reqres.in/api/users/4"

        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        return response




