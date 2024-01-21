#2. Vizsgafeladat - Kovács Örs
# A vizsgán a hallgató a feladat egyik változatát választja. 
# A feladatot a hallgatónak legkésőbb a 7. modul kezdetéig kell megkapnia a Verziókezelő rendszerben.  
# A hallgató otthon végzi a feladatot. Amennyiben a hallgatónak kérdései merülnek fel a feladat elvégzése során, 
# akkor az óra alatt vagy a tanár számára megfelelő időben teheti fel neki azokat. A kész munka megvédése a tanteremben történik. 
# A hallgató bemutatja a munkát. A tanár bármilyen kérdést feltehet a feladattal kapcsolatban. 
# Létre kell hozni egy alkalmazást könyvek eladásának rögzítéséhez egy könyvesboltban. 
# A fő feladat: számba venni a könyvek eladásának folyamatát, rögzíteni az eladást végrehajtó munkatársat, megszámolni a bevételt. 
# A következő információ tárolása szükséges: 
# Munkatárs:  NÉV  Beosztás  Telefon  Email 
# Könyv:  A könyv címe  Megjelenés éve  Szerző  Műfaj  Önköltségi ár  Potenciális eladási ár 
# Értékesítés:  Munkatárs  Könyv  Értékesítés dátuma  Tényleges eladási ár 
# A következő funkciókat kell megvalósítani:  Hozzáadás, törlés, munkavállalói információk  Hozzáadás, törlés, információ a könyvekről 
#  Hozzáadás, törlés, értékesítési információk  Jelentések. Az adatok a képernyőn vagy egy fájlban jeleníthetők meg, a felhasználó választásának függvényében. 
# o Teljes körű információ a könyvesbolt alkalmazottairól 
# o Teljes körű információ a könyvekről 
# o Teljes körű információ az értékesítésről 
# o Egy bizonyos dátum összes értékesítése 
# o Összes értékesítés egy bizonyos időszakban 
# o Egy adott alkalmazott összes értékesítése 
# o A legkeresettebb könyv címe az adott időszakban 
# o Információ a legsikeresebb kereskedőről az adott időszakban 
# o Teljes nyereség az adott időszakbano A legkeresettebb szerző az adott időszakban 
# o A legkelendőbb műfaj az adott időszakban  Adatok mentése fájlba  Adatok betöltése fájlból A feladat megoldható mind függvénnyekkel, mind objektum-orientáltan. A hallgató választhat.

import os
import sys
import datetime

def Clear_Screen():         # Operációs rendszer szerinti képernyőtisztítás...
    if os.name == 'nt':     # Windows esetén a cls parancs fut....
        _ = os.system('cls')
    if os.name == 'posix':     # Mac és Linux esetén  parancs fut....
        _ = os.system('clear')
    return
    

def First_UserInterface(): # Első lépsként megnyitjuk a 3 db adatfile-t...
    Clear_Screen()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                    - A D A T F I L E kezelés -                  ")
    print()
    print("             A program működéséhez 3 db adatfile szükséges!\n Ha nem írsz be egyedi értéket, akkor az alapértelmezett file név marad!")
    print()
    print(" 1. A MUNKATÁRS adatfile alapértelemezett neve: employees.txt\n")
    print(" 2. A KÖNYV adatfile alapértelemezett neve: books.txt\n")
    print(" 3. Az ÉRTÉKESÍTÉS adatfile alapértelemezett neve: sales.txt\n")
    return


def AccessFile_Emp(): # Munkatárs adatfile megnyitása...
    directory = os.getcwd()
    emp_file_data=list()
    filename=""
    filename=input("Kérem írd be a megnyitandó MUNKATÁRS adatbázis file nevét! (ENTER - alapértelmezett érték...): ")
    if filename!="":
        fullfilename=filename+".txt"
    else:
        fullfilename = "employees.txt"
    try:
        with open(fullfilename,"r",encoding="utf-8") as fileHandler:
            for r in fileHandler:
                filerow=list(r.strip().split(";"))
                emp_file_data.append(filerow)
    except FileNotFoundError:
        print(f"A fájl {fullfilename} nem található az alábbi elérési útvonalon: {directory}...!")
        AccessFile_Emp()     
    return emp_file_data,fullfilename
    
