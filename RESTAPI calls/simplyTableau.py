from urllib2 import urlopen, Request
import xml.etree.ElementTree as ET

API_VERSION = 2.2


def signIn(server_name,site_url_id,user_name,password):

	signin_url = "https://{server}/api/{api_v}/auth/signin".format(server=server_name,api_v=API_VERSION)

	request_xml = ET.Element('tsRequest')
	credentials = ET.SubElement(request_xml, 'credentials',name=user_name, password=password)
	site_element = ET.SubElement(credentials, 'site',contentUrl=site_url_id)
	request_data = ET.tostring(request_xml)
	try:
		req = Request(signin_url, data = request_data)
		req = urlopen(req)
		server_response = req.read()
		signIn_STATUS = True
	except Exception e:
		signIn_STATUS = False
	
	if signIn_STATUS == True:
		token = response_xml.find('.//t:credentials',namespaces={'t':"http://tableau.com/api"}).attrib['token']
		site_id = response_xml.find('.//t:site',namespaces={'t': "http://tableau.com/api"}).attrib['id']
	else:
		token = None
		site_id = None

	return signIn_STATUS,e,token,site_id



def signOut(server_name,token):

	headers = {'X-tableau-auth': token}
	signout_url = "http://{server}/api/{api_v}/auth/signout".format(server=server_name,api_v=API_VERSION)

	try:
		req = Request(signout_url, headers=headers, data=b'')
		req = urlopen(req)
		signOut_STATUS = True
	except Exception e:
		signOut_STATUS = False

	return signOut_STATUS,e



def getSites():
	