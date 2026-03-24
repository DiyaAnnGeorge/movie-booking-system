import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="root",database="project")
cursor=con.cursor()
'''if con.is_connected:
    print ("connection successful")'''

#Creating Table
'''cursor.execute("create table MOVIES(Movieid int auto_increment primary key,MovieName varchar(20),Language varchar(10),Genre varchar(20),Cost int(3))")
cursor.execute("create table Booking (Slno int auto_increment primary key, Username varchar(10) not null,Movie varchar(20),Movieid int,Seat_no varchar(2),Time time,Date date,FOREIGN KEY (MovieId) REFERENCES MOVIES(MovieId))")
cursor.execute("CREATE TABLE Shows (Slno INT AUTO_INCREMENT PRIMARY KEY, MovieId INT,Time TIME,Date DATE,Screen varchar(1),FOREIGN KEY (MovieId) REFERENCES MOVIES(MovieId))")
'''
#welcome text
'''f=open('welcm.txt','w')
f.write("|WELCOME TO BOOKMYTICKET|")
f.close()'''

##################################################################################################################################################################################################################################

def movietable():
    data=cursor.fetchall()
    headers=["Movieid","Moviename","Language","Gernre","cost"]
    from tabulate import tabulate
    tab=tabulate(data,headers=headers,tablefmt='grid')
    print(tab)
    
def bookingtable():
    data=cursor.fetchall()
    headers=["Slno","Username","Movie","Seat_no", "Time","Date"]
    from tabulate import tabulate
    tab=tabulate(data,headers=headers,tablefmt='grid')
    print(tab)

def showtable():
    data=cursor.fetchall()
    headers=["Slno","MovieId","Time","Date","Screen"]
    from tabulate import tabulate
    tab=tabulate(data,headers=headers,tablefmt='grid')
    print(tab)

def main_menu():
    f=open('welcm.txt','r')
    text=f.read()
    f.close()
    print("-"*40)
    print(text)
    print("-"*40)
    print("      __________________      ")
    print("     |     1. ADMIN     |     ")
    print("     |__________________|     ")
    print("     |     2. USER      |     ")
    print("     |__________________|     ")
    print("     |     3.ABOUT US   |     ")
    print("     |__________________|     ")
    print("     |     4. EXIT      |     ")
    print("     |__________________|     ")
    print()
    ch=int(input ("ENTER YOUR CHOICE: "))
    print()
    if ch==1:
        #adminlogin
        for i in range(3):
            pswrd=input("Enter password ")
            
            if pswrd=='admin00':
                print("  |                                         |   ")
                print("  |                                         |   ")
                print("  |             WELCOME ADMIN               |   ")
                print("  |                                         |   ")
                print("  |                                         |   ")
                admin()
                break
            else:
                print('INCORRECT PASSWORD')
        else:
            print('No more attempts')
            main_menu()
         
    elif ch==2:
        login()
    elif ch==3:
        with open('about us.txt', 'r') as f:
            text=f.read()
        print(text)
        print("_"*160)
        print()
        main_menu()
    elif ch==4:
        exit()
    else:
        print("INVALID")
        main_menu()
        
        
def login():
    global username
    print("1.LOGIN")
    print("2.SIGN UP")
    ch=int(input("ENTER YOUR CHOICE: "))
    print()
    if ch==1:
        import csv
        for i in range(3):
            username = input("Enter username: ")
            password = input("Enter password: ")
            f=open("user.csv",'r')
            row=csv.reader(f)
            for e in row:
                if e[0]==username and e[1]==password:
                    print("  |                                         |   ")
                    print("  |                LOGGED IN                |   ")
                    print("  |                                         |   ")
                    f.close()
                    user()
                    break
            else:
                print("Incorrect username or password.")
        else:
            main_menu()
            
    elif ch==2:
        import csv
        username=input ("Enter username: ")
        f=open('user.csv','r')
        row=csv.reader(f)
        for i in row:
            if i[0]==username:
                print()
                print("USERNAME ALREADY EXIST")
                print()
                main_menu()
                break
        
        else:
            password=input("Enter password: ")
            re=input("Renter password: ")
            if re==password:
                data=[username,password]
                f=open('user.csv','a',newline='')
                writer=csv.writer(f)
                writer.writerow(data)
                print("   |                                   |    ")
                print("   |   YOUR ACCOUNT HAS BEEN CREATED   |    ")
                print("   |                                   |    ")
            else:
                print("Re-entered password is incorrect")
                main_menu()
                
        f.close()
        user()
    else:
        print("INVALID CHOICE")
        main_menu()
        
#user functions    
        
