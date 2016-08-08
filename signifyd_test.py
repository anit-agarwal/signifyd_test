import unittest
import requests
import json
import random
from selenium import webdriver
from time import sleep

class SignifydTest(unittest.TestCase):
    caseId = 0
    dataId = 0
    dataSize = 2

    dataBank = [{
  "purchase": {
    "browserIpAddress": "192.168.1.1",
    "orderId": "4fj58as",
    "createdAt": "2016-07-11T17:54:31-05:00",
    "paymentGateway": "stripe",
    "paymentMethod": "credit_card",
    "transactionId": "1a2sf3f44f21s1",
    "currency": "USD",
    "avsResponseCode": "Y",
    "cvvResponseCode": "M",
    "orderChannel": "PHONE",
    "receivedBy": "John Doe",
    "totalPrice": 74.99,
    "products": [
      {
        "itemId": "1",
        "itemName": "Sparkly sandals",
        "itemUrl": "http://mydomain.com/sparkly-sandals",
        "itemImage": "http://mydomain.com/images/sparkly-sandals.jpeg",
        "itemQuantity": 1,
        "itemPrice": 49.99,
        "itemWeight": 5
      },
      {
        "itemId": "2",
        "itemName": "Summer tank top",
        "itemUrl": "http://mydomain.com/summer-tank",
        "itemImage": "http://mydomain.com/images/summer-tank.jpeg",
        "itemQuantity": 1,
        "itemPrice": 19.99,
        "itemWeight": 2
      }
    ],
    "shipments": [
      {
        "shipper": "UPS",
        "shippingMethod": "ground",
        "shippingPrice": 10,
        "trackingNumber": "3A4U569H1572924642"
      },
      {
        "shipper": "USPS",
        "shippingMethod": "international",
        "shippingPrice": 20,
        "trackingNumber": "9201120200855113889012"
      }
    ]
  },
  "recipient": {
    "fullName": "Bob Smith",
    "confirmationEmail": "bob@gmail.com",
    "confirmationPhone": "5047130000",
    "organization": "SIGNIFYD",
    "deliveryAddress": {
      "streetAddress": "123 State Street",
      "unit": "2A",
      "city": "Chicago",
      "provinceCode": "IL",
      "postalCode": "60622",
      "countryCode": "US",
      "latitude": 41.92,
      "longitude": -87.65
    }
  },
  "card": {
    "cardHolderName": "Robert Smith",
    "bin": 407441,
    "last4": "1234",
    "expiryMonth": 12,
    "expiryYear": 2015,
    "billingAddress": {
      "streetAddress": "",
      "unit": "2A",
      "city": "Chicago",
      "provinceCode": "IL",
      "postalCode": "60622",
      "countryCode": "US",
      "latitude": 41.92,
      "longitude": -87.65
    }
  },
  "userAccount": {
    "email": "bob@gmail.com",
    "username": "bobbo",
    "phone": "5555551212",
    "createdDate": "2013-01-18T17:54:31-05:00",
    "accountNumber": "54321",
    "lastOrderId": "4321",
    "aggregateOrderCount": 40,
    "aggregateOrderDollars": 5000,
    "lastUpdateDate": "2013-01-18T17:54:31-05:00"
  },
  "seller": {
    "name": "Amazon",
    "domain": "amazon.com",
    "shipFromAddress": {
      "streetAddress": "1850 Mercer Rd",
      "unit": "",
      "city": "Lexington",
      "provinceCode": "KY",
      "postalCode": "40511",
      "countryCode": "US",
      "latitude": 38.07,
      "longitude": -84.53
    },
    "corporateAddress": {
      "streetAddress": "410 Terry Ave",
      "unit": "3L",
      "city": "Seattle",
      "provinceCode": "WA",
      "postalCode": "98109",
      "countryCode": "US",
      "latitude": 47.6,
      "longitude": -122.33
    }
  }
},
{
  "purchase": {
    "browserIpAddress": "192.168.10.10",
    "orderId": "4ll3029s",
    "createdAt": "2016-07-29T19:54:31-05:00",
    "paymentGateway": "chip",
    "paymentMethod": "credit_card",
    "transactionId": "9995949492",
    "currency": "USD",
    "avsResponseCode": "Y",
    "cvvResponseCode": "M",
    "orderChannel": "EMAIL",
    "receivedBy": "Daffy Duck",
    "totalPrice": 13.13,
    "products": [
      {
        "itemId": "1",
        "itemName": "Orange Duck Feet",
        "itemUrl": "http://mydomain.com/duck-feet",
        "itemImage": "http://mydomain.com/images/duck-feet.jpeg",
        "itemQuantity": 5,
        "itemPrice": 10.99,
        "itemWeight": 3
      },
      {
        "itemId": "2",
        "itemName": "All season black top",
        "itemUrl": "http://mydomain.com/black-top",
        "itemImage": "http://mydomain.com/images/black-top.jpeg",
        "itemQuantity": 2,
        "itemPrice": 5.55,
        "itemWeight": 4
      }
    ],
    "shipments": [
      {
        "shipper": "UPS",
        "shippingMethod": "ground",
        "shippingPrice": 7,
        "trackingNumber": "3A4U569H1572924642"
      },
      {
        "shipper": "USPS",
        "shippingMethod": "international",
        "shippingPrice": 3,
        "trackingNumber": "9201120200855113889012"
      }
    ]
  },
  "recipient": {
    "fullName": "Patrick Star",
    "confirmationEmail": "patrick@gmail.com",
    "confirmationPhone": "4347130000",
    "organization": "SIGNIFYD",
    "deliveryAddress": {
      "streetAddress": "999 Main St.",
      "unit": "NA",
      "city": "New York",
      "provinceCode": "NY",
      "postalCode": "10598",
      "countryCode": "US",
      "latitude": 31.92,
      "longitude": -89.65
    }
  },
  "card": {
    "cardHolderName": "Patrick Star",
    "bin": 993402,
    "last4": "3849",
    "expiryMonth": 12,
    "expiryYear": 2019,
    "billingAddress": {
      "streetAddress": "",
      "unit": "NA",
      "city": "New York",
      "provinceCode": "NY",
      "postalCode": "10598",
      "countryCode": "US",
      "latitude": 31.92,
      "longitude": -89.65
    }
  },
  "userAccount": {
    "email": "patrick@gmail.com",
    "username": "patrick",
    "phone": "5555551212",
    "createdDate": "2015-03-18T17:54:31-05:00",
    "accountNumber": "54321",
    "lastOrderId": "4321",
    "aggregateOrderCount": 90,
    "aggregateOrderDollars": 902000,
    "lastUpdateDate": "2016-01-18T17:54:31-05:00"
  },
  "seller": {
    "name": "Amazon",
    "domain": "amazon.com",
    "shipFromAddress": {
      "streetAddress": "1850 Mercer Rd",
      "unit": "",
      "city": "Lexington",
      "provinceCode": "KY",
      "postalCode": "40511",
      "countryCode": "US",
      "latitude": 38.07,
      "longitude": -84.53
    },
    "corporateAddress": {
      "streetAddress": "410 Terry Ave",
      "unit": "3L",
      "city": "Seattle",
      "provinceCode": "WA",
      "postalCode": "98109",
      "countryCode": "US",
      "latitude": 47.6,
      "longitude": -122.33
    }
  }
}
                ]

    def create_case(self, json_input):
        case_url = "https://api.signifyd.com/v2/cases"