def AccessFile_Books(): # Könyv adatfile megnyitása...
    directory = os.getcwd()
    books_file_data = []
    
    filename=input("Kérem írd be a megnyitandó KÖNYV adatbázis file nevét! (ENTER - alapértelmezett érték...):")
    if filename!="":
        fullfilename=filename+".txt"
    else:
        fullfilename = "books.txt"
    try:
        with open(fullfilename,"r",encoding="utf-8") as fileHandler:
            for r in fileHandler:
                filerow=list(r.strip().split(";"))
                books_file_data.append(filerow)
    except FileNotFoundError:
        print(f"A fájl {fullfilename} nem található az alábbi elérési útvonalon: {directory}...!")
        AccessFile_Books()
    return books_file_data,fullfilename

def AccessFile_Sales(): # Értékesítés adatfile megnyitása...
    directory = os.getcwd()
    sales_file_data = []
    
    filename=input("Kérem írd be a megnyitandó ÉRTÉKESÍTÉS adatbázis file nevét! (ENTER - alapértelmezett érték...):")
    if filename!="":
        fullfilename=filename+".txt"
    else:
        fullfilename = "sales.txt"
    try:
        with open(fullfilename,"r",encoding="utf-8") as fileHandler:
            for r in fileHandler:
                filerow=list(r.strip().split(";"))
                sales_file_data.append(filerow)
    except FileNotFoundError:
        print(f"A fájl {fullfilename} nem található az alábbi elérési útvonalon: {directory}...!")
        AccessFile_Sales()
    return sales_file_data,fullfilename

def Menu_Interface(emp_file_data,books_file_data,sales_file_data):
    menuitem=" "
    while menuitem!='0':
        Clear_Screen()
        print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
        print("                         - F Ő M E N Ü -                         ")
        print()
        print("     1. MUNKATÁRS almenü\n")
        print("     2. KÖNYVEK almenü\n")
        print("     3. ÉRTÉKESÍTÉS almenü\n")
        print()
        menuitem=input("Kérem válasszon az alábbi menüpontok közül! (KILÉPÉS - 0): ")
        if menuitem.isnumeric() and 0<int(menuitem)<4: 
            if menuitem=='1':
                Emp_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='2':
                Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='3':
                Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
            break
    return

def Emp_Menu_Interface(emp_file_data,books_file_data,sales_file_data):
    menuitem=" "
    while menuitem!='0':
        Clear_Screen()
        print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
        print("                        - MUNKATÁRS almenü -                     ")
        print()
        print("     1. Új munkatárs Rögzítése\n")
        print("     2. Munkatárs adatainak Módosítása\n")
        print("     3. Munkatárs keresése név alapján\n")
        print("     4. Munkatárs Törlése\n")
        print("     5. Munkatársak Riport\n")
        print()
        menuitem=input("Kérem válasszon az alábbi menüpontok közül! (VISSZALÉPÉS - 0): ")
        if menuitem.isnumeric() and 0<int(menuitem)<6: 
            if menuitem=='1':
                New_Emp_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='2':
                Edit_Emp_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='3':
                Search_Emp_By_Fullname_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='4':
                Delete_Emp_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='5':
                List_All_Emp_Interface(emp_file_data,books_file_data,sales_file_data)
            break
    Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return

def New_Emp_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - MUNKATÁRS almenü -                      ")      
    print()
    print("     1. Új munkatárs rögzítése")
    print()
    emp_fullname=input("Kérem a dolgozó teljes nevét!:")
    emp_jobname=input("Kérem a dolgozó beosztását!:")
    emp_telnr=input("Kérem a dolgozó telefonszámát!(csak számokkal):")
    emp_email=input("Kérem a dolgozó email címét! (ékezetes karakerek nélkül):")
    print()
    yesno=input("Mentsem az adatokat? (Y/N):")
    if yesno.upper()=="Y":
        emp_file_data.append([emp_fullname,emp_jobname,emp_telnr,emp_email])
    return    


def Report_Emp_Std(emp_file_data,books_file_data,sales_file_data):
    c=1
    print("Sorszám     Név                     Beosztás            Telefonszám         E-mail")
    for r in emp_file_data:
        print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]}")
        c+=1
    return

