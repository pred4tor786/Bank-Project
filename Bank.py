import mysql.connector as my  
import math, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def place_value(number): 
	return ("{:,}".format(number))

digits = "0123456789"
OTP = ""
for z in range(6) : 
    OTP += digits[math.floor(random.random() * 10)]

sender_name= "AMD BANK"
subject1="OTP FOR ACCOUNT VERIFICATION IS - "
subject=subject1 + OTP


con=my.connect(host="localhost",db="project",user="root",password="root")
cs=con.cursor()

print("#################### Welcome To AMD Bank ####################")
print('''1. Login
2. Register
3. Exit''')

choice=int(input("Enter your choice:"))

if choice==1:
    go=0
    username=input("Please Enter your Username:")
    rslt=""
    lo="locked"
    temp= False
    w="select email_id from AMDB"
    cs.execute(w)
    fetch=cs.fetchall()
    for x in fetch:
        if username in x:
            temp=True
            go=1
    if temp:
         pass
    else:
        print("Invalid Username.Please Try Again.")
        sys.exit()
    
    if go==1:
        p="select passwd from AMDB where email_id=('{}')". format(username)
        cs.execute(p)
        fetch1=cs.fetchall()
        q="select account_status from AMDB where email_id=('{}')". format(username)
        cs.execute(q)
        fetchStatus=cs.fetchone()
        if lo in fetchStatus:
            print("Unable to Login as your account has been locked temporarily.Please try again later.")
            sys.exit()
        else:
            pass
    for i in range(1,4):
        password=input('Enter password:')
        for x in fetch1:
            if password not in x:
                rslt="F"
                print("Please Enter Valid Password.","Number of Attempts left:",3-i)
        if rslt!="F":
            break
    else:
        pass
                
    if (3-i)==0:
        print("==> ACCOUNT LOCKED <==")
        print("Please Try Again After 24 Hours.")
        accstatus="update amdb set account_status ='locked' where email_id=('{}')". format(username)
        cs.execute(accstatus)
                
                
    else:
        qeury="select Account_No from amdb where email_id=('{}')". format(username)
        cs.execute(qeury)
        account_ex=cs.fetchone()
        for i in account_ex:
            account_in=i
        print("---> LOGIN SUCCESSFUL <---")
        rslt="S"
    fnamequery="select fname from amdb where email_id=('{}')". format(username)
    cs.execute(fnamequery)
    fname=list(cs.fetchone())
    for m in fname:
        dname=m
    lnamequery="select lname from amdb where email_id=('{}')". format(username)
    cs.execute(lnamequery)
    lname=list(cs.fetchone())
    for l in lname:
        dlname=l    
    if rslt=="S":
        print("Redirecting...")
        curdate= datetime.today().strftime("%B %d, %Y")
        curtime= datetime.now().strftime("%I:%M%p")
        subsec="SECURITY ALERT ! You Account has been accessed on "+ curdate + " at " + curtime
        email_id= "AMDBANKVERIFY@gmail.com"
        password= "ipprojectop"
        message= MIMEMultipart()
        message["from"] = sender_name
        message["to"] = username
        message["subject"] = subsec

        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(email_id,password)
                smtp.send_message(message)
        print("####################","Welcome",dname,dlname,"####################")
        print('''OPTIONS :-
        1. Withdraw Money
        2. Add Money
        3. Transaction Statistics
        4. Net Banking
        5. Delete Account''')

        print()
        
        choice2= int(input("Enter the option which you want to perform:"))
              
        if choice2==1:
            TransactionType='Withdrawn'
            digits1 = "0123456789"
            OTPw = ""
            for z in range(4) : 
                OTPw += digits1[math.floor(random.random() * 10)]
            subw="OTP for withdrawing money from your AMD Bank account is- " + str(OTPw)
            account_de=input("Please Enter Bank Account Number:")
            wmoney=int(input("Enter the amount of money to be withdrawn:"))
            amch= "select Amount from AMDB where email_id=('{}')". format(username)
            cs.execute(amch)
            fetch_amount=cs.fetchone()
            for op in list(fetch_amount):
                curr=int(op)
                
            if curr<wmoney:
                print("Your Account do not have sufficient money in order to withdraw given Amount.")
            
            else:
                print("Sending request,Please wait... ")
                email_id= "AMDBANKVERIFY@gmail.com"
                password= "ipprojectop"
                message= MIMEMultipart()
                message["from"] = sender_name
                message["to"] = username
                message["subject"] = subw

                with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(email_id,password)
                    smtp.send_message(message)
                    
                    print("An OTP has been sent to your registered Email.Please enter the OTP for verification")
                    input_OTPw=input("Please enter the OTP:")
                    if OTPw==input_OTPw:
                        m="update AMDB set Amount=Amount-{} where email_id=('{}')". format(wmoney,username)
                        cs.execute(m)

                        n="select Amount from AMDB where email_id=('{}')". format(username)
                        cs.execute(n)
                        updtbal= cs.fetchone()
                        for ou in list(updtbal):
                            upba=int(ou)
                        statsQuery="insert into stats(email_id,updatbal,Transaction_Type, DateOfTransaction) values('{}',{},'{}',NOW())". format(username,upba,TransactionType)
                        cs.execute(statsQuery)
                        statement="insert into statement(DateOfTransaction,Account_No,Transac_Desc,Withdrawls,Balance) values(NOW(),{},'Withdrawn',{},{})". format(account_de,wmoney,upba)
                        cs.execute(statement)
                        print("=======> TRANSACTION SUCCESSFUL.<=======")
                        print("Updated Balance:","Rs",upba)
                    else:
                        print("OTP entered is wrong.Transaction Failed")
                    
            
        
        elif choice2==2:
            TransactionType='Added'           
            digits2 = "0123456789"
            OTPa = ""
            for l in range(4) : 
                OTPa += digits2[math.floor(random.random() * 10)]
            account_de=input("Please Enter Bank Account Number:")
            amoney=int(input("Enter the amount of money to be added:"))
            suba="The OTP sent for adding money to your AMD Bank account is - " +  str(OTPa)
            
            print("Sending request,Please wait... ")
            email_id= "AMDBANKVERIFY@gmail.com"
            password= "ipprojectop"
            message= MIMEMultipart()
            message["from"] = sender_name
            message["to"] = username
            message["subject"] = suba
            with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(email_id,password)
                smtp.send_message(message)

                print("An OTP has been sent to your registered Email.Please enter the OTP for verification")
                otpav=input("Please enter OTP here:")
                if OTPa==otpav:
                    d="update AMDB set Amount=Amount+{} where email_id=('{}')". format(amoney,username)
                    cs.execute(d)
                    o="select Amount from AMDB where email_id=('{}')". format(username)
                    cs.execute(o)
                    updatbal=cs.fetchone()
                    for oo in list(updatbal):
                                upbal=int(oo)
                    statsQuery="insert into stats(email_id,updatbal,Transaction_Type,DateOfTransaction) values('{}',{},'{}',NOW())". format(username,upbal,TransactionType)
                    cs.execute(statsQuery)
                    statement="insert into statement(DateOfTransaction,Account_No,Transac_Desc,Deposits,Balance) values(NOW(),{},'DEPOSITED',{},{})". format(account_de,amoney,upbal)
                    cs.execute(statement)
                    print("=======> TRANSACTION SUCCESSFUL.<=======")
                    print("Updated Balance:","Rs",upbal)
                else:
                    print("OTP entered is wrong.Transaction Failed")

        elif choice2==3:
            z=','
            xlst=[]
            ylst=[]
            xquery="select DateOfTransaction from stats where email_id=('{}')". format(username)
            cs.execute(xquery)
            x=cs.fetchall()
            yquery="select updatbal from stats where email_id=('{}')". format(username)
            cs.execute(yquery)
            y=cs.fetchall()
            for i in x[::]:
                xlst.append(str(i[-1]))
            for o in y:
                if z in str(o) :
                    ylst.append(list(o))
            plt.plot(xlst,ylst)
            plt.xlabel('DATE OF TRANSACTION')
            plt.ylabel('UPDATED BALANCE')
            plt.gcf().canvas.set_window_title('Transaction Statistics')
            plt.show()

        elif choice2==4:
            print('''OPTIONS :-
        1. Send Money
        2. Account Statement ''')

            print()
     
            choice3=int(input("Enter the option which you want to perform:"))

            if choice3==1:
                print(''' OPTIONS :-
        1. AMD to AMD Bank Account
        2. Exit ''')

                print()

                bchoice=int(input("Please Select One Option:"))

                if bchoice==1:
                    digits1 = "0123456789"
                    OTPs = ""
                    for z in range(4) : 
                        OTPs += digits1[math.floor(random.random() * 10)]
                    subs="OTP for Sending money from your AMD Bank account is- " + str(OTPs)
                    account_de=input("Please Enter Bank Account Number from which the Amount has to be Sent:")
                    acc_no=input("Please Enter Bank Account Number to which the Amount has to Sent:")
                    desc=input("Enter a Description for Transaction:")
                    que="select Account_No from amdb"
                    cs.execute(que)
                    fetch_acc=cs.fetchall()
                    for x in fetch_acc:
                        if acc_no in x:
                            temp=True
                            go=1
                    if temp:
                        pass
                    else:
                        print("Invalid Account Number.Please Try Again.")
                        
                    money=int(input("Enter the Amount to be Sent:"))
                    amch= "select Amount from AMDB where Account_No=('{}')". format(account_de)
                    cs.execute(amch)
                    fetch_amount=cs.fetchone()
                    for op in list(fetch_amount):
                        curr=int(op)
                    if curr<money:
                        print("Your Account do not have sufficient money in order to send the given Amount.")
                    else:
                        print("Processing request,Please wait... ")
                        email_id= "AMDBANKVERIFY@gmail.com"
                        password= "ipprojectop"
                        message= MIMEMultipart()
                        message["from"] = sender_name
                        message["to"] = username
                        message["subject"] = subs

                        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login(email_id,password)
                            smtp.send_message(message)
                    
                        print("An OTP has been sent to your registered Email.Please enter the OTP for verification")
                        input_OTPs=input("Please enter the OTP:")
                        if OTPs==input_OTPs:
                            print("Sending request,Please wait... ")
                            acc_query="select email_id from amdb where Account_No=({})". format(acc_no)
                            cs.execute(acc_query)
                            ac=cs.fetchone()
                            for em in ac:
                                email=em
                            
                            fname_query="select fname from amdb where Account_No=({})". format(acc_no)
                            cs.execute(fname_query)
                            name=cs.fetchone()
                            for f in name:
                                fname=f

                            lname_query="select lname from amdb where Account_No=({})". format(acc_no)
                            cs.execute(lname_query)
                            namel=cs.fetchone()
                            for l in namel:
                                lname=l
                            q="update amdb set Amount=Amount - {} where Account_No=('{}')". format(money,account_de)
                            cs.execute(q)
                            updatedA="select Amount from amdb where Account_No={}". format(account_de)
                            cs.execute(updatedA)
                            updatbal=cs.fetchone()
                            for i in updatbal:
                                Amount_Final=i
                            statement1="insert into statement(DateOfTransaction,Account_No,Transac_Desc,Debit,Balance) values(NOW(),{},'{}',{},{})". format(account_de,desc,money,Amount_Final)
                            cs.execute(statement1) 
                            
                            q2="update amdb set Amount=Amount + {} where Account_No=('{}')". format(money,acc_no)
                            cs.execute(q2)
                            updatedAC="select Amount from amdb where Account_No={}". format(acc_no)
                            cs.execute(updatedAC)
                            updatbalance=cs.fetchone()
                            for i in updatbalance:
                                Amount_Credit=i
                            statement2="insert into statement(DateOfTransaction,Account_No,Transac_Desc,Credit,Balance) values(NOW(),{},'{}',{},{})". format(acc_no,desc,money,Amount_Credit)
                            cs.execute(statement2)
                            Amount_print=int(Amount_Credit)

                            subJect="Dear " + str(fname) + ' ' + str(lname) + ',' + "An amount of INR " + str('{:,}'.format(money)) + str('.00') + " has been CREDITED to your AMD Bank Account on " + str(datetime.today())[0:11] + ".Total Avail.bal INR " + str('{:,}'.format(Amount_print)) + str('.00')
                            email_id= "AMDBANKVERIFY@gmail.com"
                            password= "ipprojectop"
                            message= MIMEMultipart()
                            message["from"] = sender_name
                            message["to"] = email
                            message["subject"] = subJect

                            with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                                smtp.ehlo()
                                smtp.starttls()
                                smtp.login(email_id,password)
                                smtp.send_message(message)
                            print() 
                            print("----> TRANSACTION SUCCESSFUL <-----.")
                        else:
                            print("OTP entered is wrong.Transaction Failed")
                            
            elif choice3==2:
                print('''OPTIONS :-
        1. View Account Statement
        2. Exit ''' )
                print()
    
                c=int(input("Enter the option which you want to perform:"))
                print()

                DOT=[]
                s1="select DateofTransaction from statement where Account_No={}". format(account_in)
                cs.execute(s1)
                d1=cs.fetchall()
                for dot in d1:
                    DOT.append(str(dot[-1]))
                Accounts=[]
                s2="select Account_No from statement where Account_No={}". format(account_in)
                cs.execute(s2)
                d2=cs.fetchall()
                for acc in d2:
                    Accounts.append(str(acc[-1]))

                Transac_desc=[]
                s3="select Transac_Desc from statement where Account_No={}". format(account_in)
                cs.execute(s3)
                d3=cs.fetchall()
                for desc in d3:
                    Transac_desc.append(str(desc[-1]))

                Withdrawls=[]
                s4="select IFNULL(Withdrawls,'') as Withdrawls from statement where Account_No={}". format(account_in)
                cs.execute(s4)
                d4=cs.fetchall()
                for withdraw in d4:
                    Withdrawls.append(str(withdraw[-1]))

                Deposits=[]
                s5="select IFNULL(Deposits,'') as Deposits from statement where Account_No={}". format(account_in)
                cs.execute(s5)
                d5=cs.fetchall()
                for dep in d5:
                    Deposits.append(str(dep[-1]))

                Credit=[]
                s6="select IFNULL(Credit,'') as Credit from statement where Account_No={}". format(account_in)
                cs.execute(s6)
                d6=cs.fetchall()
                for cre in d6:
                    Credit.append(str(cre[-1]))

                Debit=[]
                s7="select IFNULL(Debit,'') as Debit from statement where Account_No={}". format(account_in)
                cs.execute(s7)
                d7=cs.fetchall()
                for deb in d7:
                    Debit.append(str(deb[-1]))

                Balance=[]
                s8="select Balance from statement where Account_No={}". format(account_in)
                cs.execute(s8)
                d8=cs.fetchall()
                for bal in d8:
                    Balance.append(str(bal[-1]))

                dt={'DateOfTransaction':DOT,'Account_No':Accounts,'Description':Transac_desc,'Withdrawls':Withdrawls,'Deposits':Deposits,'Credit':Credit,'Debit':Debit,'Balance':Balance}
                df=pd.DataFrame(dt)
                pd.options.display.width = 0

                if c==1:
                    print(df)
                    qry="select Amount from amdb where email_id=('{}')". format(username)
                    cs.execute(qry)
                    close_bal=cs.fetchone()
                    for i in close_bal:
                        bal=i
                    print("--------------------------------------------------------------------------------------------------")
                    print("                                                                       Closing Balance: Rs",bal)


                elif c==2:
                    exit 
                    print("Goodbye!")
                    
        elif choice2==5:
            digits2 = "0123456789"
            OTPd = ""
            res=''
            print("NOTE : DELETING YOUR ACCOUNT WILL LEAD TO PERMANENT LOSS OF DATA WHICH WOULD NOT BE RECOVERED.")
            print()
            surity=input("Are you sure you want to delete your Account?(Yes/No)")
            print()
            if surity=='Yes':
                p="select passwd from AMDB where email_id=('{}')". format(username)
                cs.execute(p)
                fetcha=cs.fetchall()
                repassword=input('Please Re-Enter your Password:')
                for x in fetcha:
                    if repassword not in x:
                        print("Incorrect Password")
                        res='F'
                    else:
                        res='T'
                        for d in range(4) : 
                            OTPd += digits2[math.floor(random.random() * 10)]
                        subd="The OTP sent for Verifcation so as Delete your AMD Bank account permanently is - " +  str(OTPd)
                        print("An OTP has been sent to your registered Email.Please enter the OTP for Verification")
                        print("Sending OTP,Please wait... ")
                        email_id= "AMDBANKVERIFY@gmail.com"
                        password= "ipprojectop"
                        message= MIMEMultipart()
                        message["from"] = sender_name
                        message["to"] = username
                        message["subject"] = subd
                        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login(email_id,password)
                            smtp.send_message(message)

                            
                            otpde=input("Please Enter OTP here:")
                            if OTPd==otpde:
                                des="delete from stats where email_id='{}'". format(username)
                                cs.execute(des)
                                dea="delete from amdb where email_id='{}'". format(username)
                                cs.execute(dea)
                                print("ACCOUNT DELETED SUCCESSFULLY.")
                            else:
                                print("OTP entered is Incorrect,Account Deletion Failed")

            elif surity=='No':
                print("Account Deletion Cancelled")
            else:
                print("Please Enter Yes Or No")
            
                



        
