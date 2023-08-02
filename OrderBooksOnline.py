#create table library1(id int primary key auto_increment,name varchar(50),author varchar(50),price float,type varchar(50));

#cart table
#create table cart1(cartid int primary key auto_increment,name varchar(50),author varchar(50),price float,email varchar(50),quantity int);

#admin table username and password
#create table admin1(username varchar(50),password varchar(50));

#reglogin table
#create table reglogin1(id int primary key auto_increment,name varchar(50),email varchar(50),password varchar(50));

#ORDERS table
#create table orders1(oid int primary key auto_increment,book_name varchar(50),price float,email varchar(50),quantity int,ord_date varchar(50),total_amt float,id int);

import datetime
import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydtabase")
cur=conn.cursor(buffered= True)

#FETCHING DATA FROM DATABASE
def read_db(b_name):
    a=0
    cur.execute("select * from library1")
    for i in cur:
        if (i[1]==b_name):
            a+=1
            return True
    if (a==0):
        return False  

def read_db_table_cart(b_name):
    a=0
    cur.execute("select * from cart1 where email=%s",(u_emailid,))
    for i in cur:
        if (i[1]==b_name):
            a+=1
            return True
    if (a==0):
        return False
def user_books_in_cart():
    cur.execute("select * from cart1 where email=%s",(u_emailid,))
    return cur
         

def particular_row_data(b_name):
    cur.execute("select name,author,price,type from library1 where name=%s",(b_name,))
    return cur

"""
def particular_row_data_from_cart(id_to_order):
    cur.execute("select * from cart1 where id=%s",(id_to_order))
    return cur
"""

    
#DELETING DATA     cur.execute("delete from bms where account_no=%s",(acno,))       |  | 
def delete_data():
    display_all(0,0)   
    b_name=input("ENTER NAME OF BOOK To Remove It From Database:    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        cur.execute("delete from library1 where name=%s",(b_name,))
        conn.commit
        admin()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100))
        admin()

#heading for displaying all books
def heading():
    global gap
    gap=" "*3
    headline=f"{gap}{'BOOK NAME':18s}{gap}{'BOOK AUTHOR':20s}{gap}{'PRICE':10s}{gap}{'TYPE':15s}"
    print(("="*78).center(100))
    print(headline.center(100))
    print(("-"*78).center(100))

#UPDATING NAME
def update_name():
    b_name=input("ENTER NAME OF BOOK:    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        new_name=input("ENTER NEW NAME OF BOOK:    ".center(100)) 
        qry="update library1 set name=%s where name=%s"
        cstmr_info=(new_name,b_name)
        cur.execute(qry,cstmr_info)
        conn.commit()
        update()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100))
        update()

#UPDATING AUTHOR
def update_author():
    b_name=input("ENTER NAME OF BOOK:    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        new_name=input("Enter Name Of Author:    ".center(100)) 
        qry="update library1 set author=%s where name=%s"
        cstmr_info=(new_name,b_name)
        cur.execute(qry,cstmr_info)
        conn.commit()
        update()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100)) 
        update()

#UPDATING PRICE
def update_price():
    b_name=input("ENTER NAME OF BOOK:    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        new_name=int(input("ENTER PRICE OF BOOK:    ".center(100)))
        qry="update library1 set price=%s where name=%s"
        cstmr_info=(new_name,b_name)
        cur.execute(qry,cstmr_info)
        conn.commit()
        update()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100)) 
        update()

#UPDATING TYPE
def update_type():        
    b_name=input("ENTER NAME OF BOOK::    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        new_name=input("ENTER TYPE OF BOOK:    ".center(100))
        qry="update library1 set type=%s where name=%s"
        cstmr_info=(new_name,b_name)
        cur.execute(qry,cstmr_info)
        conn.commit()
        update()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100))
        update()



#DISPLAYING COMPLETE DATA
def display_all(a,b):
    heading()
    cur.execute("select * from library1")
    for row in cur:
        rec=f"{gap}{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}"
        print(rec.center(100))
    print(("-"*78).center(100))  
    if (a==1):
        admin() 
    else:
        pass

