import sqlite3
from sqlite3 import Error
import time
import pandas as pd
import sys
import os
cls = lambda: os.system('cls')
con = sqlite3.connect('patient.db')
cur = con.cursor()


                              #creation of  Table

def patient(con):
    cur.execute("create table PATIENT(P_NAME varchar(15),DOB varchar(10),PID integer(5) primary key,DISEASE varchar(10),ARRIVAL_DATE varchar(10),DISCHARGE_DATE varchar(10),BLOOD_GROUP varchar(3),ADDRESS varchar(20),gender varchar(1),DID integer(5),NID integer(5))")
    con.commit()

def room(con):
    cur.execute("create table ROOM(R_COST integer(4),R_TYPE varchar(5),RID integer(5) primary key,PID integer(5) ,foreign key(PID) references PATIENT(PID))")
    con.commit()

def nurse(con):
    cur.execute("create table NURSE(NID integer(5) primary key,QUALIFICATION varchar(10),N_NAME varchar(15))")
    con.commit()

def medicine(con):
    cur.execute("create table MEDICINE(M_NAME varchar(10),M_COST float(5),MID integer(5) primary key)")
    con.commit()

def doctor(con):
    cur.execute("create table DOCTOR(DID integer(5) primary key,D_NAME varchar(15),EMAIL varchar(20),QUALIFICATION varchar(10))")
    con.commit()

def test(con):
    cur.execute("create table TEST(TID integer(5) primary key,T_COST float(5))")
    con.commit()

def relative(con):
    cur.execute("create table RELATIVE(R_NAME varchar(15),RELATION varchar(10),PHONE_NO integer(10),PID integer(5),foreign key(PID) references PATIENT(PID))")
    con.commit()

def phonenumber(con):
    cur.execute("create table PHONENUMBER(PID integer(5),PHONE_NUMBER integer(10),foreign key(PID) references PATIENT(PID))")
    con.commit()

def takes(con):
    cur.execute("create table TAKES(M_DATE varchar(10),QUANTITY integer(3),MID integer(5),PID integer(5),foreign key(MID) references MEDICINE(MID),foreign key(PID) references PATIENT(PID))")
    con.commit()
    
def had(con):
    cur.execute("create table HAD(TEST_DATE varchar(10),PID integer(5),TID integer(5),foreign key(PID) references PATIENT(PID),foreign key(TID) references TEST(TID))")
    con.commit()
    
def bill(con):
    cur.execute("create table BILL(BILL_ID integer(5) primary key,ROOM_COST integer(3),MCOST integer(3),TCOST integer(3),OTHER_CHARGE integer(3),BILL_DATE varchar(10),PID integer(5),foreign key(PID) references PATIENT(PID))")
    con.commit()       




                                  #insetion of Data

def ins_patient(con):
    n=input("enter Name :")
    d=input("enter DOB :")
    p=int(input("enter PID :"))
    ds=input("enter Disease :")
    ad=input("enter Arrival Date :")
    dd=input("enter Discharge Date :")
    bg=input("enter Blood Group :")
    add=input("enter Address :")
    gn=input("enter Gender :")
    did=int(input("enter DID :"))
    nid=int(input("enter NID :"))
    cur.execute("insert into PATIENT values(?,?,?,?,?,?,?,?,?,?,?)",(n,d,p,ds,ad,dd,bg,add,gn,did,nid))
    ins_phonenumber(con,p)
    print("Enter details of Relatives")
    ins_relative(con,p)
    print("Enter Details of Medicine Taken")
    ins_takes(con,p)
    print("Enter Details of Tests taken")
    ins_had(con,p)
    print("Enter room Details")
    ins_room(con,p)
    con.commit()
    c=input("Do you want to go to the main menu(Y/N) :")
    if(c=='y' or c=='Y'):
        cls()
        main_menu()
    else:
        sys.exit()
    

def ins_relative(con,p):
    n=input("Enter Relative's Name")
    r=input("Enter Relation with patient")
    pn=int(input("Enter Phone Number of Relative"))
    cur.execute("insert into relative values(?,?,?,?)",(n,r,pn,p))
    con.commit()
    
def ins_phonenumber(con,p):
   n=int(input("How many phone numbers does the patient have :"))
   pid=p
   for i in range(n):
       n=int(input("Enter phone number :"))
       cur.execute("insert into phonenumber values(?,?)",(pid,n))
       con.commit()

def ins_takes(con,p):
    md=input("Enter Date :")
    m=int(input("Enter MID :"))
    q=int(input("Enter Quantity :"))
    cur.execute("insert into takes values(?,?,?,?)",(md,q,m,p))
    con.commit()

def ins_had(con,p):
    d=input("Enter Date of test :")
    t=int(input("Enter TID :"))
    cur.execute("insert into had values(?,?,?)",(d,p,d))
    con.commit()

def ins_room(con,p):
    c=int(input("Enter Room Cost :"))
    t=input("Enter Room type :")
    r=int(input("Enter RID"))
    cur.execute("insert into room values(?,?,?,?)",(c,t,r,p))
    con.commit()

                                     #Displaying data
    
def display(con):
    print("1. Display all records ")
    print("2. Display specific record ")
    print("3. Go to Main Menu ")
    n=int(input("Enter your choice :"))
    if(n==1):
        cls()
        displayall(con)
    elif(n==2):
        cls()
        displayone(con)
    elif(n==3):
        cls()
        main_menu()
    else:
        print("Wrong input!")
        cls()
        display(con)

