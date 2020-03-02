# Spotify Autologin
### What is it?
Spotify Autologin is a simple script that uses OpenVPN and PyWinAuto to automate boring stuff like:
- Creating temporary OpenVPN service account
- Connecting to a specific OpenVPN server
- Logging in Spotify with your credentials and "correct" IP address

### Why do I need this?
Probably you don't.  
If you don't have Spotify premium and Spotify is not accessible in your country (e.g. Russia and CIS) then you need to login with fake IP every 2 weeks. I got tired of this and made script, that does all the boring stuff.

### How to install?
1. You need to have Python 3.6 or higher.
2. Install required libraries with `pip install -r requirements.txt`
3. Install and add to PATH OpenVPN.
4. Change values in [config.json](config.json). It's strongly recommended to change `vpn_username`. Also it is a bad practice to have raw password stored in any files. If you know how to — make script use your SYSVAR or store it encrypted and decrypt it only at script runtime.
5. You are ready-to-go. Just run `python run.py` in your command prompt.

### Would it be updated / do you accept PRs and Issues?
Yes. I would like to get any feedback. There are still a lot of work to do (for example, catching failed POST requests and retries in [helper.py](helper.py)) and I hope that you would help me with that :)

### License
[MIT](https://choosealicense.com/licenses/mit/)