#DISPLAYING SINGLE DATA BASE ON ID2
def display_one():
    b_name=input("ENTER NAME OF BOOK:    ".center(100))
    prsnt=read_db(b_name)   
    if (prsnt==True):
        heading()
        cur.execute("select * from library1 where name=%s",(b_name,))
        for row in cur:
            rec=f"{gap}{row[1]:18s}{gap}{row[2]:20s}{gap}{row[3]:<10.2f}{gap}{row[4]:15s}"
            print(rec.center(100))
        print(("-"*78).center(100))            
        admin()
    else:
        print("ENTERED ID IS NOT IN DATABASE:   ".center(100))
        admin()


#updating Complete Row
def update_row():
    b_name=input("ENTER NAME OF BOOK    ".center(100))
    prsnt=read_db(b_name)
    if (prsnt==True):
        name=input("ENTER NAME OF BOOK:    ".center(100))
        author=input("ENTER NAME OF AUTHOR:    ".center(100))
        price=float(input("ENTER PRICE OF BOOK:    ".center(100)))
        kind=input("ENTER TYPE OF BOOK:    ".center(100))
        qry="update library1 set name=%s,author=%s,price=%s,type=%s where name=%s"      
        cstmr_info=(name,author,price,kind,b_name)
        cur.execute(qry,cstmr_info)
        conn.commit()
        update()
    elif (prsnt==False):
        print("ENTERED ID IS NOT IN DATABASE".center(100)) 
        update_row() 

#UPDATING DATA
def update():
    print("Select Your Option".center(100))
    display_all(0,0)
    choice=input(("1:UPDATE ENTIRE ROW          2:UPDATE SELECTED  ROW          3:EXIT".center(100)))
    if (choice=="1"):
        update_row()
    elif (choice=="2"):
        print("What U want To Update".center(100))
        choice=input("1:NAME     2:AUTHOR     3:PRICE     4:TYPE".center(100))
        if (choice=='1'):
            update_name()
        elif (choice=='2'):
            update_author()
        elif (choice=='3'):
            update_price()
        elif (choice=='4'):
            update_type()
    elif (choice=="3"):
        admin()
    else:
        print("Enter Valid Option")
        update()

#Adding Data In Database
def insert():
    name=input("Enter Name Of Book:    ".center(100))
    author=input("Enter Name Of Author:    ".center(100))
    price=float(input("Enter Price Of Book:    ".center(100)))
    kind=input("Enter Type of Book:    ".center(100))
    qry="insert into library1(name,author,price,type) values(%s,%s,%s,%s)"
    cstmr_info=(name,author,price,kind)
    cur.execute(qry,cstmr_info)
    conn.commit()
    print("*"*100)
    admin()


#ADMIN FN
def admin():
    gap=" "*3
    print("Enter your choice".center(100,"-"))
    optn=input(("1:INSERT     2:UPDATE     3:DELETE     4:DISPLAY     5:SHOW CUSTOMERS     6:ORDERS     7:EXIT\n".center(100)))   
    if (optn=="1"):
        insert()
    elif (optn=="2"):
        update()    
    elif (optn=="3"):
        delete_data() 
    elif (optn=="4"):
        print("Enter Your Choice".center(100)) 
        choice=input(("1:DISPLAY ALL      2:DISPLAY SINGLE DATA      3:EXIT".center(100)))      
        if (choice=="1"):
            display_all(1,0)
        elif (choice=="2"):
            display_one()
        elif (choice=="3"):
            lib_main()     
        else:
            print("Select Valid Option")   
            admin()
    elif (optn=="5"):
        print("YOUR CUSTOMERS ARE".center(100,"*"))  
        cur.execute("select * from reglogin1") 
        headline=f"{'ID':4s}{gap}{'NAME':18s}{gap}{'EMAIL':20s}"   
        print(headline.center(100)) 
        print(("-"*75).center(100))
        for row in cur:
            info=f"{row[0]:<4d}{gap}{row[1]:<18s}{gap}{row[2]:<20s}" 
            print(info.center(100))
        print(("-"*75).center(100))  
        admin()  
    elif (optn=="6"):
        pass
        print(("="*77).center(100))
        headline=f"{'BOOK NAME':<15s}{gap}{'PRICE':<5s}{gap}{'EMAILID':<15s}{gap}{'QTY':<3s}{'date':<10}{gap}{'AMOUNT':<6s}"
        print(headline.center(100))
        print(("-"*77).center(100))
        cur.execute("select * from orders1")
        for row in cur:
            info=f"{gap}{row[1]:<15s}{gap}{row[2]:<5.1f}{gap}{row[3]:<15s}{gap}{row[4]:<3d}{gap}{row[5]:<10s}{gap}{row[6]:<6.1f}"
            print(info.center(100))
        print(("-"*77).center(100))   
        admin() 
    elif (optn=="7"):
        lib_main()
            
