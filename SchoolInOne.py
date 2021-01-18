#SchoolInOne.py
#By Abhinav Balla, Pranav Aida, Anvith Vobbilisetty, and Surya Sripathi.

import smtplib #import library needed to send emails.
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMailWithAttachment(subject, message, ImgFileName):
    # Define these once; use them twice!
    strFrom = 'schoolhelper632@gmail.com'
    strTo = 'samplehelper1@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>' + message + '</b> <br><img src="cid:image1"><br>', 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    print (ImgFileName)
    fp = open(ImgFileName, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    s = smtplib.SMTP('smtp.gmail.com' , 587)
    s.starttls()
    s.login('schoolhelper632@gmail.com', 'Pranburvith')
    s.sendmail(strFrom, strTo, msgRoot.as_string())
    print(" \n Please wait...")
    print(" \n Sent!")
    s.quit()
   
def SendMailWithoutAttachment(subject, message):
    gmailaddress = "schoolhelper632@gmail.com"
    gmailpassword = "Pranburvith"
    mailto = "samplehelper1@gmail.com"
    # msg = input("What is your message? Please include your school email so the tutor can contact you back. \n ")
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Please wait...")
    print(" \n Sent!")
    mailServer.quit()

asking = True
while asking == True:
    q = str(input("Hello! I'm School-In-One. How can I assist you? Here are a few options that I can help with: Tutoring, Counseling or Mental Health, Report something, Class Scheduling. If you change your mind \n and don't feel like you need any help, please type none. "))
    answer = q.lower()

    if answer == "tutoring":
        tutor = str(input("What subject do you need tutoring in? Tutoring in Math, Science, Spanish, and English is available. Type the subject that you want tutoring in."))
        subject = tutor.lower()
        if subject =="math":
            print("Matching you with our Math tutor...")
            msg = input("What is your message? Please include your school email so we can contact you back. \n ")
            attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
            if attach in "yes":
                ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
                SendMailWithAttachment('Math Help', msg, ImgFileName)
            else:
                SendMailWithoutAttachment('Math Help', msg)
               
        if subject =="science":
            print("Matching you with our Science tutor...")
            msg = input("What is your message? Please include your school email so the tutor can contact you back. \n ")
            attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
            if attach in "yes":
                ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
                SendMailWithAttachment('Science Help', msg, ImgFileName)
            else:
                SendMailWithoutAttachment('Science Help', msg)  
                   
        if subject =="english":
            print("Matching you with our English tutor...")
            msg = input("What is your message? Please include your school email so the tutor can contact you back. \n ")
            attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
            if attach in "yes":
                ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
                SendMailWithAttachment('English Help', msg, ImgFileName)
            else:
                SendMailWithoutAttachment('English Help', msg)
           
        if subject =="spanish":
            print("Matching you with our Spanish tutor...")
            msg = input("What is your message? Please include your school email so the tutor can contact you back. \n ")
            attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
            if attach in "yes":
                ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
                SendMailWithAttachment('Spanish Help', msg, ImgFileName)
            else:
                SendMailWithoutAttachment('Spanish Help', msg)

    elif answer in 'counseling mental health':
        print("Matching you with our Counselor...")
        msg = input("What is your message? Please include your school email so the couselor can contact you back. We are here for you! \n ")
        attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
        if attach in "yes":
            ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
            SendMailWithAttachment('Counseling', msg, ImgFileName)
        else:
            SendMailWithoutAttachment('Counseling', msg)

    elif answer in "report something":
        msg = input("What would you like to report? \n ")
        attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
        if attach in "yes":
            ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
            SendMailWithAttachment('Reporting', msg, ImgFileName)
        else:
            SendMailWithoutAttachment('Reporting', msg)

    elif answer in "class scheduling":
       
        msg = input("What is your message? Please include your school email so we can contact you back. \n ")
        attach = str(input("Do you have an attachment to send along with the message? y/n ")).lower()
        if attach in "yes":
            ImgFileName = str(input("Please specify the location of the screenshot? ex:. c:\\downloads\\test.png \ \n"))
            SendMailWithAttachment('Class Scheduling', msg, ImgFileName)
        else:
            SendMailWithoutAttachment('Class Scheduling', msg)
       
    elif answer in "noneno":
            print("Okay! Thanks for stopping by anyway!")
            asking = False
   
    else:
            print("Sorry, I couldn't understand what you said. Please respond with: Tutoring, Counseling, Report Something, or Class Scheduling.")

    if answer not in "noneno":
        string = str(input(" \n Do you have another question? "))
        response = string.lower()
        if response in "yes yeah":
            print("Great!")
            asking = True
        elif response not in "yes yeah":
            print("Understood. Have a nice day!")
            asking = False