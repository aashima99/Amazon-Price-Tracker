import requests
from bs4 import BeautifulSoup
import smtplib
import time

page_url="https://www.amazon.in/Fujifilm-Instax-Instant-Camera-Blush/dp/B085282C1R/ref=lp_22484840031_1_9?s=electronics&ie=UTF8&qid=1604164842&sr=1-9"

# set the browser agent and user string
browser_agent={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 RuxitSynthetic/1.0 v7082496601 t38550 ath9b965f92 altpub cvcv=2'}

def check_price():
    
    # sending a request to fetch HTML of the page
    product_page=requests.get(page_url,headers=browser_agent)
    
    # create the soup object
    soup= BeautifulSoup(product_page.content,'html.parser')
    
    print(soup.prettify())
    
    page_title=soup.find(id="productTitle").get_text() 
    
    product_price=soup.find(id="priceblock_ourprice").get_text()[2:7]
    
    product_price=product_price.replace(',','')
    final_price=float(product_price)
    
    #using strip to remove extra spaces in the title
    print(page_title.strip())
    
    if(final_price<5000):
        send_email()
        
# function that sends an email if the prices fell down   
def send_email():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('sender_emailid', 'password')
  subject = 'Price Fell Down'
  body = "Check the amazon link-https://www.amazon.in/Fujifilm-Instax-Instant-Camera-Blush/dp/B085282C1R/ref=lp_22484840031_1_9?s=electronics&ie=UTF8&qid=1604164842&sr=1-9  "
  message = f"Subject: {subject}\n\n{body}"

  server.sendmail('sender_emailid','reciever_emailid',message)
  
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

check_price()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60*60*24)
