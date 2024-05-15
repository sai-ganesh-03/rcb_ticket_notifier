import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_chrome_driver import GetChromeDriver
import time
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
get_driver = GetChromeDriver()
get_driver.install()

def send_email(sender_email, sender_password, receiver_emails, subject, message):
    # Set up the MIME
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = ', '.join(receiver_emails)
    email_message['Subject'] = subject

    # Attach the message to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_emails, email_message.as_string())

    # Quit the server
    server.quit()

def get_chat_ids(bot_token):
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
    data = response.json()
    chat_ids = []
    if data["ok"] and data["result"]:
        for result in data["result"]:
            chat_id = result["message"]["chat"]["id"]
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)
    return chat_ids

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

def check_url_for_ticket(urls):
    # Start a WebDriver session
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # required when running as root user. otherwise you would get no sandbox errors.
    chrome_options.add_argument("--headless") # No need to open browser window
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disk-cache-size=0")  # Disable disk cache
    chrome_options.add_argument("--disable-application-cache")  # Disable application cache
    chrome_options.add_argument("--disable-cache")
    driver = webdriver.Chrome(options=chrome_options)
    i=0

    # Create/open a file to write logs
    log_file = open("log.txt", "a")

    # log_file.write(str(get_chat_ids(bot_token)) + "\n")
    for url in urls:
        log_file.write(url + "\n")
        driver.get(url)
        time.sleep(5)  # Adjust the delay as needed

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        page_text = driver.find_element(By.TAG_NAME, "body").text
        if "Saturday, May 18, 2024 07:30 PM" in page_text or "Chennai Super Kings" in page_text:
            log_file.write("Yes " + url + "\n")  # or you can perform any action you want here
            sender_email='sandursaiganesh21@gmail.com'
            sender_password=os.getenv("SENDER_EMAIL_PASSWORD")
            receiver_emails=['sandursaiganesh@gmail.com','mshuja370@gmail.com']
            subject='Ticket Found!!!{}'.format(i)
            message="Ticket Found"
            send_email(sender_email, sender_password, receiver_emails, subject, message)
            log_file.write("Mail sent\n")

            # Send Telegram message
            telegram_message = "Ticket Found!!!!!"
            # chat_ids = get_chat_ids(bot_token)
            chat_ids = [617361892,988083039]
            if chat_ids:
                for chat_id in chat_ids:
                    send_telegram_message(bot_token, chat_id, telegram_message)
                    log_file.write(f"Message sent to chat ID: {chat_id}\n")
            else:
                log_file.write("No chat IDs found.\n")

            i=i+1

    # Close the WebDriver session
    driver.quit()
    log_file.close()

if __name__=="__main__":
    print("Started")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    # URLs to check
    urls = [
        "https://shop.royalchallengers.com/ticket",
        "https://www.royalchallengers.com/rcb-ipl-tickets"
    ]
    check_url_for_ticket(urls)