elif choice==2:
    o='@'
    print("###############REGISTER HERE###############")
        
    First_Name=input("Please Enter your First name:")
    Last_Name=input("Please Enter your Last name:")
    mobile_no= int(input("Please Enter your Mobile Number:"))
    cmobile_no=str(mobile_no)
    if len(cmobile_no)<10:
            print("PLease Enter a Valid Mobile Number")
    Address=input("Please Enter your address:")
    Amount=int(input("Enter the amount to be deposited for opening bank account(MIN:Rs500):"))
    if Amount <= 500:
        print("Please enter the Amount more than 500")
        Amount=int(input("Enter the amount to be deposited for opening bank account:"))
    else:
        pass
    email=input("Please enter your Email ID:")           
    while o not in email:
        print("The Email you entered is wrong.PLEASE ENTER VALID EMAIL ID")
        email=input("Please enter your Email ID:")
    else:
        pass
    password_f= input("Please Enter your password:")
    password_c= input("Please Re-Enter your password:")
    if password_f!=password_c:
        print("ERROR!!! PASSWORD DOES NOT MATCH,PLEASE TRY AGAIN")
    else:
        print("An OTP has been sent to your Email for verification.Please Enter the OTP for account verification")
        email_id= "AMDBANKVERIFY@gmail.com"
        password= "ipprojectop"
        message= MIMEMultipart()
        message["from"] = sender_name
        message["to"] = email
        message["subject"] = subject

        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_id,password)
            smtp.send_message(message)
        print("Email sent Successfully")

    otp_input=input("Please Enter the OTP Here:")
    if otp_input==OTP:
        query="insert into  AMDB(fname,lname,mobile_no,address,Amount,email_id,passwd) values('{}','{}',{},'{}',{},'{}','{}')". format(First_Name,Last_Name,mobile_no,Address,Amount,email,password_f)
        cs.execute(query)
        digitsb = "0123456789"
        Account_No = ""
        for d in range(11) : 
            Account_No += digitsb[math.floor(random.random() * 10)]
        acc_query="update amdb set Account_No={} where fname=('{}')". format(Account_No,First_Name)
        cs.execute(acc_query)
        print("Congratulations! Your Account has been created Successfully")
    else:
        print("OTP is not valid,please try again")

elif choice==3:
      print("Goodbye and have a nice day!")
      sys.exit()
print()
con.commit()
cs.close()
con.close()












