# FarmMarkets

This is my application what allows you to work with US farmers markets data in easy way.

### Basic requirements:
- Python [3.8^]
- MySQL


***
### Unpacking

First you have to set up virtual environment and install dependencies:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then create .env file and write your personal MYSQL profile data:
```
USERNAME = 'your username'
PASSWORD = 'your password'
```
And enter next console commands:
```
make init
make upload
```
***
### Usage

Enter command to launch the application:
```
make start
```
Commands and features:<br>
- **list [mode, reverse]** - shows all Farmers markets sorted by mode type;
- **guide** - shows app instruction;
- **exit** - finish session;





