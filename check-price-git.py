import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.uk/ADMI-Gaming-PC-A10-9700-Graphics/dp/B00J5JOQF2?ref_=Oct_RAsinC_Ajax_428651031_2&pf_rd_r=Y22XW560JSY2ZZG75AP6&pf_rd_p=2bf28924-7788-5c31-88ed-99de4daa9e7c&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=428651031&pf_rd_m=A3P5ROKL5A1OLE"

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}

def check_price():

	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, "html.parser")
	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[1:10])
	if converted_price < 200:
		send_mail()
	print(title.strip())
	print(converted_price)
	if converted_price > 200:
		send_mail()


def send_mail():
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("mail@gmail.com", "password")
	subject = "Price fell down"
	body = "https://www.amazon.co.uk/ADMI-Gaming-PC-A10-9700-Graphics/dp/B00J5JOQF2?ref_=Oct_RAsinC_Ajax_428651031_2&pf_rd_r=Y22XW560JSY2ZZG75AP6&pf_rd_p=2bf28924-7788-5c31-88ed-99de4daa9e7c&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=428651031&pf_rd_m=A3P5ROKL5A1OLE"
	msg = "Subject: {} {}".format(subject, body) 
	server.sendmail(
		"frommail@gmail.com",
		"tomail@gmail.com",
		msg
		)
	print("HEY E-MAIL HAS BEEN SENT")
	server.quit()


while True:
	check_price()
	time.sleep(60)