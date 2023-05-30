import cgi

requestParams = {
    "command" : "TOKENIZATION",
    "access_code" : "QvMQiaL3flsiTGSu7FMe",
    "merchant_identifier": "AstdpYTL",
    "merchant_reference" : "XYZ9239-yu898",
    "amount" : "1000",
    "currency" : "SAR",
    "language" : "en",
    "customer_email" :"naseem.10@gmail.com",
    "signature" :"2b2d34b216aec8122c08fca32620afd70dff9f4da63973f1df9b1fbd7c123ec8",
    "order_description" : "iPhone 6-S"
}


redirectUrl = 'https://sbcheckout.payfort.com/FortAPI/paymentPage'
print ("<html xmlns='http://www.w3.org/1999/xhtml'>\n<head></head>\n<body>\n")
print ("<form action='redirectUrl' method='post' name='frm'>\n")
for (slug, title) in requestParams.items():
    print ("\t<input type='hidden' name='"+ cgi.escape(slug)+"' value='"+ cgi.escape(title)+"'>\n")

print ("</form>")
print ("\t<script type='text/javascript'>\n")
print ("\t\tdocument.frm.submit();\n")
print ("\t</script>\n")
print ("\n</body>\n</html>")

#PASSaccess_code=QvMQiaL3flsiTGSu7FMeamount=1000command=PURCHASEcurrency=SARcustomer_email=dbpillai@gmail.comlanguage=enmerchant_identifier=AstdpYTLmerchant_reference=TEST81003PASS