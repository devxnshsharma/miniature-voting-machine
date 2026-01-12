import pymysql
houselist=['Ekta','Pragati','Shakti','Shanti']

try:
    db= pymysql.connect(host ="localhost", user="root",
                    passwd="XXXXX", port=3306)
    c=db.cursor()
    #create a database 
    print("Welcome to TIS, VV Voting portal")
    print("**********************************")
    year=int(input("enter the current year in yyyy format"))
    c.execute("create database y%d;"%(year))
    print('backend created')
    c.execute("use y%d;"%(year))
    db.commit()
except pymysql.Error as e:
    print('NOTE:{}'.format(e))


#---------------functions for candidate menu-------------#        
def CandAdd(name):
    try:
        c.execute("use y%d;"%(year))
        cname=input("Candidate's name :").upper()
        qry="insert into %s values(\'%s\',0);"%(name,cname)
        ch= input('confirm insertion (y/n)?')
        if ch in 'yY':
            c.execute(qry)
            db.commit()
            print(" record inserted in ",name)
        else:
            print('Candidate not inserted...')
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))

def CandDel(name):
    try:
        c.execute("use y%d;"%(year))
        cname=input("Candidate's name to be removed :").upper()
        qry="select * from %s where cname=\'%s\';"%(name,cname)
        c.execute(qry)
        res=c.fetchall()
        if len(res) == 0:
            print("No matching record found.....")
        else:
            qry="delete from %s where cname=(\'%s\');"%(name,cname)
            ch= input('confirm deletion (y/n)? all vote records would be deleted')
            if ch in 'yY':
                c.execute(qry)
                db.commit()
                print(" record deleted from ",name)
            else:
                print("Record not deleted")
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))
    print()
   
def CandMod(name):
    try:
        c.execute("use y%d;"%(year))
        oldname=input("Candidate's old name :").upper()
        newname =input("Candidate's new name:").upper()
        qry="select * from %s where cname=\'%s\';"%(name,oldname)
        c.execute(qry)
        res=c.fetchall()
        if len(res) == 0:
            print("No matching record found.....")
        else:
            ch= input('confirm updation (y/n)?')
            if ch in 'yY':
                qry="update %s set cname=\'%s\' where cname=\'%s\';"%(name,newname,oldname)
                c.execute(qry)
                db.commit()
                print(" record updated successfully.. ",newname)
            else:
                print('Not modified')
           
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))
    print()
   
def CandDisp(name):
    try:
        c.execute("use y%d;"%(year))
        qry="select * from %s ;"%(name)
        c.execute(qry)
        res=c.fetchall()
        if len(res) == 0:
            print("Please enter candidates names first.....")
        else:
            print("\n\t____________________________________________")
            print("\tCandidate Names contending for  %s House"%(name))
            print("\t--------------------------------------------")
            for i in res:  
                print(i[0].upper())
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))

#---------------functions for House Main Menu-------------#
def CandMenu(name):
    while True:
        print("\n+++CANDIDATE MENU+++")
        print("1. Add candidate name")
        print("2. Delete candidate name")
        print("3. Modify candidate name")
        print("4. Display all candidates")
        print("5. go back to the previous menu")
        opt=int(input("Your choice?"))
        if opt==1:
            c=int(input('How many candidate names to be inserted?'))
            for i in range(c):
                        CandAdd(name)
        elif opt==2:
            CandDel(name)
        elif opt==3:
            CandMod(name)
        elif opt==4:
            CandDisp(name)
        elif opt==5:

            break
        else:
            continue

def House(name):
    try:
        qry="create table %s(cname varchar(20) primary key, votes int default 0); "%(name)
        c.execute("use y%d;"%(year))
        c.execute(qry)
        db.commit()
        print(name,"House table successfully created")
        print("Enter candidates names now before proceeding for voting")
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))
                       
def votecaste(name):
    try:
        c.execute("use y%d;"%(year))
        qry="select * from %s ;"%(name)
        c.execute(qry)
        res=c.fetchall()
        sno=1
        c1,c2,c3=-1,-1,-1
        if len(res) == 0:
            print("Please enter candidates names first.....")
        else:
            print("\n\t____________________________________________")
            print("\tCandidate Names contending for  %s House"%(name))
            print("\t--------------------------------------------")
            for i in res:  
                print(sno," ",i[0].upper())
                sno+=1
            c1=int(input('1st choice:'))
            c2=int(input('2nd choice:'))
            c3=int(input('3rd choice:'))
            try:
                print("you have chosen ",res[c1-1][0],res[c2-1][0],res[c3-1][0])
            except:
                print("invalid value entered")
                votecaste(name)
           
            ch=input('y/n?')
            if ch in 'yY':
               
                qry1="update %s set votes=votes+1 where cname in ('%s\');"%(name,res[c1-1][0])
                qry2="update %s set votes=votes+1 where cname in ('%s\');"%(name,res[c2-1][0])
                qry3="update %s set votes=votes+1 where cname in ('%s\');"%(name,res[c3-1][0])
                c.execute(qry1)
                c.execute(qry2)
                c.execute(qry3)
                db.commit()
                print("vote casted sucessfully...")
                HouseMenu(name)
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))

def votecount(name):
    try:
        c.execute("use y%d;"%(year))
        qry="select * from %s order by votes desc;"%(name)
        c.execute(qry)
        res=c.fetchall()
        if len(res) == 0:
            print("Please enter candidates names first.....")
        else:
            print("\n\t____________________________________________")
            print("\t\t  VOTES STATUS for  %s House"%(name))
            print("\t--------------------------------------------")
            print("\tCANDIDATE\t\tVOTES")
            for i in res:  
                print(f"\t{i[0].upper():<20}{i[1]:>6}")
    except pymysql.Error as e:
        print('NOTE:{}'.format(e))
#------------------------------------------------
def HouseMenu(name):
    choice ='y'
    while choice=='y':
        print()
        print("\n\t____________________")
        print("\t",name,"House Menu")
        print("\t---------------------")
        print("1. Create House backend for the first time")
        print("2. Manage Candidates list")
        print("3. Caste a Vote")
        print("4. Vote counting")
        print("5. Exit")
        val=int(input("\n Press 1-5 for choosing the option:"))
        if val==1:
            House(name)
        elif val==2:
            CandMenu(name)
        elif val==3:
            votecaste(name)
        elif val==4:
            votecount(name)
        elif val==5:
            print("going back to the main menu..")
            Main()
            break
        else:
            print("invalid choice entered..")            
#-----------------------------------------  
def Main():
    ch='y'
    name=''
   
    while ch=='y':
        print("\n....House List....")
        print("-------------------")
        for i in range(len(houselist)):
            print(i+1,". ",houselist[i])
        print(len(houselist)+1,".  EXIT")
        val=int(input("\n Choose the option:"))
        if val==1:
            name=houselist[val-1]
        elif val==2:
            name=houselist[val-1]
        elif val==3:
            name=houselist[val-1]
        elif val==4:
            name=houselist[val-1]
        elif val==5:
            print("exiting....")
            break
        else:
            print("invalid value entered")
            Main()
            break
        HouseMenu(name)
        ch=input("Continue(y/n)?")
        if ch not in 'yY':
            break
Main()
c.close()
db.close()