def user():
    print()
    print("1.SEARCH MOVIES")
    print("2.BOOK TICKET")
    print("3.CANCEL TICKET")
    print("4.UPDATE TICKET")
    print("5.GO TO MAIN MENU")
    print()
    ch=int (input ("Enter your choice: "))
    print()
    if ch==1:
        search()
    elif ch==2:
        book_ticket()
    elif ch==3:
        delete_ticket()
    elif ch==4:
        update_ticket()
    elif ch==5:
        print("Would you like to give a feedback y/n")
        choice=input("Enter your choice: ")
        import csv
        if choice=='y' or choice=='Y':
            feedback=input("Enter your feedback: ")
            data=[username,feedback]
            f=open('feedback.csv','a',newline='')
            writer=csv.writer(f)
            writer.writerow(data)
            f.close()
            print()
            print("|  THANK YOU FOR YOUR FEEDBACK  |")
            print()
            main_menu()
        if choice=='n' or choice=='N':
            main_menu()
    else:
        print("INVALID CHOICE")
        user()
        


def search():
    print()
    print("1.VIEW ALL MOVIES")
    print("2.SEARCH BY LANGUAGE")
    print("3.SEARCH BY GENRE")
    print("4.Back to menu")
    print()
    s=int(input ("Enter your choice: "))
    print()
    if s==1:
        from PIL import Image
        img=Image.open(r"C:\Users\User\Python 11th and 12th\movies.jpg")
        img.show()
        cursor.execute("select * from movies")
        movietable()
        search()
        
    elif s==2:
        cursor.execute("select distinct language from movies")
        data=cursor.fetchall()
        headers=["Language"]
        from tabulate import tabulate
        tab=tabulate(data,headers=headers,tablefmt='grid')
        print(tab)
        l=input ("Enter language: ")
        query=("select * from movies where language =%s")
        val=(l,)
        cursor.execute(query,val)
        movietable()
        search()
            
    elif s==3:
        cursor.execute("select distinct genre from movies")
        data=cursor.fetchall()
        headers=["Gernre"]
        from tabulate import tabulate
        tab=tabulate(data,headers=headers,tablefmt='grid')
        print(tab)
        l=input ("Enter genre: ")
        query=("select * from movies where genre =%s")
        val=(l,)
        cursor.execute(query,val)
        movietable()
        search()
    elif s==4:
        user()
    else:
        print("invalid choice")
        user()
  
    
def book_ticket():
    from PIL import Image
    img=Image.open(r"C:\Users\User\Python 11th and 12th\movies.jpg")
    img.show()
    movie=None
    cursor.execute("select * from movies")
    movietable()
    mid=input ("Enter movieid: ")
    q="select * from movies where movieid=%s"
    val=(mid,)
    cursor.execute(q,val)
    row=cursor.fetchall()
    for i in row:
        movie=i[1]
    q="select * from shows where movieid=%s "
    val=(mid,)
    cursor.execute(q,val)
    showtable()
    
    n=int (input("Enter number of tickets: "))
    q="select * from shows where movieid=%s "
    val=(mid,)
    cursor.execute(q,val)
    row=cursor.fetchall()
    s=int(input ("Enter slno"))
    for i in range (n):
        for i in row:
            if i[0]==s:
                time=i[2]
                date=i[3]
    
    #DISPLAY SEATS
    
        from matplotlib import pyplot as plt
        for i in range(6):
            i=i+1
            y=['A','B','C','D','E','F']
            x=[i,i,i,i,i,i]
            plt.scatter(x,y,color='blue')
        plt.show()
        
        while True:    #checking if seat is already booked
            seat=input ("Enter seat number: ")
            cursor.execute("select * from booking")
            data=cursor.fetchall()
            for i in data:
                if seat==i[4] and movie==i[2] and time==i[5] and date==i[6]:
                    print("Seat already booked")
                    break
                    
            else:
                query="insert into booking (username,movie,movieid,seat_no,time,date)value(%s,%s,%s,%s,%s,%s)"
                val=(username,movie,mid,seat,time,date)
                cursor.execute(query,val)
                con.commit()
                break
            
    q="select slno,username,movie,seat_no,time,date from booking where username=%s"
    v=(username,)
    cursor.execute(q,v)
    bookingtable()
    user()
    

                 
def delete_ticket():
    query="select slno,username,movie,seat_no,time,date from booking where username=%s"
    val=(username,)
    cursor.execute(query,val)
    bookingtable()
    n=int(input("How many tickets would you like to cancel: "))
    for i in range(n):
        s=input ("Enter Slno: ")
        val=(username,s)
        query="delete from booking where username=%s and Slno=%s"
        cursor.execute(query,val)
        con.commit()
    query="select slno,username,movie,seat_no,time,date from booking where username=%s"
    val=(username,)
    cursor.execute(query,val)
    bookingtable()
    user()

        
