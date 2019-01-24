# Bitly url shorterer

Project can be used to shorten url and then check its clicks count

### How to install

Register on http://bitly.com and click `GENERATE ACCES TOKEN`. 
It looks like 'dcdf6d1bdsd770fb069703f5a5e1c51e37ef67a8'.
Then create '.env' file and put token here in next format `'TOKEN=\'dcdf6d1bdsd770fb069703f5a5e1c51e37ef67a8\''`


Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to use
Create short link:
```
python main.py -u https://test.com
http://bit.ly/2S6axwL
```
See click count:
```
python main.py -u bit.ly/2S6axwL
0
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
