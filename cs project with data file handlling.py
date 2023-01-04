import pickle
import smtplib as s
from random import seed
from random import randint
print("#######WELCOME TO THE REGISTRATION PAGE OF NATIONAL EXAM OF SUMMATIVE ASSESSMENT#############")

seed(1)
for i in range(1):
    cndterollno = randint(100000, 1000000)
Record = []
caste = ()
f = 1
z = 1
br = True
cd = True
while f == 1:
    name = (input("Enter Candidate's Name-"))
    parents = (input("Father's Name-"))
    school = (input("Last school Attended-"))
    marks = int(input("Marks scored in Sr Secondary (in percentage)-"))
    if marks > 60:
        print("proceeding...")
        break
    else:
        print("Sorry! you don't clear the eligibility criteria for the examination. Good Luck!")
        continue

while br == True:
    categories = ["1. General", "2. Other Backward Classes", "3. Scheduled Caste/Scheduled Tribe"]
    print(*categories, sep = "\n")
    print("type in your category")
    ch = int(input("enter the serial number of your respective category"))
    if ch == 1:
        caste = ("General")
    if ch == 2:
        caste = ("Other Backward Class")
    if ch == 3:
        caste = ("Scheduled Caste/Scheduled Tribe")
    if ch >= 4:
        continue
    else:
        break

while z == 1:
    Idnumber=int(input("Enter your 12 Digit AadharId/DrivingLicense number"))
    if len(str(Idnumber)) == 12:
        break
    else:
        continue

while cd == True:
    streams = ["1. Physics, Chemistry, Maths", "2. Physics, Chemistry, Biology", "3. Physics, Chemistry,Geography",
               "4. Physics, Chemistry with other subjects", "5. Political Science, History, Geography",
               "6. Other Subjects"]
    print(*streams, sep="\n")
    streamch = int(input("Choose your respective stream by entering the numbers allocated"))
    if streamch == 1:
        stream = ("Physics,Chemistry,Maths")
    if streamch == 2:
        stream = ("Physics,Chemistry,Biology")
    if streamch == 3:
        stream = ("Physics,Chemistry,Geography")
    if streamch == 4:
        stream = ("Physics,Chemistry with other subjects")
    if streamch == 5:
        stream = ("Political Science,History,Geography")
    if streamch == 6:
        stream = ("Personalised Subjects(non-listed)")
    if streamch >= 7:
        continue
    else:
        break

mailaddress = (input("Your Email Address-"))
Datalist = [name, parents, school, caste, stream, cndterollno]
Data=str(Datalist)

Record.append(Data)
data_bytes=str.encode(Data)

f=open("stregistration.dat","ab")
f.write(data_bytes)
f.close()



ob = s.SMTP("smtp.gmail.com", 587)

ob.starttls()

ob.login("upscmockery@gmail.com", "UPSCmockery@gmail12")

subject = "Exam Registration Details - UPSCmockery"
body = ("Hey", name, "Aadhar ID number-",Idnumber,
        "You have successfully submitted your application for National Exam of Summative Assessment, 20XX and",
        "It is subject to further scrutiny in terms of prescribed eligibility conditions."
        "Your candidature is further subject to the eligibility criterion as per the notification and acceptability of your Document ID number"
        , "Following are your exam registration details", Data)

message = "subject:{}\n\n{}".format(subject, body)
ob.sendmail("UPSC mockery", mailaddress, message)
print("Your Registration Details were sent to your respective email")
print(*Datalist, sep = "\n")
ob.quit()
