import requests
#xml = """%3CRegisterUserRequest%3E%0A%20%20%20%3CPreRegisterId%3EODAwMDM3NTEzMzE2OTY2NzYxNg%3D%3D%3C%2FPreRegisterId%3E%0A%20%20%20%3CPhoneInputMethod%3E1%3C%2FPhoneInputMethod%3E%0A%20%20%20%3CBuildType%3E1%3C%2FBuildType%3E%0A%20%20%20%3CPhoneNumber%3E569450580%3C%2FPhoneNumber%3E%0A%20%20%20%3CPushToken%3EGCM%3Aen4SGbjVTN-Lmtp1HVcLxo%3AAPA91bFBj41v5aSksbi4jX5TObyNQvsfVzUdjw9TQflc7NPHt5FjqQHem1G1aEqx-1pxE5Wf9kTwkNNPrwy3Tgq7Wk33bDjU15uksWjHram7wMzZw78W2tk1-zQsGBDRCs4u60dwYpFp%3C%2FPushToken%3E%0A%20%20%20%3CCountryIDDCode%3E972%3C%2FCountryIDDCode%3E%0A%20%20%20%3CUDID%3E9a0eafb8735d8a5f2d1f6b115336e461563ac74d%3C%2FUDID%3E%0A%20%20%20%3CDeviceType%3ELenovo%20K52e78%3C%2FDeviceType%3E%0A%20%20%20%3CDevice%3Ephone%3C%2FDevice%3E%0A%20%20%20%3CDeviceManuf%3Elenovo%3C%2FDeviceManuf%3E%0A%20%20%20%3CSystemVersion%3E6.0%3C%2FSystemVersion%3E%0A%20%20%20%3CSystem%3EAndroid%3C%2FSystem%3E%0A%20%20%20%3CLanguage%3Een%3C%2FLanguage%3E%0A%20%20%20%3CViberVersion%3E16.5.0.9%3C%2FViberVersion%3E%0A%20%20%20%3CCC%3Eil%3C%2FCC%3E%0A%20%20%20%3CMCC%3E425%3C%2FMCC%3E%0A%20%20%20%3CMNC%3E05%3C%2FMNC%3E%0A%20%20%20%3CVoIP%3E1%3C%2FVoIP%3E%0A%20%20%20%3CMCCSim%3E425%3C%2FMCCSim%3E%0A%20%20%20%3CMNCSim%3E05%3C%2FMNCSim%3E%0A%20%20%20%3CMCCNetwork%3E425%3C%2FMCCNetwork%3E%0A%20%20%20%3CMNCNetwork%3E05%3C%2FMNCNetwork%3E%0A%20%20%20%3CIMSI%3E425052006492688%3C%2FIMSI%3E%0A%20%20%20%3CNoHangup%3E0%3C%2FNoHangup%3E%0A%20%20%20%3CReRegisterState%3E0%3C%2FReRegisterState%3E%0A%3C%2FRegisterUserRequest%3E"""
#xml = """<RegisterUserRequest> <PreRegisterId>ODAwMDM3NTEzMzE2OTY2NzYxNg==</PreRegisterId> <PhoneInputMethod>1</PhoneInputMethod> <BuildType>1</BuildType> <PhoneNumber>569450580</PhoneNumber> <PushToken>GCM:en4SGbjVTN-Lmtp1HVcLxo:APA91bFBj41v5aSksbi4jX5TObyNQvsfVzUdjw9TQflc7NPHt5FjqQHem1G1aEqx-1pxE5Wf9kTwkNNPrwy3Tgq7Wk33bDjU15uksWjHram7wMzZw78W2tk1-zQsGBDRCs4u60dwYpFp</PushToken> <CountryIDDCode>972</CountryIDDCode> <UDID>9a0eafb8735d8a5f2d1f6b115336e461563ac74c</UDID> <DeviceType>Lenovo K52e78</DeviceType> <Device>phone</Device> <DeviceManuf>lenovo</DeviceManuf> <SystemVersion>6.0</SystemVersion> <System>Android</System> <Language>en</Language> <ViberVersion>16.5.0.9</ViberVersion>"""
xml = """
<RegisterUserRequest>
   <PreRegisterId>MTU2NjI0NzQ0NTQ5NDY4MzMzMQ==</PreRegisterId>
   <PhoneInputMethod>1</PhoneInputMethod>
   <PhoneNumber>7156913180</PhoneNumber>
   <PushToken>GCM:dJ8w_8NBQ_Ksi8yET6hxXm:APA91bEw894q39qP4wDfX9sUdOsnTGHYKXvI91LQ4PjQ16pXTez3S9y1frHZE-zO20VzZ4mfl5aXHkllMb1F7PApAYeZY9XPViomAPXU4oqe84zJj9lVVfu4jgU-4H9vQVru62Dhiy5_</PushToken>
   <CountryIDDCode>1</CountryIDDCode>
   <UDID>74983d250dfbbc5bf230a021b1ec529689496129</UDID>
   <DeviceType>A33w</DeviceType>
   <Device>phone</Device>
   <DeviceManuf>oppo</DeviceManuf>
   <SystemVersion>5.1</SystemVersion>
   <System>Android</System>
   <Language>ar</Language>
   <ViberVersion>15.2.0.14</ViberVersion>
   <CC>eg</CC>
   <MCC>602</MCC>
   <MNC>02</MNC>
   <VoIP>1</VoIP>
   <MCCSim>602</MCCSim>
   <MNCSim>03</MNCSim>
   <MCCNetwork>602</MCCNetwork>
   <MNCNetwork>02</MNCNetwork>
   <IMSI>602022202435114</IMSI>
   <NoHangup>0</NoHangup>
   <ReRegisterState>0</ReRegisterState>
</RegisterUserRequest>"""
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent':'Android',
           'Content-Length':'1502',
           'Host':'secure.viber.com',
           'Connection':'close',
           'Accept-Encoding':'gzip',
           'Accept-Encoding':'deflate'}
print("sending the request...")   

print(requests.post('https://secure.viber.com/viber/viber.php?function=RegisterUser', data=xml, headers=headers).text)

i = 0
#while i < 10: 
##  print(requests.post('http://secure.viber.com/viber/viber.php?function=RegisterUser', data=xml, headers=headers).text)    
# i = i + 1

print("finished")   
