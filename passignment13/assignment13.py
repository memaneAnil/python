
import os
from sys import *
import hashlib
import time
import os.path
import schedule
import email, smtplib, ssl
import ntpath


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def DeleteFiles(argv="demo"):
    arr={}

    
    starttime=time.time() 
    arr=FindDuplicate(argv)
    printDuplicate(arr)
    
    results=list(filter(lambda x: len(x)>1,arr.values()))
    
              
    filescan=0
    filedups=0
    path=""
    
    if len(results)>0:
        print("Duplicates Found :")

        print("The following files are identical.")
        log_dir='Marvellous'
        if not os.path.exists(log_dir):
            try:
                os.mkdir(log_dir)
            except:
                pass

        
        log_path=os.path.join(log_dir,"Log%s.txt"%(time.ctime()))
        path=log_path
        
        if not os.path.exists(log_path):
            try:
                fd=open(log_path,'w')
                print("file created in write mode")
            except:
                pass
        

       
        icnt=0
        
        for result in results:
            
            for subresult in result:
                icnt+=1
                filescan+=1
                if icnt>=2:
                    filedups+=1
                    print(subresult+"\n")
                    fd.write("%s\n" % subresult)
                    #fd.write(subresult)
                    os.remove(subresult)
        icnt=0
        
        fd.close()
        sendMail(path,filescan,filedups,starttime)
    else:
        print("No duplicate files found")
        exit()
def sendMail(path,filescan,filedups,starttime):
    subject = "An email with attachment from Python"
    body = "Stating time of scanning\n"+str(starttime)+"Total number of file scan is :\n"+str(filescan)+"Total number of duplicate file :"+str(filedups)
    sender_email = "annilmemane@gmail.com"
    receiver_email = "marvellousinfosystem@gmail.com"
    print("Enter password")
    password =input()

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email 
    
    message.attach(MIMEText(body, "plain"))
        #path=os.path.basename(path)
   
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
    
        
    
def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf= afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups={}
    
    if exists:
               
        for dirName,subdirs,FileList in os.walk(path):
            print("Current folder is :",dirName)
            for fname in FileList:
                path=os.path.join(dirName+"/"+fname)
                filehash=hashfile(path)

                if filehash in dups:
                    dups[filehash].append(path)
                else:
                    dups[filehash]=[path]
        return dups
        print("Error : Invalid number of arguments")
        exit()
        
    else:
        print("Invalid Path")

def printDuplicate(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values())) 

    if len(results)>0:
        print("Duplicates Found :")

        print("The following files are identical.")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print("\t\t%s"% subresult)

        
def main():

    print("Directory watcher application")
    if(len(argv)!=2):
        print("Insufficient arguments")
        exit()
    if(argv[1]=='-h'):
        print("this script will travel the directory and display the names of all entries")
        exit()
    if (argv[1]=='-u'):
        print("usage : Application_name Directory_name")
        exit()

    try:
        
        schedule.every(1).minutes.do(DeleteFiles,argv[1])
        #DeleteFiles(arr)
        while(True):
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

if __name__=="__main__":
    main()