def displayall(con):
    cur.execute("select * from patient")
    records = cur.fetchall()
    print("Printing records")
    time.sleep(2)
    for row in records:
        print("\n")
        print("Name :",row[0])
        print("DOB :",row[1])
        print("PID :",row[2])
        print("Disease :",row[3])
        print("Arrival Date :",row[4])
        print("Discharge Date :",row[5])
        print("Blood group :",row[6])
        print("Address :",row[7])
        print("Gender :",row[8])
        print("\n")
    time.sleep(5)
    display(con)
    

def displayone(con):
    p=int(input("Enter PID of patient to display details :"))
    cur.execute("select * from patient where pid=?",(p,))
    row = cur.fetchall()
    print("Printing records")
    time.sleep(2)
    print("\n")
    print("Name :",row[0][0])
    print("DOB :",row[0][1])
    print("PID :",row[0][2])
    print("Disease :",row[0][3])
    print("Arrival Date :",row[0][4])
    print("Discharge Date :",row[0][5])
    print("Blood group :",row[0][6])
    print("Address :",row[0][7])
    print("Gender :",row[0][8])
    print("\n")
    time.sleep(5)
    display(con)
    
    
    
                                       #deleting records

def delrec(con):
    n=int(input("Enter PID to delete patients record"))
    cur.execute("delete from patient where PID= ?",(n,))
    cur.execute("delete from relative where PID= ?",(n,))
    cur.execute("delete from phonenumber where PID= ?",(n,))
    cur.execute("delete from takes where PID= ?",(n,))
    cur.execute("delete from had where PID= ?",(n,))
    cur.execute("delete from room where PID= ?",(n,))
    time.sleep(2)
    print("Records Deleted")
    con.commit()
    c=input("Do you want to go to the main menu(Y/N) :")
    if(c=='y' or c=='Y'):
        cls()
        main_menu()
    else:
        sys.exit()
    

                           #updating records
    
def update_patient(con):
    p=int(input("Enter PID to update record :"))
    cur.execute("delete from patient where pid=?",(p,))
    n=input("enter Name :")
    d=input("enter DOB :")
    ds=input("enter Disease :")
    ad=input("enter Arrival Date :")
    dd=input("enter Discharge Date :")
    bg=input("enter Blood Group :")
    add=input("enter Address :")
    gn=input("enter Gender :")
    did=int(input("enter DID :"))
    nid=int(input("enter NID :"))
    cur.execute("insert into PATIENT values(?,?,?,?,?,?,?,?,?,?,?)",(n,d,p,ds,ad,dd,bg,add,gn,did,nid))
    con.commit()
    time.sleep(2)
    print("Record updated..")
    c=input("Do you want to go to the main menu(Y/N) :")
    if(c=='y' or c=='Y'):
        cls()
        main_menu()
    else:
        sys.exit()


                            #generate bill
def genbill(con):
    pid=int(input("Enter PID :"))
    bid=int(input("Enter BID :"))
    cur.execute("select R_COST from room where pid= ?",(pid,))
    rcost=cur.fetchall()
    rcost=rcost[0][0]
    cur.execute("select m_cost from medicine where mid=(select mid from takes where pid=?)",(pid,))
    mc=cur.fetchall()
    cur.execute("select quantity from takes where pid=?",(pid,))
    qt=cur.fetchall()
    mcost=mc[0][0]*qt[0][0]
    cur.execute("select t_cost from test where tid=(select tid from had where pid=?)",(pid,))
    tcost=cur.fetchall()
    tcost=tcost[0][0]
    othercharge=int(input("Enter other charges :"))
    bd=input("Enter Billdate :")
    cur.execute("insert into bill values(?,?,?,?,?,?,?)",(rcost,mcost,bid,tcost,othercharge,bd,pid))
    time.sleep(2)
    print("Bill generated..")
    print("Bill Date : %d",bd)
    print("Room cost : %d",rcost)
    print("Medicine cost : %d",mcost)
    print("Test cost : %d ",tcost)
    print("Other Charges : %d",othercharge)
    print("\n\n")
    c=input("Do you want to go to the main menu(Y/N) :")
    if(c=='y' or c=='Y'):
        cls()
        main_menu()
    else:
        sys.exit()
    

def main_menu():
    print("             Main Menu")
    print("1. Create tables ")
    print("2. Insert Records ")
    print("3. Update Records ")
    print("4. Delete Records ")
    print("5. Display Records ")
    print("6. Generate Bill ")
    print("7. Exit ")
    n=int(input("Enter your choice :"))
    if(n==1):
        patient(con)
        room(con)
        nurse(con)
        medicine(con)
        doctor(con)
        test(con)
        relative(con)
        phonenumber(con)
        takes(con)
        had(con)
        bill(con)
        time.sleep(2)
        print("Tables Created..")
        c=input("Do you want to go to the main menu(Y/N) :")
        if(c=='y' or c=='Y'):
            main_menu()
        else:
            sys.exit()     
    elif(n==2):
        cls()
        ins_patient(con)
    elif(n==3):
        cls()
        update_patient(con)
    elif(n==4):
        cls()
        delrec(con)
    elif(n==5):
        cls()
        display(con)
    elif(n==6):
        cls()
        genbill(con)
    elif(n==7):
        sys.exit()
    else:
        print("Wrong input!")
        main_menu()
        
        
main_menu()

    