def update_ticket():
    print("1. CHANGE SEAT NO.")
    print("2. CHANGE SHOW TIME")
    ch = int(input("Enter your choice: "))
    query = "select slno,username,movie,seat_no,time,date from booking where username=%s"
    val = (username,)
    cursor.execute(query, val)
    bookingtable()
    movie = None  
    time = None   
    date = None
    if ch == 1:
        n = int(input("Enter the row you want to change: "))
        q = "select * from booking where Slno=%s"
        val=(n,)
        cursor.execute(q,val)
        row = cursor.fetchall()
        for i in row:
            movie = i[2]
            time = i[5]
            date = i[6]
        from matplotlib import pyplot as plt
        for i in range(6):
            i=i+1
            y=['A','B','C','D','E','F']
            x=[i,i,i,i,i,i]
            plt.scatter(x,y,color='blue')
        plt.show()
    
        while True:
            seat=input ("ENTER SEAT NUMBER: ")
            cursor.execute("select * from booking")
            data=cursor.fetchall()
            for i in data:
                if seat==i[4] and movie==i[2] and time==i[5] and date==i[6]:
                    print("SEAT ALREADY BOOKED")
                    break

            else:
                v=(seat,n)
                q="update booking set seat_no=%s where slno=%s"
                cursor.execute(q,v)
                con.commit()
                break
        query = "select slno,username,movie,seat_no,time,date from booking where username=%s"
        val = (username,)
        cursor.execute(query, val)
        bookingtable()
        print(  "  YOUR SEAT HAS BEEN CHANGED  "  )
        user()
        
    elif ch==2:
        n = int(input("Enter the row you want to change"))
        query = "select * from booking where username=%s"
        val = (username,)
        cursor.execute(query, val)
        row=cursor.fetchall()
        for i in row:
            mid=i[3]
            movie=i[2]
        q="select * from shows where movieid=%s"
        val=(mid,)
        cursor.execute(q,val)
        showtable()
        q="select * from shows where movieid=%s "
        val=(mid,)
        cursor.execute(q,val)
        row=cursor.fetchall()
        s=int(input ("Enter slno"))
        for i in row:
            if i[0]==s:
                time=i[2]
                date=i[3]
        from matplotlib import pyplot as plt
        for i in range(6):
            i=i+1
            y=['A','B','C','D','E','F']
            x=[i,i,i,i,i,i]
            plt.scatter(x,y,color='blue')
        plt.show()
        
        while True:
            seat=input ("ENTER SEAT NUMBER: ")
            cursor.execute("select * from booking")
            data=cursor.fetchall()
            for i in data:
                if seat==i[4] and movie==i[2] and time==i[5] and date==i[6]:
                    print("SEAT ALREADY BOOKED")
                    break

            else:
                v=(seat,time,date,n)
                q="update booking set seat_no=%s,time=%s,date=%s where slno=%s"
                cursor.execute(q,v)
                con.commit()
                break
        query = "select slno,username,movie,seat_no,time,date from booking where username=%s"
        val = (username,)
        cursor.execute(query, val)
        bookingtable()
        print(  "  SHOW TIME HAS BEEN CHANGED  "  )
        user()
    
        
    

#admin functions

def admin():
    print()
    print("1.VIEW BOOKING DETAILS")
    print("2.VIEW MOVIE DETAILS")
    print("3.ADD MOVIES")
    print("4.DELETE MOVIES")
    print("5.UPDATE MOVIE DETAILS")
    print("6.ADD AND DELETE SHOWS")
    print("7.VIEW FEEDBACKS")
    print("8.Log out")
    print()
    ch=int(input ("Enter your choice: "))
    print()
    if ch==1:
        cursor.execute("select slno,username,movie,seat_no,time,date from booking")
        bookingtable()
        admin()
    elif ch==2:
        cursor.execute("select * from movies")
        movietable()
        admin()
    elif ch==3:
        cursor.execute("select * from movies")
        movietable()
        movie=input("Enter movie name: ")
        lan=input("Enter language: ")
        gen=input("Enter genre: ")
        cost=int(input("Enter cost:"))
        query="insert into movies (moviename,language,genre,cost)value(%s,%s,%s,%s)"
        val=(movie,lan,gen,cost)
        cursor.execute(query,val)
        con.commit()
        cursor.execute("select * from movies")
        movietable()

        cursor.execute("SELECT LAST_INSERT_ID()")
        mid = cursor.fetchone()[0]
        n = int(input("Enter the number of showtimes: "))
        cursor.execute("select * from shows")
        row=cursor.fetchall()
        for i in range(n):
            while True:
                from datetime import datetime
                current=datetime.now()
                while True:
                    try:
                        date =input ("Enter date ")
                        date = datetime.strptime(date, "%Y-%m-%d")
                        if date>=current:
                            break
                        else:
                            print("Please enter a future date")
                    except ValueError:
                        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                time = input("Enter showtime (HH:MM) ")
                screen =input ("Enter screen: ")
                
                query = "INSERT INTO shows (movieid, time, date,screen) VALUES (%s, %s, %s, %s)"
                values = (mid, time, date,screen)
                cursor.execute(query,values)
                con.commit()
                break
                        
        q="select * from shows where movieid=%s"
        val=(mid,)
        cursor.execute(q,val)
        showtable()
        admin()
        
    elif ch==4:
        cursor.execute("select * from movies")
        movietable()
        mid=input("Enter movieid")
        query="delete from shows where movieid= %s"
        val=(mid,)
        cursor.execute(query,val)
        con.commit()
        query="delete from booking where movieid= %s"
        val=(mid,)
        cursor.execute(query,val)
        con.commit()
        q="delete from movies where movieid=%s"
        val=(mid,)
        cursor.execute(q,val)
        con.commit()
        print()
        print("   DELETION SUCCESSFUL   ")
        admin()
    elif ch==5:
      update_movie()
    elif ch==6:
        shows()
    elif ch==7:
        import csv
        f=open('feedback.csv','r')
        csv.reader(f)
        for i in f:
            print(i)
        admin()
    elif ch==8:
        main_menu()
    else:
        print("INVALID")
        admin()
        
