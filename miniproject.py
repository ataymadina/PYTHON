from pickle import load,dump
from os import remove,rename
import os
import random
import time
print
print
print
print
print
print ("\t \t \t WELCOME TO A & A LIBRARY \t \t \t")
print
print
print
print
print
print
print ("\t \t \t \t \t \t \t PROJECT DONE BY:")
print
print
print ("\t \t \t \t \t \t \......... ")
print
print ("\t \t \t \t \t \t \t……….. ")
print
print
a=raw_input("PRESS ENTER TO CONTINUE:")
a=str(a)
if a.isalpha():
    pass
class book:
    def __init__(self,bno=" ",bname=" ",auname=" "):
        self.bno=bno
        self.bname=bname
        self.auname=auname   
    def create_book(self):
        print
        print ("\t\t\t Creating Book Record \t\t\t")
        print
        self.bno=raw_input("\t Enter Book Number:")
        print
        self.bname=raw_input("\t Enter Name of the Book:")
        print
        self.auname=raw_input("\t Enter Name of the Author:")
        print
        print
        print ("\t \t \t Book Created \t \t \t")
   
    def show_book(self):
        print
        print
        print ("\t \t Book Number:",self.bno)
        print
        print ("\t \t Book Name:",self.bname)
        print
        print ("\t \t Author Name:",self.auname)
        print
        print
    def modify_book(self):
        print
        print
        print ("\t \t Book No.: ",self.bno)
        print
        self.bname=raw_input("\t \t Enter New Book Name:")
        print
        self.auname=raw_input("\t \t Enter New Author Name:")
        print
        print
        print ("\t \t Book Modified")
        print
    def ret_bno(self):
        return (self.bno)
    def report_book(self):
        print (self.bno,self.bname,self.auname)
class student:
    def __init__(self,admno=" ",name=" ",stbno=" ",token=0):
        self.admno=admno
        self.name=name
        self.stbno=stbno
        self.token=token
    def createstud(self):
        print
        print ("\t \t \t Creating Student Record \t \t \t")
        print
        self.admno=raw_input("\t \t Enter Admission Number:")
        print
        self.name=raw_input("\t \t Enter Name of the Student:")
        self.stbno=" "
        self.token=0
        print
        print
        print ("\t \t \t Student Record Created \t \t \t")
        print
        print ("#"*70)
        print
    def showstud(self):
        print
        print
        print ("\t Admission No.:",self.admno)
        print
        print ("\t Name:",self.name)
        print
        print ("\t Stbno:",self.stbno)
        print
        print
    def displaystud(self):
        print
        print ("\t Admission Number of the Student is:",self.admno)
        print
        print ("\t Name of the Student is:",self.name)
        if (self.token==1):
            print ("\t Book Number is:",self.stbno)
    def modifystud(self):
        print
        print ("\t Admission No:",self.admno)
        print
        self.name=raw_input("\t New Student Name:")
        print
        print ("\t \t Student's Name Modified !!")
    def ret_admno(self):
        return self.admno
   
    def ret_stbno(self):
        return self.stbno
    def ret_token(self):
        return self.token
    def add_token(self):
        self.token=1
    def reset_token(self):
        self.token=0
    def get_stbno(self,t):
        self.stbno=t
    def reportstud(self):
        print (self.admno, self.name, self.token)
def writebook():
    ch="Y"
    fp=open("book1.dat","ab")
    while ch=="Y":
        bk.create_book()
        dump(bk,fp)
        print
        ch=raw_input("\t \t Do You Want to Continue<y/n>:")
        print
        print ("#"*70)
        print
        ch=ch.upper()
def writestudent():
    ch="Y"
    fp=open("student1.dat","ab")
    while ch=="Y":
        st.createstud()
        dump(st,fp)
        ch=raw_input("\t \t Do You Want to Continue <y/n>:")
        ch=ch.upper()
        print      
def display_alls():
		fin=open("student1.dat","rb")
		if not (fin):
			print ("\t \t File is Not Found..")
		else:
			try:
				while True:
					print
					st=load(fin)
					st.showstud()
			except EOFError:
				pass
			fin.close()
