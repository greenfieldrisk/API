# to pull service info
# % python3 -mzeep https://service2.ultipro.com/services/LoginService

wsdl='https://service2.ultipro.com/services/LoginService'
auth={'ClientAccessKey':'S41PI','Password':'+YB+H0cOBLl2|TGA3_/fL}T5L@+k!hQcZk8}!C;Ums46VM)Ym]','UserAccessKey':'E8XIXE000010','UserName':'AscentRMG'}

#Service: LoginService
     #Port: WSHttpBinding_ILoginService (Soap12Binding: {http://tempuri.org/}WSHttpBinding_ILoginService)
         #Operations:
            #Authenticate(_soapheaders={ClientAccessKey: xsd:string, Password: xsd:string, UserAccessKey: xsd:string, UserName: xsd:string}) -> Status: ns1:AuthenticationStatus, StatusMessage: xsd:string, Token: xsd:string
#

#to print the XML rather than sending it to the service.
# node = client.create_message(client.service, 'myOperation', user='hi')
from zeep import Client
import lxml.etree as ET



client = Client(wsdl)
result=client.service.Authenticate(_soapheaders=auth)
#node = client.create_message(client.service,'Authenticate',_soapheaders=auth)

#print(node)
#print(ET.tostring(node,pretty_print=True))

print(result)
