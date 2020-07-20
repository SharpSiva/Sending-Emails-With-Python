import os
import smtplib          #defines an SMTP client session object that can be used to send mail to any Internet machine
import imghdr           #The imghdr module determines the type of image contained in a file.

Email_Address=os.environ.get('Email_Address')        #Hiding username,password in Env variable
Email_Password=os.environ.get('Email_Password')

from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='Welcome'
msg['From']='Sender@gmail.com'
msg['To']='Receiver@gmail.com'
msg.set_content("""Hi,Guys!
               Let me introduce the brand new Logo
               Along with that we have pdf
               Hope, you all will like it.
                """)
#To add image as attachments
files=['python_black.jpg','python_white.jpg']         #if file in diff location,mention path.
for file in files:
    with open(file,'rb') as img:
        imge_data=img.read()
        imge_type=imghdr.what(img.name)
        imge_name=img.name
        #print(imge_type)                             #To identify the format of image.
    msg.add_attachment(imge_data,maintype='image',subtype=imge_type,filename=imge_name)
#To add PDF as attachments
with open('A_Byte_of_python.pdf','rb') as pdf:
    pdf_data=pdf.read()
    pdf_name=pdf.name
msg.add_attachment(pdf_data,maintype='application',subtype='octet-stream',filename=pdf_name)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(Email_Address,Email_Password)
        server.send_message(msg)
except smtplib.SMTPAuthenticationError:
    print("Authentication Error! Please verify your Username and Password")
except Exception:
    print("Something went wrong!")
else:
    print("Mail send successfully")