def update_movie():
    
    print("1.UPDATE MOVIE NAME")
    print("2.UPDATE LANGIAGE")
    print("3.UPDATE GENRE")
    print("4.UPDATE SHOW TIME")
    print("5.BACK TO ADMIN MENU")
    print()
    ch=int (input ("Enter your choice: "))
    if ch==1:
        cursor.execute ("select * from movies")
        movietable()
        m=input ("Enter movieid: ")
        n=input ("Enter updated movie name: ")
        query="update movies set moviename=%s where movieid=%s"
        val=(n,m)
        cursor.execute(query ,val)
        con.commit()
        cursor.execute ("select * from movies")
        movietable()
        update_movie()
    elif ch==2:
        cursor.execute ("select * from movies")
        movietable()
        m=input ("Enter movieid: ")
        l=input ("Enter updated language: ")
        query="update movies set language=%s where movieid=%s"
        val=(l,m)
        cursor.execute(query ,val)
        con.commit()
        cursor.execute ("select * from movies")
        movietable()
        update_movie()
    elif ch==3:
        cursor.execute ("select * from movies")
        movietable()
        m=input ("Enter movieid: ")
        g=input ("Enter updated genre: ")
        query="update movies set genre=%s where movieid=%s"
        val=(g,m)
        cursor.execute(query ,val)
        con.commit()
        cursor.execute ("select * from movies")
        movietable()
        update_movie()
    elif ch==4:
        cursor.execute ("select * from movies")
        movietable()
        m=input ("Enter movieid: ")
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        n=int(input("Enter the row you want to change: "))
        t=input("Enter time: ")
        from datetime import datetime
        current=datetime.now()
        while True:
            try:
                date =input ("Enter date ")
                date = datetime.strptime(date, "%Y-%m-%d")
                if date>=current:
                    break
                else:
                    print("Please enter a future date")
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        screen=input("Enter screen: ")
        q="update shows set time=%s,date=%s,screen=%s where slno=%s"
        val=(t,date,screen,n)
        cursor.execute(q,val)
        con.commit()
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        update_movie()
    elif ch==5:
        admin()
    else:
        print("invalid choice")
        update_movie()
        
def shows():
    print()
    print("1.ADD SHOWS ")
    print("2.DELETE SHOWS")
    print("3.BACK TO ADMIN")
    ch=int( input("Enter your choice:"))
    print()
    if ch==1:
        cursor.execute ("select * from movies")
        movietable()
        m=input("Enter movieid")
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        t=input("Enter time ")
        from datetime import datetime
        current=datetime.now()
        while True:
            try:
                date =input ("Enter date ")
                date = datetime.strptime(date, "%Y-%m-%d")
                if date>=current:
                    break
                else:
                    print("Please enter a future date")
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        screen=input ("Enter screen ")
        q="insert into shows( movieid,time,date,screen) values(%s,%s,%s,%s)"
        val=(m,t,date,screen)
        cursor.execute(q,val)
        con.commit()
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        shows()
    elif ch==2:
        cursor.execute ("select * from movies")
        movietable()
        m=input("Enter movieid")
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        n=int (input ("enter slno"))
        q=f"delete from shows where slno= %s"
        val=(n,)
        cursor.execute(q,val)
        con.commit()
        q="select * from shows where movieid=%s"
        val=(m,)
        cursor.execute(q,val)
        showtable()
        shows()
    elif ch==3:
        admin()
    else:
        print("Invalid choice")
        shows()
        

     
        
#################################################################################################################################################
from PIL import Image
img=Image.open(r"C:\Users\User\Python 11th and 12th\image.png")
img.show()
main_menu() 