###########CUSTOMER PART############
def registration():
    while True:
        a=int()
        u_name=input('ENTER YOUR NAME: '.center(100)).upper()
        for i in u_name:
            if (65<=ord(i)<=100 or 97<=ord(i)<=122):
                a+=1
        if (a==len(u_name)):
            break
            print("\n")  
        else:
            print('Enter valid name: \n'.center(100))
    while True:
        EMAIL=0
        u_email=input('ENTER YOUR EMAIL ID: '.center(100))
        if u_email.endswith('@gmail.com'): 
            cur.execute("select * from reglogin1")
            for data in cur:
                if (u_email in data):
                    print("\nEntered Email id Is Already Regisered Please Try With Diffrent Email Id:  \n".center(100))
                    EMAIL+=1
        else:
            print('Enter valid Email id: e'.center(100))     
        if EMAIL==0:
            break
            print("\n")
    while True:
        A,a,n,s=int(),int(),int(),int()       
        print('\nYour password must have at least one upper case One lower case one special case character and at least one integer value')
        u_password=input('CREATE YOUR PASSWORD: '.center(100))
        for i in u_password:
            if (65<=ord(i)<=100):
                A+=1
            elif (97<=ord(i)<=122):
                a+=1
            elif (48<=ord(i)<=57):
                n+=1
            elif (32<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126):
                s+=1
        if (A>=1 and a>=1 and n>=1 and s>=1):
            break
            print("\n")
        else:
            print('enter valid password:'.center(100))
    while True:
        u_contact=input('ENTER YOUR CONTACT NUMBER: '.center(100))
        if (len(u_contact)==10):
            print('REGISTRATION COMPLETE'.center(100,"*"))
            break
            print("\n")
        else:
            print('Please enter valid contact number:'.center(100))
    qry="insert into reglogin1(name,email,password) values(%s,%s,%s)" 
    data=[u_name,u_email,u_password]   
    cur.execute(qry,data)
    conn.commit()
    customer()
#customer orders
def place_order():
    print("BOOKS IN YOUR CART ARE".center(100))
    headline=f"{'BOOK NAME':18s}{gap}{'BOOK AUTHOR':20s}{gap}{'PRICE':10s}{gap}{'EMAILID':15s}{gap}{'QUANTITY':8s}"
    print(("="*90).center(100))
    print(headline.center(100))
    print(("-"*90).center(100))
    cur.execute("select * from cart1 where email=%s",(u_emailid,))
    total_amount=0
    for row_data in cur:
        info=f"{row_data[1]:18s}{gap}{row_data[2]:20s}{gap}{row_data[3]:<10.1f}{gap}{row_data[4]:15s}{gap}{row_data[5]:8d}"

        total_amount=total_amount+(int(row_data[3])*int(row_data[5]))
        print(info.center(100))
    print(("-"*90).center(100))
    print("TOTAL AMOUNT OF YOUR ORDER IS RS".center(100))
    print(str(total_amount).center(100))
    confirm_order=input("1:COMPLETE PAYMENT         2:EXIT".center(100))
    o_date=datetime.datetime.now()
    o_date=(o_date.strftime("%x"))
    if (confirm_order=="1"):
        print("PAYMENT SUCCESSFUL".center(100))
        
        cart_books=user_books_in_cart()
        for m in cart_books:
            qry="insert into orders1(book_name,price,email,quantity,ord_date,total_amt) values(%s,%s,%s,%s,%s,%s)"
            ord_details=(m[1],m[3],m[4],m[5],str(o_date),total_amount)
            cur.execute(qry,ord_details)        
        cur.execute("delete from cart1 where email=%s",(u_emailid,))    
        conn.commit()
        add_to_cart()
    elif (confirm_order=="2"):
        pass    
    else:
        print("SELECT VALID OPTION".center(100))
        place_order()

