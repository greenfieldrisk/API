# to pull service info
# % python3 -mzeep https://service2.ultipro.com/services/LoginService

wsdl={'LoginService':'https://service2.ultipro.com/services/LoginService',
       'EmployeePerson':'https://service2.ultipro.com/services/EmployeePerson',
       'EmployeeAddress':'https://service2.ultipro.com/services/EmployeeAddress',
       'EmployeeJob':'https://service2.ultipro.com/services/EmployeeJob'}
       

from zeep import Client
from zeep import xsd
from zeep.settings import Settings
from zeep.xsd import Element

import lxml.etree as ET
import sys
import math

#to print the XML rather than sending it to the service.
# node = client.create_message(client.service, 'myOperation', user='hi')

header=xsd.ComplexType([
        xsd.Element(
            '{http://www.ultipro.com/services/loginservice}ClientAccessKey',
            xsd.String()),
        xsd.Element(
            '{http://www.ultipro.com/services/loginservice}Password',
            xsd.String()),
        xsd.Element(
            '{http://www.ultipro.com/services/loginservice}UserAccessKey',
            xsd.String()),
        xsd.Element(
            '{http://www.ultipro.com/services/loginservice}UserName',
            xsd.String()),
    ])
header_value = header(ClientAccessKey='S41PI',Password='+YB+H0cOBLl2|TGA3_/fL}T5L@+k!hQcZk8}!C;Ums46VM)Ym]',UserAccessKey='E8XIXE000010',UserName='AscentRMG')
#main
auth={'ClientAccessKey':'S41PI','Password':'+YB+H0cOBLl2|TGA3_/fL}T5L@+k!hQcZk8}!C;Ums46VM)Ym]','UserAccessKey':'E8XIXE000010','UserName':'AscentRMG'}
client = Client(wsdl['LoginService'])
result=client.service.Authenticate(_soapheaders=[header_value])
#result=client.create_message(client.service,'Authenticate',_soapheaders=[header_value])
print(result)
#print (dump(client))
#print(ET.tostring(result,pretty_print=True))

header=xsd.ComplexType([
        xsd.Element(
            '{http://www.ultimatesoftware.com/foundation/authentication/ultiprotoken}UltiProToken',
            xsd.String()),
        xsd.Element(
            '{http://www.ultimatesoftware.com/foundation/authentication/clientaccesskey}ClientAccessKey',
            xsd.String()),
    ])

body = xsd.Element(
    '{http://www.ultipro.com/contracts}query',
    xsd.ComplexType([
        xsd.Element(
            'PageSize',
            xsd.String()),
        xsd.Element(
            'PageNumber',
            xsd.String())
    ])
)
body_c=body(PageSize='10',PageNumber="1")
header_value=header(UltiProToken=result.Token,ClientAccessKey='S41PI')
client = Client(wsdl['EmployeePerson'])
result=client.service.FindPeople([body_c],_soapheaders=[header_value])
#result=client.create_message(client.service,'FindPeople',[body_c],_soapheaders=[header_value])
#print(ET.tostring(result,pretty_print=True))
print(result)
total=result['OperationResult']['PagingInfo']['TotalItems']
print(total)
pages=math.ceil(total/1000)
print(pages)
# parse result and pull the rest
# do the addresses

print("Addresses")
client=Client(wsdl['EmployeeAddress'])
result=client.service.FindAddresses([body_c],_soapheaders=[header_value])
print(result)

print("Jobs")
client=Client(wsdl['EmployeeJob'])
result=client.service.FindJobs([body_c],_soapheaders=[header_value])
print(result)