Bit-bar-ly
==========

### Bitly click counts in your Mac OS X Menu Bar.

![bit-bar-ly](https://lunavision.s3-us-west-1.amazonaws.com/bit-bar-ly.png?v2)

Quick Install
-------------
- [Get BitBar](https://getbitbar.com/)
- Add plugin to bitbar: 
```
bitbar://openPlugin?title=bit-bar-ly&src=https://raw.githubusercontent.com/tlugger/bit-bar-ly/master/clicks.5m.py
```
- Select plugin from menu bar (will say 'Missing Access Token' or show warning)
- Select `Run in Terminal`
- In Terminal enter: `pip install requests emoji-country-flag --user`
- Select `Preferences` -> `Open Plugin Folder`
- Edit `clicks.5m.py` add your [Bitly access token](https://bitly.is/accesstoken) between the quotes for `BITLY_ACCESS_TOKEN`
- Optional, set a `BITLY_GROUP_GUID` value if your account has multiple groups

Manual Install
--------------
- `pip install -r requirements.txt --user`
- copy clicks.5m.py to your bitbar_plugins folder
- set `BITLY_ACCESS_TOKEN` with your token obtained from https://bitly.is/accesstoken
