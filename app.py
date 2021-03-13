import requests
from bs4 import BeautifulSoup
import smtplib
import time

# start project by running the following:
# pip install requests bs4

URL = 'https://www.amazon.com.au/dp/B079Y45KTJ/?coliid=I2JMY1NEN16XP0&colid=1KG5W1RQ8FCS7&psc=1&ref_=lv_ov_lig_dp_it'

# User-Agent can be obtained simply by Googling 'my user agent'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

product = soup.find(id="productTitle").get_text().strip()
price_string = soup.find(id="priceblock_ourprice").get_text()
price = float(price_string.replace("$", ""))

def price_check():
    if(price < 700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # ^ Search Extended HELO
    server.ehlo()
    server.starttls()
    server.ehlo()

    # enable Google 2-step verification for the following pw used
    # then, generate app pw using Google App Password
    server.login('moiniqbal205@gmail.com', 'uexbeljczgbxndfi')
    # alternatively, can also choose 'less secure apps'

    subject = 'Price Drop!'
    body = f"Visit the link below to check the new price of {product}: \n\n https://www.amazon.com.au/dp/B079Y45KTJ/?coliid=I2JMY1NEN16XP0&colid=1KG5W1RQ8FCS7&psc=1&ref_=lv_ov_lig_dp_it"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'moiniqbal205@gmail.com', 
        'moiniqbal205@gmail.com',
        msg
    )
    print("Email has been sent! Please check your inbox")

    server.quit()

price_check()

# comment the above line and include the following to run a price check every 24 hours
# while(True):
#     price_check()
#     time.sleep(86400)