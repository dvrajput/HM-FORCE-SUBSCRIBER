[![HM FORCE SUBSCRIBER](https://telegra.ph/file/829b818e87735d6af1a0c.png)](https://t.me/hmrequestbot)
# Introduction
**A Telegram Bot to force users to join a specific channel before sending messages in a group.**

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HM-MODS/HM-FORCE-SUBSCRIBER)


## Todo
- [ ] Add multiple channels support
- [X] Configure different groups with different channels
- [X] Clean messages after completion
- [ ] LOGGER support.

## Deploy

### Installation
- Clone this repo
```
git clone https://github.com/HM-MODS/HM-FORCE-SUBSCRIBER
```
- Change directory
```
cd HM-FORCE-SUBSCRIBER
```
- Install requirements
```
pip3 install -r requirements.txt
```

### Configuration
Add [APP_ID](https://my.telegram.org/apps), [API_HASH](https://my.telegram.org/apps), [BOT_TOKEN](https://t.me/botfather) in [Config.py](Config.py) or in Environment Variables.

### Deploying
- Run bot.py
```
python3 bot.py
```


