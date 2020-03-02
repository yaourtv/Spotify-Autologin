import subprocess, os
import json
import helper
from pywinauto import Application


localappdata = os.getenv('APPDATA')
# All VPN job goes here
with open("config.json") as configfile:
	conf = json.load(configfile)
	login, password = helper.main_worker(conf)

# Starting OpenVPN service
# Probably something bad happens there (single thread, not setting up connection properly)
subprocess.call(["run_ovpn.bat"])

# Starting Spotify application @ C:\Users\%Username%\AppData\Roaming\Spotify
# Change username here
app = Application(backend="uia").start(localappdata + "\Spotify\Spotify.exe")
app.wait_cpu_usage_lower()
# Unimportant method. Should be removed
app.Spotify.print_control_identifiers()

# Login field
app.Spotify.edit2.set_text(login)
# Password field
app.Spotify.edit4.set_text(password)
# Submit button
app.Spotify.Button5.click()
