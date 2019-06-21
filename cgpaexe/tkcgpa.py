from tkinter import *
import time;
import datetime
import random
from tkinter import messagebox



Two = 0
Three = 0
Four = 0
Eight = 0

oldsem = 0
numofsem = 0

twov = []
threev = []
fourv = []
eightv = []


def loginemp():
    root3 = Tk()
    root3.overrideredirect(True)
    root3.geometry("{0}x{1}+0+0".format(root3.winfo_screenwidth(), root3.winfo_screenheight()))
    root3.title("CGPA CALCULATIONS")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root3, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root3, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',expand = 1 ,fill = BOTH)
    login = Frame(body, width = 600, height = 400, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER ,expand = 1, fill = BOTH, ipady = 20,ipadx = 10)
    loginbtns = Frame(body, width = 700, height = 30, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    two = IntVar()
    three = IntVar()
    four = IntVar()
    eight = IntVar()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def exiit():
         qexit = messagebox.askyesno("CGPA","DO YOU WISH TO EXIT")
         if qexit > 0:
              root3.destroy()

    def okay():
        global Two,Three,Four,Eight
        Two  =  two.get()
        Three = three.get()
        Four = four.get()
        Eight = eight.get()
        root3.destroy()
        Next()
        
    #-------------------------------------------------------------------------------------------------------------------------------------------
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "CGPA CALCULATION", relief = GROOVE, width = 20 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    Label(login, text = "Predicted values :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 1)

    #heading
    Label(login, text = "Enter Details", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 0, column = 3)
    
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 2)
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 4)
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 5)



    Label(login, text = "Enter Number\n of 2 credit's :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 2)
    Label(login, text = "Enter Number\n of 3 credit's :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 2, column = 2)
    Label(login, text = "Enter Number\n of 4 credit's :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 3, column = 2)
    Label(login, text = "Enter Number\n of 8 credit's :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 4, column = 2)


    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = two,
               bd = 9, insertwidth = 3).grid(row=1,column=4)
    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = three,
               bd = 9, insertwidth = 3).grid(row=2,column=4)
    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = four,
               bd = 9, insertwidth = 3).grid(row=3,column=4)
    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = eight,
               bd = 9, insertwidth = 3).grid(row=4,column=4)
    


    btn1 = Button(loginbtns, text = "NEXT" ,command = okay,  relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)
    btn2 = Button(loginbtns, text = "EXIT" ,command = exiit, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)


   #-------------------------------------------------------------------------------------------------------------------------------------------
    root3.mainloop()



