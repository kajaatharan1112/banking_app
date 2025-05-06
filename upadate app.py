 # -----------funcations--------:98s-0
import datetime #-import date and time-
def date_time():
    return datetime.date.today()

def admin_acount_create():
    while(True):
        try:
            admin_name = str(input("Enter admin name="))
            admin_age=int(input("entertha admin age="))
        except ValueError:
            print("enter tha sutabil input")
            continue
        except TypeError:
            print("enter tha sutabil input")
            continue
        while(True):
                try:
                    admin_nic=int(input("enter the acount creater nic number="))
                
                except ValueError:
                    print("enter numbers only")
                    continue
                
                if admin_nic>99999999999 and admin_nic<1000000000000:
                    break
                else:
                    print("i nvalide nic number please try again")
        import random
        uu=str(admin_nic)[-3]
        admin_id_number=random.randint(99999,1000000)+(100*int(uu))
        admin_password = paswod_maker()
        #enter tha fill-admin data
        fill=open("admin_data.txt","a")
        fill.write(f"{admin_name},")#-admin_data-index(0)
        fill.write(f"{admin_id_number},")#-admin_data-index(1)
        fill.write(f"{admin_password},")#-admin_data-index(2)
        fill.write(f"{admin_age},")
        fill.write(f"{admin_nic},\n")
        fill.close()
        print(f"{admin_name}'s id={admin_id_number}")
        break

def paswod_maker():
    while True:
        try:
            pasword = int(input("enter the 6 degit password="))
            pasword2 = int(input("conform your password="))
            if pasword == pasword2:
                pass
            else:
                print("invalide pasword confamation please try again=")
                continue
        except ZeroDivisionError:
            print("enter 6 degit numbr")
        except ValueError:
            print("enter numbers only")
        if len(str(pasword)) == 6:
            return pasword
        else:
            print("invalide pasword tryagain")
            
            

def pasword_username_chack(people,username="admin",password="1112",acount_num="1112"):
    blance=0
    while(acount_num=="1112"):
        if people=="admin":
            fill=open("admin_data.txt","r")
            data=fill.readlines()
            fill.close()
        elif people=="user":
            fill=open("user_data.txt","r")
            data=fill.readlines()
            fill.close()
        else:
            pass 
        if username=="admin" and password=="1112":
            return data
        else:  
            for i in data:
                m=i.split(",")
                if m[0]==username and m[2]==password:
                    print("#####")
                    return m
              
        print("invalide username password-please try again")
        fill.close() 
        break  
    else:
        fill=open("blance.txt","r")
        data=fill.readlines()
        fill.close()
    
        if acount_num!=1112:
            for i in data:
                m=i.split(",")
                if m[1]==acount_num:
                    blance=int(m[2])
                else:
                    pass
        else:
            pass
        
        return blance
           
def create_a_bank_acount():
    global admin_id
    while(True):
        fill=open("user_data.txt","a")
        try:
            name=str(input("enter the acoun creater name name="))
            age=int(input("enter the acount cerater age="))
            while(True):
                try:
                    nic_number=int(input("enter the acount creater nic number="))
                    
                
                except ValueError:
                    print("enter numbers only")
                    continue
                
                if nic_number>99999999999 and nic_number<1000000000000:
                    break
                else:
                    print("i nvalide nic number please try again")
            import random
            uu=str(nic_number)[-3]
            acout_number=random.randint(99999,1000000)+(100*int(uu))
            money=int(input("enter your deposit mony="))
        except ValueError:
            print("enter tha sutabil input")
            continue
        except TypeError:
            print("intrthe sutabil index")
            continue
        print(name,acout_number,nic_number,age)
        password=paswod_maker()
        fill.write(f"{name},")#---index{0}--user-data
        fill.write(f"{acout_number},")#-1
        fill.write(f"{password},")#-2
        fill.write(f"{age},")#-3
        fill.write(f"{nic_number},\n")#-4
        fill.close()
        date=date_time()
        #open-blance-file
        data=open("blance.txt","a")
        data.write(f"{date},")
        data.write(f"{acout_number},")
        data.write(f"{money},-\n")
        data.close()
        #append-history-
        history=open("money_history.txt","a")
        history.write(f"{date},")
        history.write(f"{acout_number},")
        history.write(f"deposit,money={money},")
        history.write(f"blance={money},")
        history.write(f"who edet-{admin_id},\n")
        history.close()
        break

