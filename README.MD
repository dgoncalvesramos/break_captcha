# Break_captcha

## What is it ?

A simple python script used to complete a [challenge](https://www.root-me.org/fr/Challenges/Programmation/CAPTCHA-me-if-you-can) on root-me. The purpose was to break the captcha in less than 3 seconds. The result flag is written on the requests_results html file. You need [pytesseract](https://pypi.org/project/pytesseract/) module.

## Running
 `$ python break_captcha.py` 

The project was built on python 3. 

## Common errors 

Please be aware that the script doesn't recognize all captchas (need an update on the process captcha function) so if you have a failure in your requests_result html file, relaunch the script until a captcha is recognized. You also may need to install the following package `$ 
sudo apt install python3-packaging`if you got the `ImportError: No module named 'packaging'`. Finally you need to be log on root-me.org to use the script.
 