def Next():
    root4 = Tk()
    root4.overrideredirect(True)
    root4.geometry("{0}x{1}+0+0".format(root4.winfo_screenwidth(), root4.winfo_screenheight()))
    root4.title("CGPA CALCULATIONS")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root4, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root4, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',expand = 1 ,fill = BOTH)
    login = Frame(body, width = 600, height = 400, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER ,expand = 1, fill = BOTH, ipady = 20,ipadx = 10)
    loginbtns = Frame(body, width = 700, height = 30, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    global Two,Three,Four,Eight
    twok = []
    threek = []
    fourk = []
    eightk = []
    old = StringVar()
    ns = IntVar()
    
    for i in range(Two):
        t = "two" + str(i)
        t = StringVar()
        twok.append(t)

    for i in range(Three):
        t = "three" + str(i)
        t = StringVar()
        threek.append(t)

    for i in range(Four):
        t = "four" + str(i)
        t = StringVar()
        fourk.append(t)

    for i in range(Eight):
        t = "eight" + str(i)
        t = StringVar()
        eightk.append(t)
        
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def get():
        global twov,threev,fourv,eightv,numofsem,oldsem
        for t in twok:
            tw = str(t.get())
            twov.append(tw)

        for t in threek:
            tr = str(t.get())
            threev.append(tr)


        for t in fourk:
            fr = str(t.get())
            fourv.append(fr)

        for t in eightk:
            ei = str(t.get())
            eightv.append(ei)
        numofsem = ns.get()
        oldsem = old.get()
        root4.destroy()
        final()

    def back():
        global twov,threev,fourv,eightv,Two,Three,Four,Eight,numofsem,oldsem
        Two = 0
        Three = 0
        Four = 0
        Eight = 0
        
        numofsem = 0
        oldsem = 0

        twov = []
        threev = []
        fourv = []
        eightv = []
        root4.destroy()
        loginemp()
            
    #-------------------------------------------------------------------------------------------------------------------------------------------
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "CGPA CALCULATION", relief = GROOVE, width = 20 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    Label(login, text = "Predicted values :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 1)
    #heading
    Label(login, text = "Enter Details", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 0, column = 2)
    
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 3)
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 4)
##    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 10 , bd = 6, bg = 'Steelblue2',
##           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 5)



    Label(login, text = "Enter 2 credit \ngrades :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 0)
    Label(login, text = "Enter 3 credit \ngrades :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 1)
    Label(login, text = "Enter 4 credit \ngrades :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 3)
    Label(login, text = "Enter 8 credit \ngrades :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 4)

    Label(login, text = "Enter Old\n sem cgpa :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 2)
    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'),textvariable = old,
               bd = 9).grid(row=2,column=2)
    Label(login, text = "Enter number\nof semesters\nattended :\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 3, column = 2)
    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'),textvariable = ns,
               bd = 9).grid(row=4,column=2)
##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = three,
##               bd = 9, insertwidth = 3).grid(row=2,column=4)
##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = four,
##               bd = 9, insertwidth = 3).grid(row=3,column=4)
##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = eight,
##               bd = 9, insertwidth = 3).grid(row=4,column=4)
    
    r = 2
    for t in twok:
        Entry(login, textvariable=t, relief=SUNKEN,width=20, bd = 6,
              font = ('arial', 15, 'bold')).grid(row=r,column=0,padx = 15, pady = 15,ipady = 2)
        r = r + 1


    r1 = 2
    for t in threek:
        Entry(login, textvariable=t, relief=SUNKEN,width=20, bd = 6,
              font = ('arial', 15, 'bold')).grid(row=r1,column=1,padx = 15, pady = 15,ipady = 2)
        r1 = r1 + 1


    r2 = 2
    for t in fourk:
        Entry(login, textvariable=t, relief=SUNKEN,width=20, bd = 6,
              font = ('arial', 15, 'bold')).grid(row=r2,column=3,padx = 15, pady = 15,ipady = 2)
        r2 = r2 + 1

    r3 = 2
    for t in eightk:
        Entry(login, textvariable=t, relief=SUNKEN,width=20, bd = 6,
              font = ('arial', 15, 'bold')).grid(row=r3,column=4,padx = 15, pady = 15,ipady = 2)
        r3 = r3 + 1

         

    btn1 = Button(loginbtns, text = "NEXT" ,command = get,  relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)
    btn2 = Button(loginbtns, text = "BACK",command=back , relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)


   #-------------------------------------------------------------------------------------------------------------------------------------------
    root4.mainloop()

def final():
    root5 = Tk()
    root5.overrideredirect(True)
    root5.geometry("{0}x{1}+0+0".format(root5.winfo_screenwidth(), root5.winfo_screenheight()))
    root5.title("CGPA CALCULATIONS")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root5, width = 1280, height = 100, bd = 7, bg = 'dodgerblue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root5, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',expand = 1 ,fill = BOTH)
    login = Frame(body, width = 600, height = 400, bd = 7, bg = 'Steelblue2', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER ,expand = 1, fill = BOTH, ipady = 20,ipadx = 10)
    loginbtns = Frame(body, width = 700, height = 30, bd = 7, bg = 'Steelblue2', relief = RAISED)
    loginbtns.pack(side = BOTTOM,anchor = CENTER, fill = X)
    #-------------------------------------------------------------------------------------------------------------------------------------------
    sgpa = IntVar()
    cgpa = IntVar()
    mas = []
    global twov,threev,fourv,eightv,numofsem,oldsem
     #-------------------------------------------------------------------------------------------------------------------------------------------

    for i in range(len(twov)):
        twov[i] = twov[i].upper()

        if twov[i] == 'S' :
            twov[i] = 10 * 2

        elif twov[i] == 'A' :
            twov[i] = 9 * 2

        elif twov[i] == 'B' :
            twov[i] = 8 * 2

        elif twov[i] == 'C' :
            twov[i] = 7 * 2

        elif twov[i] == 'D' :
            twov[i] = 6 * 2

        elif twov[i] == 'E' :
            twov[i] = 5 * 2

        elif twov[i] == 'RA' :
            twov[i] = 0 * 2

        else:
            print("error")

    for i in range(len(threev)):
        threev[i] = threev[i].upper()

        if threev[i] == 'S' :
            threev[i] = 10 * 3

        elif threev[i] == 'A' :
            threev[i] = 9 * 3

        elif threev[i] == 'B' :
            threev[i] = 8 * 3

        elif threev[i] == 'C' :
            threev[i] = 7 * 3

        elif threev[i] == 'D' :
            threev[i] = 6 * 3

        elif threev[i] == 'E' :
            threev[i] = 5 * 3

        elif threev[i] == 'RA' :
            threev[i] = 0 * 3

        else:
            print("error")

    for i in range(len(fourv)):
        fourv[i] = fourv[i].upper()

        if fourv[i] == 'S' :
            fourv[i] = 10 * 4

        elif fourv[i] == 'A' :
            fourv[i] = 9 * 4

        elif fourv[i] == 'B' :
            fourv[i] = 8 * 4

        elif fourv[i] == 'C' :
            fourv[i] = 7 * 4

        elif fourv[i] == 'D' :
            fourv[i] = 6 * 4

        elif fourv[i] == 'E' :
            fourv[i] = 5 * 4

        elif fourv[i] == 'RA' :
            fourv[i] = 0 * 4

        else:
            print("error")

    for i in range(len(eightv)):
        eightv[i] = eightv[i].upper()

        if eightv[i] == 'S' :
            eightv[i] = 10 * 8

        elif eightv[i] == 'A' :
            eightv[i] = 9 * 8

        elif eightv[i] == 'B' :
            eightv[i] = 8 * 8

        elif eightv[i] == 'C' :
            eightv[i] = 7 * 8

        elif eightv[i] == 'D' :
            eightv[i] = 6 * 8

        elif eightv[i] == 'E' :
            eightv[i] = 5 * 8

        elif eightv[i] == 'RA' :
            eightv[i] = 0 * 8

        else:
            print("error")

    for i in twov:
        mas.append(i)
    for i in threev:
        mas.append(i)
    for i in fourv:
        mas.append(i)
    for i in eightv:
        mas.append(i)


    SGPA = (sum(mas)) / ((len(eightv) * 8) +(len(fourv) * 4) + (len(threev) * 3) + (len(twov) * 2))
    SGPA = round(SGPA,5)
    sgpa.set(str(SGPA))
    ocgpa = float(oldsem)
    numsematt = numofsem

    CGPA = (ocgpa * numsematt + SGPA) / (numsematt + 1)
    CGPA = round(CGPA,5)

    cgpa.set(str(CGPA))
    #-------------------------------------------------------------------------------------------------------------------------------------------
    def exiit():
         qexit = messagebox.askyesno("CGPA","DO YOU WISH TO EXIT")
         if qexit > 0:
              root5.destroy()

    def back():
        global twov,threev,fourv,eightv,numofsem,oldsem
        oldsem = 0
        numofsem = 0

        twov = []
        threev = []
        fourv = []
        eightv = []
        root5.destroy()
        Next()
    #-------------------------------------------------------------------------------------------------------------------------------------------
    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "CGPA CALCULATION", relief = GROOVE, width = 20 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    Label(login, text = "Predicted values :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 0)
    Label(login, text = "Predicted values :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 1)
    #heading
    Label(login, text = "YOUR\n CALCULATED\nVALUES\n", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 0, column = 2)
    
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 3)
    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 4)
##    Label(login, text = "Enter the value \nto predict :", relief = FLAT, width = 10 , bd = 6, bg = 'Steelblue2',
##           fg = 'Steelblue2', font = ('arial', 20, 'italic')).grid(row = 0, column = 5)


    Label(login, text = "Your SGPA:", relief = RAISED, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 1, column = 2)
    Label(login, textvariable = sgpa, relief = GROOVE, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 2, column = 2)
    Label(login, text = "Your CGPA:", relief = RAISED, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 3, column = 2)
    Label(login, textvariable = cgpa, relief = GROOVE, width = 15 , bd = 6, bg = 'Steelblue2',
           fg = 'black', font = ('arial', 20, 'italic')).grid(row = 4, column = 2)

    


##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = three,
##               bd = 9, insertwidth = 3).grid(row=2,column=4)
##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = four,
##               bd = 9, insertwidth = 3).grid(row=3,column=4)
##    Entry(login,relief=SUNKEN,font = ('arial', 15, 'italic'), textvariable = eight,
##               bd = 9, insertwidth = 3).grid(row=4,column=4)
    



         

    btn1 = Button(loginbtns, text = "EXIT" ,command = exiit,  relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)
    btn2 = Button(loginbtns, text = "BACK",command=back, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 6)


   #-------------------------------------------------------------------------------------------------------------------------------------------
    root5.mainloop()

loginemp()