def history_maker(people,acount_no,money,funcation,data,blance):
    fill1=open("money_history.txt","a")
    date=date_time()
    fill1.write(f"{date},")
    fill1.write(f"{acount_no},")
    fill1.write(f"{funcation},")
    fill1.write(f"money={money},")
    fill1.write(f"blance={blance},")
    fill1.write(f"who edet-{people},\n")
    fill1.close()
    
    fill=open("blance.txt","w")
    for i in data:
        fill.write(f"{i}")
    fill.close()
    fill=open("blance.txt","a")
    fill.write(f"{date},")
    fill.write(f"{acount_no},")
    fill.write(f"{blance},\n")
    fill.close()            
   
    
def blance_edeter(people,acount_no,money,funcation):
    fill=open("blance.txt","r")
    data=fill.readlines()
    fill.close()
    
    blance=0
    if acount_no!=1112:
        for i in data:
            m=i.split(",")
            if m[1]==acount_no:
                blance=int(m[2])
                
                print(m)#........testing
                data.remove(i)
            else:
                pass
    else:
        pass
    if funcation=="show":
        return data
    elif funcation=="withrow":
        new_blance=blance-money
        history_maker(people,acount_no,money,funcation,data,new_blance)
        return new_blance
    elif funcation=="deposit":
        new_blance=blance+money
        history_maker(people,acount_no,money,funcation,data,new_blance)
        return new_blance 
           
def chack_history(date,acount_number):
    fill=open("money_history.txt","r")
    data=fill.readlines()
    num=0
    history=[]
    for i in data:
        m=i.split(",")
        if date=="1112":
            if acount_number==m[1]:
                history.append(i)
                num=num+1
            else:
                pass
        elif acount_number==1112:
            if date==m[0]:
                history.append(i)
                num=num+1
            else:
                pass
        elif date==m[0]:
            if acount_number==int(m[1]):
                history.append(i)
                num=num+1
    if num==0:
        return ("in valide history key word try again,")
    else:
        num=0
        return history
    

def detail_changer(people,username,password,):
    if people=="admin":
            fill=open("admin_data.txt","r")
            data=fill.readlines()
            fill.close()
    elif people=="user":
        fill=open("user_data.txt","r")
        data=fill.readlines()
        fill.close()
    else:
        pass 
    for i in data:
            m=i.split(",")
            if m[0]==username and m[2]==password:
                data.remove(i)
                print("#####")
            
    
    cod=paswod_maker()
    name=input("enter your new user name=")
    m[0]=name
    m[2]=cod
    fill=open("user_data.txt","w")
    for i in data:
        fill.write(f"{i},\n")
    fill.close()
    
    fill=open("user_data.txt","a")
    m.pop()
    for i in m:
        fill.write(f"{i},")
    fill.write(f"\n")
    fill.close()
    
    
    
        
    
            

           
# ------------user inter face-#########################################################################################################################################-

while (True):
    print("\033[33m                   Well come UniCom Bank [UCB]\033[0m")
    print("\033[1m                   ---------------------------\033[0m")
    print()
    print("\033[1m Enter Your User Key Word \033[0m")
    print("custmor---[1]")
    print("admin-----[2]")
    print()
    try:
        user_key = int(input("Enter The User Key="))
    except ValueError:
        print("\033[31m--------------ERROR----input key words only---\033[0m")
        continue
    
    if user_key == 1:
        while(True):
            print("\033[34m                   Wellcome to tha online cuctomer service \033[0m")
            print("Acount holder name pasword change--------[1]")
            print("Deposit_money----------------------------[2]")
            print("withrow money----------------------------[3]")
            print("money transfer---------------------------[4]")
            print("user data--------------------------------[5]")
            print("acount blance----------------------------[6]")
            print("user history-----------------------------[7]")
            print("previous manu----------------------------[0]")
            
            try:    
                funcation_key=int(input("Enter the funcation key word="))
            except ValueError:
                print("\033[31m---ERROR____Enter Tha Sutable Key Words only---- \033[0m")
                continue
            
