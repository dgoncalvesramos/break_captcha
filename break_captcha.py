from io import BytesIO 
import lxml.html 
from PIL import Image, ImageEnhance, ImageFilter	
import requests
import base64
import pytesseract
import sys
import fileinput

def load_captcha(html): 
	tree = lxml.html.fromstring(html) 
	img_data = tree.cssselect('img')[0].get('src') 
	img_data = img_data.split(',')[1]
	base64_bytes = img_data.encode('utf-8')
	binary_img_data = base64.b64decode(base64_bytes)
	file_like = BytesIO(binary_img_data) 
	img = Image.open(file_like) 
	return img
       	
def submit_form(url,session,str_captcha):
	payload = {'cametu': str_captcha}
	r = requests.post(url,payload,cookies=session)
	with open("requests_results.html", "wb") as f:
		f.write(r.content)

def process_captcha(captcha):
	captcha.save('captcha_original.png')
	gray = captcha.convert('L')
	gray.save('captcha_gray.png')
	im = gray.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(im)
	im = enhancer.enhance(2)
	im = im.convert('1')
	im.save('final_captcha.png')		
	str_captcha = pytesseract.image_to_string('final_captcha.png')
	str_strip_captcha = ""
	i=0
	while(i<12) :
		str_strip_captcha += str_captcha[i]
		i+=1
	return str_strip_captcha
			
url = 'http://challenge01.root-me.org/programmation/ch8/'
r = requests.get(url)
session = r.cookies
captcha = load_captcha(r.content)
submit_form(url,session,process_captcha(captcha))