def Report_Books_Std(emp_file_data,books_file_data,sales_file_data):
    c=1
    print("Sorszám     Cím                     Megj.éve            Szerző              Műfaj               Önköltségi ár       Potenciális eladási ár")
    
    for r in books_file_data:
        print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]:<20}{r[4]:<20}{r[5]:<20}")
        c+=1
    return

def Report_All_Sales_Std(emp_file_data,books_file_data,sales_file_data):
    c=1
    print("Sorszám     Munkatárs               Könyv                    Értékesítés dátuma            Tényleges eladási ár")
    for r in sales_file_data:
        print(f"{c:<12}{r[0]:<24}{r[1]:<25}{r[2]:<30}{r[3]:<35}")
        c+=1
    return


def Edit_Emp_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - MUNKATÁRS almenü -                      ")      
    print()
    print("     2. Munkatárs adatainak Módosítása")
    print()
    Report_Emp_Std(emp_file_data,books_file_data,sales_file_data)
    
    valaszt_srsz=input("Melyik sorszámú dolgozót szeretnéd módosítani?: ")
    if valaszt_srsz=="":
        return
   
    print("A módosításhoz írja be az új értéket! Ha nem kíván módosítani, nyomjon ENTER-t!")
    print()
    emp_fullname=input("Kérem a dolgozó teljes nevét!:")
    emp_jobname=input("Kérem a dolgozó beosztását!:")
    emp_telnr=input("Kérem a dolgozó telefonszámát!(csak számokkal):")
    emp_email=input("Kérem a dolgozó email címét! (ékezetes karakerek nélkül):")

    yesno=input("Mentsem az adatokat? (Y/N):")
    if yesno.upper()=="Y":

        if emp_fullname:
            emp_file_data[int(valaszt_srsz)-1][0] = emp_fullname
        if emp_jobname:
            emp_file_data[int(valaszt_srsz)-1][1] = emp_jobname
        if emp_telnr:
            emp_file_data[int(valaszt_srsz)-1][2] = emp_telnr
        if emp_email:
            emp_file_data[int(valaszt_srsz)-1][3] = emp_email
    return    

def Search_Emp_By_Fullname_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - MUNKATÁRS almenü -                      ")      
    print()
    print("     3. Munkatárs keresése név alapján")
    print()
    
    emp_fullname=input("Kérem a dolgozó teljes nevét!:")
    c=1
    print("Sorszám     Név                     Beosztás            Telefonszám         E-mail")
    
    for r in emp_file_data:
        if emp_fullname==([r][0][0][:len(emp_fullname)]):
            print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]}")
            c+=1
    
    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_alluser=input("Kérlek írd be a File nevét! :")
        filename_alluser=filename_alluser+".txt"
        c=1
        with open(filename_alluser, "w", encoding="utf-8") as f:
            print("Sorszám     Név                     Beosztás            Telefonszám         E-mail",file=f)
            for r in emp_file_data:
                if emp_fullname==([r][0][0][:len(emp_fullname)]):
                    print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]}",file=f)
                    c+=1
    return   

def Delete_Emp_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - MUNKATÁRS almenü -                      ")      
    print()
    print("     4. Munkatárs Törlése")
    print()
    Report_Emp_Std(emp_file_data,books_file_data,sales_file_data)

    valaszt_srsz=input("Melyik sorszámú dolgozót szeretnéd törölni?: ")
    if valaszt_srsz=="":
        return
  
    yesno=input("Mentsem az adatokat? (Y/N):")
    
    if yesno.upper()=="Y":
        emp_file_data.pop(int(valaszt_srsz)-1)
    return    


def List_All_Emp_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - MUNKATÁRS almenü -                      ")      
    print()
    print("     5. Munkatársak Riport")
    print()
    print()
    Report_Emp_Std(emp_file_data,books_file_data,sales_file_data)

    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_alluser=input("Kérlek írd be a File nevét! :")
        filename_alluser=filename_alluser+".txt"
        c=1
        with open(filename_alluser, "w", encoding="utf-8") as f:
            print("Sorszám     Név                     Beosztás            Telefonszám         E-mail",file=f)
        for r in emp_file_data:
            print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]}",file=f)
            c+=1
    return   

def Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data):
    menuitem=" "
    while menuitem!='0':
        Clear_Screen()
        print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
        print("                       - KÖNYVEK almenü -                     ")
        print()
        print("     1. Új könyv Rögzítése\n")
        print("     2. Könyv adatainak Módosítása\n")
        print("     3. Könyv keresése cím alapján\n")
        print("     4. Könyv Törlése\n")
        print("     5. Könyvek Riport\n")
        print()
        menuitem=input("Kérem válasszon az alábbi menüpontok közül! (VISSZALÉPÉS - 0): ")
        if menuitem.isnumeric() and 0<int(menuitem)<6: 
            if menuitem=='1':
                New_Book_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='2':
                Edit_Book_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='3':
                Search_Book_By_Title_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='4':
                Delete_Book_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='5':
                List_All_Books_Interface(emp_file_data,books_file_data,sales_file_data)
            break
    Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return


def New_Book_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - KÖNYVEK almenü -                        ")      
    print()
    print("     1. Új könyv Rögzítése")
    print()
    book_title=input("Kérem a könyv teljes címét!: ")
    book_year=input("Kérem a megjelenés évét!: ")
    book_author=input("Kérem a szerző nevét!: ")
    book_type=input("Kérem a műfaj megnevezését!: ")
    book_selfcost=input("Kérem az önköltségi árat!: ")
    book_saleprice=input("Kérem az potenciális eladási árat!: ")
    print()
    yesno=input("Mentsem az adatokat? (Y/N):")
    if yesno.upper()=="Y":
        books_file_data.append([book_title,book_year,book_author,book_type,book_selfcost,book_saleprice])
    Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    


def Edit_Book_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - KÖNYVEK almenü -                        ")      
    print()
    print("     2. Könyv adatainak Módosítása")
    print()
    Report_Books_Std(emp_file_data,books_file_data,sales_file_data)
      
    valaszt_srsz=input("Melyik sorszámú könyvet szeretnéd módosítani?: ")
    if valaszt_srsz=="":
        return

    print("A módosításhoz írja be az új értéket! Ha nem kíván módosítani, nyomjon ENTER-t!")
    print()
    book_title=input("Kérem a könyv teljes címét!: ")
    book_year=input("Kérem a megjelenés évét!: ")
    book_author=input("Kérem a szerző nevét!: ")
    book_type=input("Kérem a műfaj megnevezését!: ")
    book_selfcost=input("Kérem az önköltségi árat!: ")
    book_saleprice=input("Kérem az potenciális eladási árat!: ")
    
    yesno=input("Mentsem az adatokat? (Y/N):")
    if yesno.upper()=="Y":
        if book_title:
            books_file_data[int(valaszt_srsz)-1][0] = book_title
        if book_year:
            books_file_data[int(valaszt_srsz)-1][1] = book_year
        if book_author:
            books_file_data[int(valaszt_srsz)-1][2] = book_author
        if book_type:
            books_file_data[int(valaszt_srsz)-1][3] = book_type
        if book_selfcost:
            books_file_data[int(valaszt_srsz)-1][4] = book_selfcost
        if book_saleprice:
            books_file_data[int(valaszt_srsz)-1][5] = book_saleprice
    
    Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    

def Search_Book_By_Title_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - KÖNYVEK almenü -                        ")      
    print()
    print("     3. Könyv keresése cím alapján")
    print()
    
    book_title=input("Kérem a könyv címét!:")
    
    print("Sorszám     Cím                     Megj.éve            Szerző              Műfaj               Önköltségi ár       Potenciális eladási ár")
    c=1
    for r in books_file_data:
        if book_title==([r][0][0][:len(book_title)]):
            print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]:<20}{r[4]:<20}{r[5]:<20}")
            c+=1

    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_books=input("Kérlek írd be a File nevét! :")
        filename_books=filename_books+".txt"
        c=1
        with open(filename_books, "w", encoding="utf-8") as f:
            print("Sorszám     Cím                     Megj.éve            Szerző              Műfaj               Önköltségi ár       Potenciális eladási ár",file=f)
        
        for r in books_file_data:
            if book_title==([r][0][0][:len(book_title)]):
                print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]:<20}{r[4]:<20}{r[5]:<20}",file=f)
                c+=1
    Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return   


