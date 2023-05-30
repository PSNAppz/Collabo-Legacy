# How to calculate request signature
import hashlib

import json
import requests
def signature_check_status(arrData):

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

arrData = {
    'query_command' : 'CHECK_STATUS',
    'access_code' : 'QvMQiaL3flsiTGSu7FMe',
    'merchant_identifier' : 'AstdpYTL',
    'merchant_reference' : 'MyReference0001',
    'language' : 'en',
}



signature_check_status(arrData)






def check_status(url,arrData):

    headers = {
        'Content-Type': "application/json",
    }

    arrData = json.dumps(arrData)

    response = requests.request("POST", url, data=arrData, headers=headers)
    json_data = json.loads(response.text)
    print(json_data)
    return (json_data)


url = 'https://sbpaymentservices.payfort.com/FortAPI/paymentApi';
arrData = {
    'query_command' : 'CHECK_STATUS',
    'access_code' : 'QvMQiaL3flsiTGSu7FMe',
    'merchant_identifier' : 'AstdpYTL',
    'merchant_reference' : 'MyReference0001',
    'language' : 'en',
    'signature' : 'c77fbd6c834151436625943fdb7022e14111d82ba334bf62142c1ae7acd56a8e',
}
check_status(url,arrData)