##CART
def cart():
    print("BOOKS IN YOUR CART ARE".center(100))
    headline=f"{gap}{'BOOK NAME':18s}{gap}{'BOOK AUTHOR':20s}{gap}{'PRICE':10s}{gap}{'EMAILID':15s}{gap}{'QUANTITY':8s}"
    print(("="*90).center(100))
    print(headline.center(100))
    print(("-"*90).center(100))#cur.execute("select * from bms where account_no=%s",(search,)) 
    cur.execute("select * from cart1 where email=%s",(u_emailid,))
    for row_data in cur:
        info=f"{gap}{row_data[1]:<18s}{gap}{row_data[2]:<20s}{gap}{row_data[3]:<10.1f}{gap}{row_data[4]:<15s}{gap}{row_data[5]:<8d}"
        print(info.center(100))
    print(("-"*90).center(100))
    print("ENTER YOUR CHOICE".center(100))
    choice=input("1:REMOVE ITEMS FROM CART          2:GO TO PAYMENT PAGE          3:CHANGE QUANTITY          4:EXIT".center(100))
    if (choice=="1"):
        b_name=input("ENTER NAME OF PRODUCT YOU WANT TO REMOVE".center(100))
        prsnt=read_db_table_cart(b_name)
        if (prsnt==True):
            cur.execute("delete from cart1 where name=%s",(b_name,))
            conn.commit()
            print("BOOK REMOVE FROM CART SUCCESSFULLY".center(100))
            cart()
        else:
            print("THIS BOOK IS NOT PRESENT IN YOUR CART".center(100))
            cart()
    elif (choice=="2"):
        place_order()
    elif (choice=="3"):
        b_name=input("ENTER NAME OF YOUR BOOK".center(100))
        prsnt=read_db_table_cart(b_name)
        if (prsnt==True):
            n=int(input("ENTER YOUR QUANTITY".center(100)))
            cur.execute("update cart1 set quantity=%s where name=%s",(n,b_name))
            conn.commit()
            print("CART UPDATED  SUCCESSFULLY".center(100))
            cart()
        else:
            print("ENTERED BOOK IS NOT IN YOUR CART".center(100)) 
            cart()   
    elif (choice=="4"):
        add_to_cart()
    else:
        print("ENTER VALID CHOICE".center(100)) 
        cart()     

#ADDINMG BOOKS TO CART
def add_to_cart():
    print("*"*100)
    display_all(0,0)
    print("ENTER YOUR CHOICE".center(100))
    choice=input("1:ORDER BOOK         2:GO TO CART         3:EXIT".center(100))
    if (choice=="1"):
        b_name=input("ENTER NAME OF A BOOK TO PLACE ORDER".center(100))
        prsnt=read_db(b_name)
        if (prsnt==True):
            n=input("HOW MANY COPIES U WANT TO ORDER".center(100))
            row_data= particular_row_data(b_name)
            for info in row_data:
                qry="insert into cart1(name,author,price,email,quantity) values(%s,%s,%s,%s,%s)"
                data=(info[0],info[1],info[2],u_emailid,n)
                cur.execute(qry,data)
                conn.commit()
                print("YOUR BOOKS ARE ADDED TO CART SUCCESSFULLY".center(100))
                break
            print("ENTER YOUR CHOICE".center(100)) 
            ans=input("1:SHOP MORE          2:PLACE ORDER          3:EXIT".center(100))
            if (ans=='1'):
                add_to_cart()
            elif (ans=='2'):
                cart()
            elif (ans=='3'):
                pass      
            else:
                print("ENTER VALID OPTION".center(100))
                add_to_cart() 
        else:
            print("BOOK YOU WANT IS NOT AVAILABLE ".center(100))
            add_to_cart()
    elif (choice=="2"):
        cart()
    elif (choice=="3"):    
        pass
    else:
        print("PLEASE ENTER VALID CHOICE".center(100))
        add_to_cart()