#        r = requests.get(case_url, auth=('HRnOQ9bGlIRsIfNLkRsJ09DEE', ''))
#        print(json_input)
        r = requests.post(case_url, json_input, None, auth=('HRnOQ9bGlIRsIfNLkRsJ09DEE', ''))
        return r

    def get_case(self, caseId):
        print(caseId)
        case_url = "https://api.signifyd.com/v2/cases/" + str(caseId)
        r = requests.get(case_url, auth=('HRnOQ9bGlIRsIfNLkRsJ09DEE', ''))
        return r


    def test_create_case_01(self):
        dict_input = SignifydTest.dataBank[0]
        json_input = json.dumps(dict_input)
#        print(dict_input)
#        print(json_input)
        r = self.create_case(json_input)
        print("status code:  " + str(r.status_code))
        assert(r.status_code == 201)
        investigationId = r.json()['investigationId']
        assert(investigationId > 1)
        print(investigationId)
        SignifydTest.caseId = investigationId

    def test_get_case_01(self):
        print("Sleeping 5 seconds...")
        sleep(5)
        r = self.get_case(SignifydTest.caseId)
        r_json = r.json()
        orderAmount = r_json['orderAmount']
        investigationId = r_json['investigationId']
        case_status = r_json['status']
        headline = r_json['headline']
        print(r.json())
        assert(orderAmount == 74.99)
        assert(investigationId == SignifydTest.caseId)
        assert(case_status == 'DISMISSED')
        assert(headline == 'Robert Smith')

    def test_create_case_02(self):
        dict_input = SignifydTest.dataBank[1]
        json_input = json.dumps(dict_input)
 #       print(dict_input)
 #       print(json_input)
        r = self.create_case(json_input)
        print("status code:  " + str(r.status_code))
        assert(r.status_code == 201)
        investigationId = r.json()['investigationId']
        assert(investigationId > 1)
        print(investigationId)
        SignifydTest.caseId = investigationId

    def test_get_case_02(self):
        print("Sleeping 5 seconds...")
        sleep(5)
        r = self.get_case(SignifydTest.caseId)
        r_json = r.json()
        orderAmount = r_json['orderAmount']
        investigationId = r_json['investigationId']
        case_status = r_json['status']
        headline = r_json['headline']
        print(r.json())
        assert(orderAmount == 74.99)
        assert(investigationId == SignifydTest.caseId)
        assert(case_status == 'DISMISSED')
        assert(headline == 'Robert Smith')



if __name__ == '__main__':
    unittest.main(verbosity=2)