import unittest
from faker import Faker
from app import app


class TestAPI(unittest.TestCase): #Inheriting testcase functionality from unitttest

    def setUp(self):    #Constructor for our test case
        self.app = app.test_client()    #the app used in testing is the app that we imported

    
    # Need to be able to recieve two nums and return the sum of those nums

    def test_sum(self):
        payload = {'num1': 3, 'num2': 5}
        response = self.app.post('/sum', json=payload) #sending a post request to our app's '/sum' endpoint, and awaiting a response
        data = response.json
        self.assertEqual(data['result'], 8)

    def test_random_sum(self): #Mocking a payload (random data)
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.json
        self.assertEqual(data['result'], num1+num2)

if __name__ == '__main__':
    unittest.main()