def Delete_Book_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - KÖNYVEK almenü -                        ")     
    print()
    print("     4. Könyv Törlése")
    print()
    Report_Books_Std(emp_file_data,books_file_data,sales_file_data)

    valaszt_srsz=input("Melyik sorszámú könyvet szeretnéd törölni?: ")
    if valaszt_srsz=="":
        return
  
    yesno=input("Mentsem az adatokat? (Y/N):")
    
    if yesno.upper()=="Y":
        books_file_data.pop(int(valaszt_srsz)-1)
    Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    


def List_All_Books_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                       - KÖNYVEK almenü -                        ")       
    print()
    print("     5. Könyvek Riport")
    print()
    print()
    Report_Books_Std(emp_file_data,books_file_data,sales_file_data)



    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_allbook=input("Kérlek írd be a File nevét! :")
        filename_allbook=filename_allbook+".txt"
        c=1
        with open(filename_allbook, "w", encoding="utf-8") as f:
            print("Sorszám     Cím                     Megj.éve            Szerző              Műfaj               Önköltségi ár       Potenciális eladási ár",file=f)
        for r in books_file_data:
            print(f"{c:<12}{r[0]:<24}{r[1]:<20}{r[2]:<20}{r[3]:<20}{r[4]:<20}{r[5]:<20}",file=f)
            c+=1
    Book_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return   

def Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data):
    menuitem=" "
    while menuitem!='0':
        Clear_Screen()
        print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
        print("                      - ÉRTÉKESÍTÉS almenü -                     ")
        print()
        print("     1. Könyvértékesítés Rögzítése\n")
        print("     2. Értékesítés Törlése\n")
        print("     3. Értékesítési Teljes Riport\n")
        print("     4. Adott időszak értékesítési Riport\n")
        print("     5. Egy adott alkalmazott értékesítési Riport\n")
        print("     6. A legkeresettebb könyv egy adott időszakban Riport\n")
        print("     7. A legkeresettebb szerző egy adott időszakban Riport\n")
        print("     8. A legkeresettebb szerző egy adott időszakban Riport\n")
        print("     9. A legkelendőbb műfaj egy adott időszakban Riport\n")
        print("     10. Teljes nyereség az adott időszakban Riport\n")
        print()
        menuitem=input("Kérem válasszon az alábbi menüpontok közül! (VISSZALÉPÉS - 0): ")
        if menuitem.isnumeric() and 0<int(menuitem)<11: 
            if menuitem=='1':
                New_Sales_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='2':
                Delete_Sales_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='3':
                All_Sales_Report_Interface(emp_file_data,books_file_data,sales_file_data)
            if menuitem=='4':
                Search_Sales_By_Date_Interface(emp_file_data,books_file_data,sales_file_data)
        #     if menuitem=='5':
        #         # List_All_Emp_Interface(emp_file_data,books_file_data,sales_file_data)
            break
    Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return


def New_Sales_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                      - ÉRTÉKESÍTÉS almenü -                     ")
    print()      
    print()
    print("     1. Könyvértékesítés Rögzítése")
    print()
    sales_title=input("Kérem a könyv teljes címét!: ")
    sales_date=input("Kérem az értékesítés dátumát (ÉÉÉÉ.HH.NN formátumban!: ")
    sales_employee=input("Kérem az értékesítő kolléga nevét!: ")
    sales_price=input("Kérem a tényleges eladási árat (Ft)!: ")
    print()
    yesno=input("Mentsem az adatokat? (Y/N):")
    if yesno.upper()=="Y":
        sales_file_data.append([sales_employee,sales_title,sales_date,sales_price])
    Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    


def Delete_Sales_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                      - ÉRTÉKESÍTÉS almenü -                     ")    
    print()
    print("     2. Értékesítés Törlése")
    print()
    Report_All_Sales_Std(emp_file_data,books_file_data,sales_file_data)
    
    valaszt_srsz=input("Melyik sorszámú értékesítést szeretnéd törölni?: ")
    if valaszt_srsz=="":
        return
  
    yesno=input("Mentsem az adatokat? (Y/N):")
    
    if yesno.upper()=="Y":
        sales_file_data.pop(int(valaszt_srsz)-1)
    Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    




