import smtplib
import time
import urllib.request as ur
import json

from subprocess import check_output

def check_internet_connection(host="http://google.com"):
    try:
        print(f"Pinging {host}:")
        ur.urlopen(host)
        return True
    except:
        return False

def send_email(data, content):
    PORT = 587
    SERVER = "smtp.gmail.com"
    PASSWORD = data["app_pw"]
    
    SENDER_EMAIL = data["sender"]
    SENDER_NAME = data["sender_name"]
    RECIPIENT_EMAIL = data["recipient"]
    RECIPIENT_NAME = data["recipient_name"]

    session = smtplib.SMTP(SERVER, PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    session.login(SENDER_EMAIL, PASSWORD)

    message = f"from: {SENDER_NAME} <{SENDER_EMAIL}>\r\n"
    message += f"to: {RECIPIENT_NAME} <{RECIPIENT_EMAIL}>\r\n"
    message += f"subject: {SENDER_NAME} ip address \r\n\r\n"
    message += content

    session.sendmail(SENDER_EMAIL,data["recipient"] , message)
    session.quit


def main():
    print("Checking if client has an internet connection:")
    tries = 60
    while not check_internet_connection() and tries >= 0:
        time.sleep(3)


    with open("config.json", 'r') as j:
        data =  json.loads(j.read())
        ip_address = check_output(["hostname", "-I"]).decode("utf-8").split(" ")[0]
        content ="This is the IP address of your raspberry pi: " + ip_address

        print(f"Internet connection confirmed ({ip_address}), proceeding to send email: ")

        try:
            send_email(data, content)
            print("Email sent successfully")
        except:
            print("Something went wrong and the email could not be sent")


if __name__ == "__main__":
    main()
