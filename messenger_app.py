import re
from abc import ABC, abstractmethod

class MessagingService(ABC):
    @abstractmethod
    def send_message(self,number, message):
        pass

class SMSMessagingService(MessagingService):
    def send_message(self,number, message):
        print("Sending SMS message..." )

class EmailMessagingService(MessagingService):
    def send_message(self,subject, compose):
        print("Sending Email message... " )

class WhatsAppMessagingService(MessagingService):

    def send_message(self,number, message):
        print("Sending WhatsApp message..."  )
def isvalid(s):
    pattern=re.compile("[6-9][0-9]{9}")
    return pattern.match(s)
def valid_email(mail):
    regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex,mail):
        return True
    else:
        return False
def main():
    mes= SMSMessagingService()
    whatsapp = WhatsAppMessagingService()
    mail=EmailMessagingService()
    while True:
        print("         MESSAGE SERVICE        ")
        print("1.SMS Message Service")
        print("2.Email Message Service")
        print("3.Whatsapp Message Service")
        print("4.Close App")
        n = int(input("Enter your choice(1-4): "))
        if n==1:
            try:
                mobile_number = int(input("Enter the Mobile Number: "))
                if isvalid(str(mobile_number)):

                    sms = str(input("Enter the Message:"))

                    mes.send_message(mobile_number, sms)
                    print("SMS sent")
                else:
                    print("Please,Enter the valid mobile number.")
            except Exception as e:
                print("Enter the number between 0-9")
        elif n ==2:
            try:
                email_get = str(input("Enter the Email:"))
                if valid_email(email_get):
                    subject = str(input("Enter the subject : "))
                    compose = str(input("Compose: "))
                    mail.send_message(subject, compose)
                    print("Mail sent!")
                else:
                    print("Enter valid email.")
            except Exception as err:
                print(err)

        elif n==3:
            try:
                mobile_number = int(input("Enter the Whatsapp Mobile Number: "))

                if isvalid(str(mobile_number)):
                    print(f"{mobile_number} is in whatsapp?")
                    print("1.Yes")
                    print("2.No")
                    choice = int(input("Choose your Answer(1-2):"))
                    if choice == 1:
                        sms = str(input("Enter the Message:"))
                        whatsapp.send_message(mobile_number, sms)
                        print("Whatsapp Message sent")
                    else:
                        print("Please Add the Number in Whatsapp to send Message.")
                else:
                    print("Please,Enter the valid mobile number.")
            except Exception as err:
                print(err)
        elif n==4:
            print("Thanks for using our Message service app.")
            break
        else:
            print("Enter the valid number")

















main()
