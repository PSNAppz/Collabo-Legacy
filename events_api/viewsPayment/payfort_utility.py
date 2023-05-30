# How to calculate request signature
import hashlib

import json
import requests
def get_signature(arrData):

    shaString=''


    for key in sorted(arrData.keys()) :
        line= key + "=" + arrData[key]
        shaString += line
    shaString = "PASS"+ shaString + "PASS"
    print(shaString)
    signature = hashlib.sha256(shaString.encode('utf-8')).hexdigest()

    #signature=hashlib.sha256(shaString.encode()).hexdigest()

    #your request signature
    print(signature)
    return (signature)

# arrData = {
#     'query_command' : 'CHECK_STATUS',
#     'access_code' : 'QvMQiaL3flsiTGSu7FMe',
#     'merchant_identifier' : 'AstdpYTL',
#     'merchant_reference' : 'MyReference0001',
#     'language' : 'en',
# }
#
#
#
# get_signature(arrData)






def payfort_operation(url,arrData):

    headers = {
        'Content-Type': "application/json",
    }

    arrData = json.dumps(arrData)

    response = requests.request("POST", url, data=arrData, headers=headers)
    json_data = json.loads(response.text)
    return (json_data)


#url = 'https://sbpaymentservices.payfort.com/FortAPI/paymentApi';
# arrData = {
#     'query_command' : 'CHECK_STATUS',
#     'access_code' : 'QvMQiaL3flsiTGSu7FMe',
#     'merchant_identifier' : 'AstdpYTL',
#     'merchant_reference' : 'MyReference0001',
#     'language' : 'en',
#     'signature' : 'c77fbd6c834151436625943fdb7022e14111d82ba334bf62142c1ae7acd56a8e',
# }
#payfort_operation(url,arrData)