def display_allb():
    fin=open("book1.dat","rb")
    if not (fin):
        print
        print
        print ("Book File is Not Found..")
    else:
        try:
            while True:
                bk=load(fin)
                bk.show_book()
        except EOFError:
            pass
        fin.close()
def display_spb(no):
    flag=0
    fin=open("book1.dat","rb")
    try:
        while True:
            bk=load(fin)
            if(bk.ret_bno()==no):
                bk.show_book()
                flag=1
   
    except EOFError:
        pass
    fin.close()
    if flag==0:
        print
        print
        print ("\t \t \t \t BOOK NOT PRESENT..!!")
def display_sps(n):
    flag=0
    fin=open("student1.dat","rb")
    try:
        while True:
            st=load(fin)
            if(st.ret_admno()==n):
                st.showstud()
                flag=1
    except EOFError:
        pass
    fin.close()
    if flag==0:
        print
        print ("\t \t \t STUDENT NOT PRESENT..!!")
def modify_bookrecord():
    found=0
    print
    print
    print ("\t \t \t Modify Book")
    print
    print
    n=raw_input("\t \t Enter Book Number to be Modified:")
    print
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_bno()==n:
                print
                print ("\t \t \t Book Details")
                bk.show_book()
                print
                print("\t \t  Enter New Details")
                print
                print
                bk.modify_book()
                dump(bk,fout)
                found=1
            else:
                dump(bk,fout)
    except EOFError:
        pass
    if found==0:
        print ("\t \t \t \t Book Not Present")
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")
def modify_student_record():
    found=0
    print
    print ("\t \t \t Modify Student Record")
    print
    print
    n=raw_input("\t \t Enter Student's Admission Number to be Modified:")
    print
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_admno()==n:
                print
                print ("\t \t \t STUDENT DETAILS")
                st.showstud()
                print
                print ("\t \t \t Enter New Student Details:")
                st.modifystud()
                dump(st,fout)
                found=1
            else:
                dump(st,fout)
    except EOFError:
        pass
    if found==0:
        print ("\t \t \t \t STUDENT NOT PRESENT")
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
def del_stud():
    flag=0
    print
    print
    n=raw_input("\t \t Enter Admission to be Deleted:")
    print
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_admno()<n:
                dump(st,fout)
            else:
                flag=1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
    if flag==1:
        print
        print ("\t \t \t \t RECORD DELETED..!!")
    else:
        print
        print ("\t \t \t \t SORYY..!! RECORD DOES NOT EXIST..!!..")

def del_book():
    flag=0
    print
    print
    n=raw_input("\t \t Enter Book No to be Deleted:")
    print
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_bno()<n:
                dump(bk,fout)
            else:
                flag=1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")
    if flag==1:
        print ("\t \t \t Record Deleted")
    else:
        print ("\t \t \t SORRY..!! RECORD NOT PRESENT..")
def book_issue():
    sn=" "
    bn=" "
    found=0
    flag=0
    print
    print
    print ("\t \t \t BOOK ISSUE.. \t \t \t")
    print
    print
    sn=raw_input("\t \t Enter the Student's Admission Number:")
    print
    fin1=open("book1.dat","rb")
    fin2=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin2)
            if (st.ret_admno()==sn):
                st.showstud()
                found=1
                if st.ret_token()==0:
                    bn=raw_input("\t \t Enter Book Number:")
                    try:
                        while True:
                            bk=load(fin1)
                            if bk.ret_bno()==bn:
                                bk.show_book()
                                flag=1
                                st.add_token()
                                st.get_stbno(bk.ret_bno())
                                dump(st,fout)
                                os.system("cls")
                                print
                                print
                                print ("\t \t \t Book Issued Successfully \t \t \t")
                                print
                                print ("\t PLEASE NOTE : Write the current date in backside of            your book ")
                                print ("\t \t and submit within 15 days")
                                print
                                print ("\t \t Fine Rs.20 for each day after 15 days period..!!")
                                print
                               
                    except EOFError:
					
                        
