import os
import datetime
import smtplib

### credentional for mail ###
mailAddressFrom = "test@test.com"
mailAddressFromPassword = "*****"
mailAddressToSuccess = {"test@test.com"}
mailAddressToBrocken = {"test@test.com"}

smtpServer = smtplib.SMTP('outlook.office365.com', 587)
smtpServer.starttls()
smtpServer.login(mailAddressFrom, "*****")
successMessageText = "successful backup"
brockenMessageText = "brocken backup"

### service name, need set backup name machines ###
listServiceBackup = ["File_Name_1", "File_Name_2"]

### work dir, found file ####
workDir = "S:\BCU\Day"

### found character in file name (delimiter character in file name) ###
charFind = 'D'

### find file extension for check ###
extensionFile = ".vbk"

### list elements for equals empty list ###
listBack = []

### get system date ###
dates = datetime.datetime.now().date().__str__()

def chackDatafile(pathDir, *args ):
    for filename in os.listdir(pathDir):
        a = os.path.getmtime(filename)
        if filename.endswith(extensionFile) and datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d')==dates and listServiceBackup.__contains__(filename.rsplit(charFind)[0]):
            tempelementForEquals = filename.rsplit(charFind)[0]
            listBack.append(tempelementForEquals)
    sendMailBrockenBackup = set(listServiceBackup) - set(listBack)
    if not sendMailBrockenBackup:
        sendMailSuccess()
    else:
        sendMailbrocken(sendMailBrockenBackup)

def sendMailbrocken(sendMailBrocken):
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressToBrocken,
        "Subject: %s" % "backup is brocken",
        "",
        "backup is brocken" + sendMailBrocken.__str__()
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressToBrocken, mailBodyMassage)
    smtpServer.quit()

def sendMailSuccess():
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressToSuccess,
        "Subject: %s" % "all backups are done successfully",
        "",
        "backup done is well"
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressToSuccess, mailBodyMassage)
    smtpServer.quit()

### run for test ####
chackDatafile(os.chdir(workDir), listServiceBackup)