#------------------------------------------------------------------

            if funcation_key==0:
                    print("\033[34m ________________Thank you_________\033[0m")
                    break
           
            
            elif funcation_key<0 or funcation_key>7:
                print("\033[31m---ERROR____Invalide Key Please Try Again---- \033[0m")
                continue
            
            else:
                print("\033[34m----------Enter Your Banking Details-------\033[0m")
                name=input("Enter tha acount holder name=")
                acount_number=input("Enter tha acount number=")
                acount_password=input("Enter tha acount holder password=")
                
                blance=pasword_username_chack(name,name,name,acount_number)
                if blance==0:
                    print("\033[31m---ERROR____your acount number is RONG-------Try  Again-- \033[0m")
                    continue
                else:
                    pass
                
                acount=pasword_username_chack("user",name,acount_password)
                if acount!=None:
                    print("\033[34m---Your Acount Founded---- \033[0m")
                else:
                    print("\033[31m---ERROR____Invalide User Name Password--[Please Try again]------ \033[0m")
                    continue
                    
            #banking actvity-------------------------------------------------
            if funcation_key==1:
                    detail_changer("user",name,acount_password)
                    print("\033[34m---Your Username and Password are Changed---- \033[0m")
                
            
            elif funcation_key==3:
                try:
                    money=int(input("Enter your withrowl amount="))
                except ValueError:
                    print("\033[31m---ERROR____Enter Tha Money Value only----\033[0m")
                    continue
                if money<blance:
                    new_blance=blance_edeter(name,acount_number,money,"withrow")
                    print("\033[34m---Your Curant Acount Blance---\033[0m")
                    print(new_blance)
                else:
                    print("\033[31m---ERROR____invalide withrowl amount---- [UCB]\033[0m")
                    continue

            elif funcation_key==2:
                try:
                    money=int(input("Enter your deposit amount="))
                except ValueError:
                    print("\033[31m---ERROR____Enter Money Value Only---- [UCB]\033[0m")
                    continue
                new_blance=blance_edeter(name,acount_number,money,"deposit")
                print("\033[34m---Your Curant Acount Blance---\033[0m")
                print(new_blance)
            
            elif funcation_key==4:
                acount_number2=int(input("Enter tha transfer acount number="))
                acount_number3=int(input("Conform yuor transfre acount number="))
                blance1=pasword_username_chack(name,name,name,acount_number2)
                if blance==0:
                    print("\033[31m---ERROR____Invalid Acount Number -------Pleace Try Again----\033[0m")
                    continue
                else:
                    pass
                
                if acount_number2==acount_number3:
                    try:
                        money=int(input("inter your withrowl amount="))
                    except ValueError:
                        print("\033[31m---ERROR____Enter Money Value Only---- [UCB]\033[0m")
                        continue
                    if money<blance:
                        new_blance=blance_edeter(name,acount_number,money,"withrow")
                        new_blance1=blance_edeter(name,acount_number2,money,"deposit")
                        print("user new blance=",new_blance)
                    else:
                        ("\033[31m---ERROR____Invalid Transfer ----Please Try Again--- [UCB]\033[0m")
                        continue
                else:
                    print("\033[31m---ERROR____Acount Number Confomation is rong----------Please Try Again---- \033[0m")
                    continue
            
            elif funcation_key==5:
                i=pasword_username_chack("user",name,acount_password)
                print()
                print(f"Acoun holder name---{i[0]}")
                print(f"Acoun number--------{i[1]}")
                print(f"Age-----------------{i[2]}")
                print(f"NIc_Number----------{i[3]}")
                print()

            elif funcation_key==6:
                blance=pasword_username_chack(name,name,name,acount_number)
                print(blance)
            
            elif funcation_key==7:
                print("\033[34m                ---Choos Your Sutable Key Word---\033[0m")
                print("\033[1m                ---------------------------------\033[0m")
                print("Date user history---[1]")
                print("ALL user history----[2]")
                print("")
                ee=int(input("Enter tha key word = "))
                print()
                if ee==1:
                    date=(input("enter tha date(year-month-date)="))
                    dd=chack_history(date,acount_number)
                    for i in history:
                        print(i)
                elif ee==2:
                    history=chack_history("1112",acount_number)
                    for i in history:
                        print(i)
    
                

    
            
        
        
    elif user_key == 2:
        print("\033[33m---WELL COME ADMIN---\033[0m")
        
        
        try:
            fill=open("admin_data.txt","r")
            fill.close()
        except FileNotFoundError:
            print()
            print("Enter user_name=123123   Password=super_admin")
            print("---------------------------------------------")
        
        admin_username=input("Enter your admin user name=")
        admin_password=input("Enter your admin pass word=")
        
        if admin_username=="123123" and admin_password=="super_admin":
            admin_acount_create()
        else:
            admin_detail=pasword_username_chack("admin",admin_username,admin_password)
            if admin_detail != None:
                admin_id=admin_detail[1]
                
                while(True):
                    print("manu")#_______admin.funcation.start--
                    print("\033[34m-[key Word]-\033[0m")
                    print()
                    print("Acount holder actvity-----[1]")
                    print("admin actvity-------------[2]")
                    print("go to main manu-----------[3]")
                    print()
                    
                    try:
                        ii=int(input("enter the key word="))
                    except ValueError:
                        print("\033[31m--ERROR---------Enter The Sutable Key Word Only---\033[0m")
                    if ii==1:
                        while True:
                            
                            print("Acount holder actvity")
                            print("Create an acount-------[1]")
                            print("Deposit_money----------[2]")
                            print("Withrow money----------[3]")
                            print("Money transfer---------[4]")
                            print("User data--------------[5]")
                            print("Acount blance----------[6]")
                            print("User history-----------[7]")
                            print("Previous manu----------[0]")
                            print()
                            
                            try:    
                                funcation_key=int(input("enter the funcation key word="))
                            except ValueError:
                                print("enteer key words only")
                                continue
                            
                                  
                            ###
                            if funcation_key==1:
                                create_a_bank_acount()
                                print("acount created suckssfully")
                            elif funcation_key==0:
                                    print("thank you")
                                    break
                            elif funcation_key<0 or funcation_key>7:
                                print("invalide key word----try again")
                                continue
                            ###
                            
                            else:
                                name=input("enter tha acount holder name=")
                                acount_number=input("enter tha acount number")
                                acount_password=input("enter tha acount holder password")
                                
                                blance=pasword_username_chack(name,name,name,acount_number)
                                if blance==0:
                                    print("invalid acount number")
                                    continue
                                acount=pasword_username_chack("user",name,acount_password)
                                if acount!=None:
                                    print("acount founted")
                                else:
                                    print("invalide user name pass word")
                                    print("try again")
                                    continue
                                
                            #banking actvity-----------------------------------------------------------------------------------------------------------------------------------------  
                            print( "enter the acount holder details")
                            
                            if funcation_key==3:
                                try:
                                    money=int(input("inter your withrowl amount="))
                                except ValueError:
                                        print("enter moni value only-in numbers")
                                        continue 
                                if money<blance:
                                    new_blance=blance_edeter(admin_id,acount_number,money,"withrow")
                                    print("your neu blance is=",new_blance)
                                else:
                                    print("invalid withrowl amount")
                                    continue

                            elif funcation_key==2:
                                try:
                                    money=int(input("enter your deposit amount="))
                                except ValueError:
                                        print("enter moni value only-in numbers")
                                        continue
                                new_blance=blance_edeter(admin_id,acount_number,money,"deposit")
                                print("your new blance=",new_blance)
                            
                            elif funcation_key==4:
                                acount_number2=int(input("enter tha transfer acount number="))
                                acount_number3=int(input("conform yuor transfre acount number="))
                                blance1=pasword_username_chack(name,name,name,acount_number2)
                                if blance1==0:
                                    print("invalid acount number")
                                    continue
                                else:
                                    pass
                                if acount_number2==acount_number3:
                                    try:
                                        money=int(input("inter your withrowl amount="))
                                    except ValueError:
                                        print("enter moni value only-in numbers")
                                        continue
                                    if money<blance:
                                        new_blance=blance_edeter(admin_id,acount_number,money,"withrow")
                                        new_blance1=blance_edeter(admin_id,acount_number2,money,"deposit")
                                        print("user new blance=",new_blance)
                                    else:
                                        print("invalide acount blanse")
                                        continue
                                else:
                                    print("transfer acount confamation is rong===========================")
                                    continue
                            
                            elif funcation_key==5:
                                i=pasword_username_chack("user",name,acount_password)
                                print()
                                print(f"acoun holder name={i[0]}")
                                print(f"acoun number={i[1]}")
                                print(f"age={i[2]}")
                                print(f"nic number={i[3]}")
                                print()

                            elif funcation_key==6:
                                blance=pasword_username_chack(name,name,name,acount_number)
                                print(blance)
                            
                            elif funcation_key==7:
                                print("enter the sutabil key word")
                                print("date user history=1")
                                print("all user history=2")
                                ee=int(input("enter tha key word="))
                                if ee==1:
                                    date=(input("enter tha date(year-month-date)="))
                                    dd=chack_history(date,acount_number)
                                    for i in history:
                                        print(i)
                                elif ee==2:
                                    history=chack_history("1112",acount_number)
                                    for i in history:
                                        print(i)
                                

                                                
                    elif ii==2:
                        while(True):
                            print("well come to staf actvity")
                            print("ACTVITY MANU")
                            print("all-acount holder-blance list=1")
                            print("bank transtation history=2")
                            print("all custmor details list=3")
                            print("change admin password,username=4")
                            print("chack admin detail=5")
                            print("all admin details=6")#fnish this
                            print("your details=7")
                            print("create a admin=8")
                            print("go to previous manu=0")
                            try:
                                key=int(input("enter than menu key word="))
                            except ValueError:
                                print("input key words only=")
                                continue
                            if key==0:
                                print("go to previous manu")
                                break
                            elif key>8 and key<0:
                                print("invalid key word please try again")
                                continue
                            
                            elif key==1:
                                fill=open("blance.txt","r")
                                data=fill.readlines()
                                fill.close()
                                for i in data:
                                    m=i.split(",")
                                    print(f"acount number={m[1]},blance={m[2]}")
                                    print()
                                    
                            elif key==2:
                                date=input("enter tha date year-month-date=")
                                data=chack_history(date,1112)
                                for i in data:
                                    print(i)
                                    print()
                                    
                            elif key==3:
                                fill=open("user_data.txt","r")
                                data=fill.readlines()
                                fill.close()
                                for i in data:
                                    m=i.split(",")
                                    print()
                                    print(f"acoun holder name={m[0]}")
                                    print(f"acoun number={m[1]}")
                                    print(f"age={m[2]}")
                                    print(f"nic number={m[3]}")
                                    print()
                                    
                            elif key==4:
                                detail_changer("admin",admin_username,admin_password)
                                print("your new password user  name changed")
                                
                            elif key==5:
                                i=pasword_username_chack("admin",admin_username,admin_password)
                                print()
                                print(f"admin name={i[0]}")
                                print(f"admin id number={i[1]}")
                                print(f"age={i[2]}")
                                print(f"nic number={i[3]}")
                                print()
                                
                            elif key==3:
                                fill=open("user_data.txt","r")
                                data=fill.readlines()
                                fill.close()
                                for i in data:
                                    m=i.split(",")
                                    print()
                                    print(f"acount holder name={m[0]}")
                                    print(f"acount number ={m[1]}")
                                    print(f"age={m[2]}")
                                    print(f"nic number={m[3]}")
                                    print()
                                    
                            elif key==6:
                                fill=open("admin_data.txt","r")
                                data=fill.readlines()
                                fill.close()
                                for i in data:
                                    m=i.split(",")
                                    print()
                                    print(f"admin name={m[0]}")
                                    print(f"admin id={m[1]}")
                                    print(f"age={m[2]}")
                                    print(f"nic number={m[3]}")
                                    print()
                        
                            elif funcation_key==7:
                                i=pasword_username_chack("admin",admin_username,admin_password)
                                print()
                                print(f"your name={i[0]}")
                                print(f"your id number={i[1]}")
                                print(f"age={i[2]}")
                                print(f"nic number={i[3]}")
                                print()   
                                 
                            elif key==8:
                                admin_acount_create()
                                print("new admin created")            
                    elif ii==3:
                        print("go to previus menu")
                        break
            else:
                print("invalid admin id pass word")
                continue
    else:
        print("Invald Key Word try again")