def All_Sales_Report_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                      - ÉRTÉKESÍTÉS almenü -                     ")
    print()      
    print()
    print("     3. Értékesítési Teljes Riport\n")
    print()
    Report_All_Sales_Std(emp_file_data,books_file_data,sales_file_data)
    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_allsales=input("Kérlek írd be a File nevét! :")
        filename_allsales=filename_allsales+".txt"
        with open(filename_allsales, "w", encoding="utf-8") as f:
            print("Sorszám     Munkatárs               Könyv                    Értékesítés dátuma            Tényleges eladási ár",file=f)        
            c=1
            for r in sales_file_data:
                f.write(f"{c:<12}{r[0]:<24}{r[1]:<25}{r[2]:<30}{r[3]:<35}\n")
                c+=1
    Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return    



def Search_Sales_By_Date_Interface(emp_file_data,books_file_data,sales_file_data):
    Clear_Screen()
    lines=list()
    print("* * * * * * * *  KÖNYVESBOLT Információs Központ * * * * * * * * ")
    print("                      - ÉRTÉKESÍTÉS almenü -                     ")     
    print()
    print("     4. Adott időszak értékesítési Riport")
    print()
    
    sales_date1=input("Kérem adja meg az intervallum kezdő dátumát!: ")
    sales_date2=input("Kérem adja meg az intervallum végső dátumát!: ")
    sales_date_list=[sales_date1,sales_date2]
    sales_date_list.sort()
    print("Sorszám     Munkatárs               Könyv                    Értékesítés dátuma            Tényleges eladási ár")  
    c=1
    for r in sales_file_data:
        if sales_date_list[0]<([r][0][2])<sales_date_list[1]:
            print(f"{c:<12}{r[0]:<24}{r[1]:<25}{r[2]:<30}{r[3]:<35}")
            c+=1
    yesno=input("Mentsem az adatokat külső File-ba? (Y/N):")
    
    if yesno.upper()=="Y":
        filename_sales=input("Kérlek írd be a File nevét! :")
        filename_sales=filename_sales+".txt"
        c=1
        with open(filename_sales, "w", encoding="utf-8") as f:
            print("Sorszám     Munkatárs               Könyv                    Értékesítés dátuma            Tényleges eladási ár",file=f)  
            for r in sales_file_data:
                if sales_date_list[0]<([r][0][2])<sales_date_list[1]:
                    print(f"{c:<12}{r[0]:<24}{r[1]:<25}{r[2]:<30}{r[3]:<35}",file=f)
            c+=1
    Sales_Menu_Interface(emp_file_data,books_file_data,sales_file_data)
    return   


def Save_Data_Emp_Files(data, fullfilename):
    print("MUNKATÁRS.... Változások mentése")
    with open(fullfilename, "w", encoding="utf-8") as f:
        for r in data:
            f.write(f"{r[0]};{r[1]};{r[2]};{r[3]}\n")
    print("Fájlba írtam az adatokat. Kész.\n")
    return

def Save_Data_Book_Files(data, fullfilename):
    print("KÖNYV.... Változások mentése")
    with open(fullfilename, "w", encoding="utf-8") as f:
        for r in data:
            f.write(f"{r[0]};{r[1]};{r[2]};{r[3]};{r[4]};{r[5]}\n")
    print("Fájlba írtam az adatokat. Kész.\n")
    return

def Save_Data_Sales_Files(data, fullfilename):
    print("ÉRTÉKESÍTÉS.... Változások mentése")
    with open(fullfilename, "w", encoding="utf-8") as f:
        for r in data:
            f.write(f"{r[0]};{r[1]};{r[2]};{r[3]}\n")
    print("Fájlba írtam az adatokat. Kész.\n")
    return




def main():
    Clear_Screen()
    First_UserInterface()
    emp_file_data,emp_filename=AccessFile_Emp()
    books_file_data,books_filename=AccessFile_Books()    
    sales_file_data, sales_filename =AccessFile_Sales()
    Menu_Interface(emp_file_data,books_file_data,sales_file_data)

    Save_Data_Emp_Files(emp_file_data,emp_filename)
    Save_Data_Book_Files(books_file_data,books_filename)
    Save_Data_Sales_Files(sales_file_data,sales_filename)


if __name__ == '__main__':
    sys.exit(main())
