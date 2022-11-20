# Monkey Type Auto Typer
This web crawler will automaticaly type on https://monkeytype.com.

<img src="README.assets\monkey_type.png">

# Instructions

### Driver
The web crawler depends on the Selenium Python library, which requires a browser driver. I used Google Chrome, so I will need a Chrome driver. You can find the latest Chrome drivers [here]( https://chromedriver.chromium.org).

Make sure to specify your driver's path in main.py.
```python
PATH = "C:\Program Files (x86)\chromedriver.exe" # the location of your driver

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
```

### Installation
Make sure you have Selenium installed.
```python
pip install selenium # install selenium with pip
```
### Things To Note
You can adjust the delay to make typing slower or faster.
```python
delay = 0 # the delay between each letter typed
```
Monkey Type has a bot detection system, so don't blame me when your account gets banned.
