import os
import requests
import zipfile
import io
from datetime import date


# Main method that takes all job
def main_worker(conf):
	login, password = conf['login'], conf['password']
	webaddr = f"https://www.vpnjantit.com/create-free-account.html?server={conf['server']}&type=OpenVPN"
	webconf_addr = f"https://www.vpnjantit.com/assets/{conf['server']}.vpnjantit.com.zip"
	username = conf['vpn_username'] + date.today().strftime("-%d%m%y")

	downl_extract_config(webconf_addr)
	rename_config(conf['server'])
	create_user(username, conf['vpn_password'], webaddr)
	write_credentials(username, conf['vpn_password'])

	return login, password


# Creates user with the unique name at vpnjatit
def create_user(username, password, url):
	data = {
		'user': username,
		'pass': password
	}

	requests.post(url=url, data=data)


# Writes VPN login/password at the text file
def write_credentials(username, password):
	with open('pass.txt', 'w') as file:
		file.write(username + '-vpnjantit.com\n' + password)


# Obviously renames vpn config file
def rename_config(prefix):
	file = os.listdir(f'vpnconf/{prefix}.vpnjantit.com/')[1]
	os.rename(f'vpnconf/{prefix}.vpnjantit.com/' + file, 'cfg.ovpn')


# Downloads vpn config zip file and extracts it
def downl_extract_config(url):
	request = requests.get(url, stream=True)
	z = zipfile.ZipFile(io.BytesIO(request.content))
	z.extractall(path='vpnconf/')
