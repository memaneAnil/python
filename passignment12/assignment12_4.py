import os
import psutil
import time
from sys import *
import os
import email, smtplib, ssl
import ntpath


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def ProcessDisplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="_"*80
    
    log_path=os.path.join(log_dir,"Marvellous.log")
    path=log_path
    f=open(log_path,'w')
    f.write(separator+ "\n")
    f.write("Marvellous Infosystem process Logger : "+time.ctime()+ "\n")
    f.write(separator+ "\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


        for element in listprocess:
            f.write("%s\n" % element)

    f.close()

    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "annilmemane@gmail.com"
    receiver_email = "marvellousinfosystem@gmail.com"
    password =input()

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email 
    
    message.attach(MIMEText(body, "plain"))
    path=os.path.basename(path)
    print(path)
    filename=path
    
    
    with open(filename, "rb") as attachment:
        
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

   
    encoders.encode_base64(part)

    
    part.add_header("Content-Disposition",f"attachment; filename= {filename}",)

   
    message.attach(part)
    text = message.as_string()

    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

   


def main():
    print("___________Marvellous Infosytem by Piyush Khairnar__________")

    print("Application name :"+argv[0])

    if(len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if((argv[1]=='-h') or (argv[1]=='-H')):
        print("Help : This script is used log record of running processes")
        exit()

    if((argv[1]=='-u') or (argv[1]=='-U')):
        print("usage: Application name Absoulute path of directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__=="__main__":
    main()