#USER LOGIN PART
def login():
    global a,u_emailid
    u_emailid=input('ENTER YOUR EMAIL ID:'.center(100))
    u_password=input('ENTER YOUR PASSWORD: '.center(100))
    cur.execute("select * from reglogin1")
    for info in cur:      
        if (u_emailid in info and u_password in info):
            print("LOGIN  SUCCESSFUL :)".center(100))
            add_to_cart()
            return
        elif (u_emailid in info and u_password not in info):
            getpass(u_emailid)
            return            
    if (a>=3):    
        print("YOU REACH YOUR MAXIMUM DAILY LIMIT:  ".center(100))
        return
    if (a==0):
        print("LOGIN UNSUCCESSFUL:  ".center(100))    
    if (a<3):
        a+=1
        print(str(4-a).center(100))     
        print("ATTEMPTS REMAINING:  ".center(100))
        login()

a=0
#RESETING AND GETTING PASSWORD
def getpass(u_emailid):
    choice=input("1:FORGOT PASSWORD     2:RESET PASSWORD     3:LOGIN   :".center(100))
    if (choice=='1'):
        forgot_pass(u_emailid)
        customer()
    elif (choice=='2'):
        reset_pass(u_emailid)
        customer()
    else:
        print("ENTER VALID CHOICE:  ".center(100))    
        customer()
def pass_validation(new_pass):
    A,a,n,s=int(),int(),int(),int()
    for i in new_pass:
        if (65<=ord(i)<=100):
            A+=1
        elif (97<=ord(i)<=122):
            a+=1
        elif (48<=ord(i)<=57):
            n+=1
        elif (32<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126):
            s+=1
    if (A>=1 and a>=1 and n>=1 and s>=1):
        return True
    else:
        print('ENTER VALID PASSWORD: '.center(100))
def forgot_pass(u_emailid):
    cur.execute("select * from reglogin1".center(100))
    for data in cur:
        if (u_emailid==data[2]):
            print(("YOUR PASSWORD IS:  ",data[3]).center(100))
def reset_pass(u_emailid):
    cur.execute("select * from reglogin1")
    for data in cur:
        if (u_emailid in data):
            new_pass=input("ENTER  NEW PASSWORD:  ".center(100))
            return_val=pass_validation(new_pass)
            if (return_val==True):
                if (new_pass==data[3]):
                    print("YOUR LATEST PASSWORD SHOULD NOT MATCH WITH LAST THREE PASSWORDS:  ".center(100))
                else:
                    print("PASSWORD RESET SUCCESSFULLY :)".center(100))
                    cur.execute("update reglogin1 set password=%s where email=%s",(new_pass,data[2],))
                    conn.commit()


def customer():
    print("1:REGISTRATION          2:LOGIN          3:EXIT".center(100))
    choice=input('ENTER YOUR CHOICE: '.center(100))
    if choice=='1':
        print("REGISTRATION".center(100,"-"))
        registration()
    elif choice=='2':
        print("YOU HAVE MAXIMUM 4 ATTEMPTS:".center(100))
        login()
    else:
        print("PLEASE ENTER VALID OPTION".center(100))
        customer()


def admin_login():
    admin_uername=input("ENTER YOUR USERNAME".center(100))
    admin_password=input("ENTER YOUR PASSWORD".center(100))
    cur.execute("select * from admin1")
    for info in cur:
        if admin_uername and admin_password in info:
            print("LOGIN SUCCESSFUL".center(100))
            admin()
        else:
            print("INVALID CREDENTIALS PLEASE TRY AGAIN".center(100)) 
            admin_login()   
            


#MAIN LIBRARY FN
def lib_main():
    optn=input(("1:ADMIN     2:CUSTOMER     3:EXIT".center(100)))    
    if (optn=="1"):
        admin_login()
    elif (optn=="2"):
        customer()  
    elif (optn=="3"):
        pass     
    else:
        print("ENTER VALID CHOICE".center(100))  
        lib_main()   
print("WELCOME".center(100,"*"))        
lib_main()