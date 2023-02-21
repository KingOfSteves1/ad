import time as t
import os
import random as r
#vars

cmaze=False
pdeath=""
#functions

def death():
    global pdeath
    t.sleep(2)
    print("--------------")
    print("You have died from "+pdeath+".")
    print("--------------")
    t.sleep(5)
    enter()
def enter():
    global cmaze
    global pdeath
    os.system('cls')
    c=""
    route=""
    hrul=False
    maze=False
    print("--------------------")
    print("Welcome to Hard Game")
    print("--------------------")
    t.sleep(2.45)
    print("make sure to round logically")
    t.sleep(.1)
    os.system('cls')
    route=int(input("Choose a route: 1=bad 2=good 3=neutral:\n"))
    #secret route
    if route ==4:
        hrul=True
        cmaze=True
        if hrul==True:
            print("-------------")
            print("You have won!")
            print("-------------")
            t.sleep(2)
            print("Just kidding.")
            t.sleep(1.5)
            pdeath="no reason just because u need to die and never choose this choice again because u are de big gei"
            death()
    #BAD ROUTE
    elif route ==1:
        maze=True
        if maze==True:
            mazegame()
    #death if anything else
    else:
        pdeath="chosing a boring routes"
        death()

def mazegame():
    global cmaze
    global pdeath
    if cmaze==True:
        print("You finished the maze via cheating!")
        t.sleep(1)
        women()
    else:
        print("--------------------------")
        print("You have entered THE MAZE!")
        print("--------------------------")
        t.sleep(2)
        print("You find yourself inside of a maze.\nYou have 3 options forward(1), right(2) and left(3).")
        rmc=r.randint(1,3)
        print(rmc)
        c=input("")
        if c==str(rmc):
            rmc=r.randint(1,3)
            print("You got it right!")
            t.sleep(1)
            print("-----------")
            print("You move on")
            t.sleep(1)
            print("-----------")
            print("You have 3 options forward(1), right(2) and left(3).")
            c=input("")
            if c==str(rmc):
                rmc=r.randint(1,3)
                print("You got it right!")
                t.sleep(1)
                print("-----------")
                print("You move on")
                t.sleep(1)
                print("-----------")
                print("You have 3 options forward(1), right(2) and left(3).")
                c=input("")
                if c==str(rmc):
                    rmc=r.randint(1,3)
                    print("You got it right!")
                    t.sleep(1)
                    print("-----------")
                    print("You move on")
                    t.sleep(1)
                    print("-----------")
                    print("You have 3 options forward(1), right(2) and left(3).")
                    c=input("")
                    if c==str(rmc):
                        rmc=r.randint(1,3)
                        print("You got it right!")
                        t.sleep(1)
                        print("-----------")
                        print("You move on")
                        t.sleep(1)
                        print("-----------")
                        print("You have 3 options forward(1), right(2) and left(3).")
                        c=input("")
                        if c==str(rmc):
                            print("You got it right!")
                            t.sleep(1)
                            print("You finished the maze!")
                            t.sleep(1)
                            women()
                        else:
                            pdeath = "you ate soup with fork"
                            death()
                    else:
                        pdeath = "spontanious heart attack"
                        death()
                else:
                    pdeath = "falling bowlder"
                    death()
            else:
                pdeath = "tiger eating you"
                death()
        else:
            pdeath = "spider wraps you up and slowy devours your corpse"
            death()    

def women():
    global pdeath
    c = input("Do u like women??\nyes|no\n")
    if c=="yes":
        print("Women")
        t.sleep(1000)
        pdeath="old age"
        death()
    elif c=="no":
        print("You are diagnosed with the big gei")
        print("----------------------------------")
        t.sleep(2.5)
        print("You have been approached by a group of women.")
        print("---------------------------------------------")
        t.sleep(2.5)
        print("You must now roll 3 times with a d20 die with varying requirements of Rizz.")
        print("---------------------------------------------------------------------------")
        t.sleep(3)
        c = input("Do you wish to proceed?\ny|n\n")
        if c =="n":
            pdeath = "Lack of Courage, you then keel over and died"
            death()
        elif c =="y":
            c=r.randint(1,20)
            print(c)
            t.sleep(2)
            if c <= 5:
                pdeath = "Lack of Rizz"
                death()
            else:
                print("You rolled a "+str(c)+", which is greater than that of 5, you live.")
                print("-------------------------------------------------------------------")
                c=r.randint(1,20)
                print(c)
                if c<=15:
                    pdeath="no rizz"
                    death()
                else:
                    print("You rolled a "+str(c)+", which is greater then that of 10, you live.")
                    print("--------------------------------------------------------------------")
                    c=r.randint(1,20)
                    print(c)
                    if c<=19:
                        pdeath="You suck at gambling"
                        death()
                    else:
                        slep()
        else:
            pdeath="why did u do this"
            death()
    else:
        pdeath ="you brought this upon urself"
        death()
def slep():
    os.system('cls')
    global pdeath
    print("Answer this question:")
    qa = int(input("1 + 4 + 2 + 7 + 9 + 65 + 3 + 2 / 8 + 23 - 2 * 2 + 2 + 76 / 2 = "))
    if qa==150:
        print("Big brian")
        t.sleep(2)
        print("time for a patience challenge")
        t.sleep(2)
        print("reddy go")
        os.system('cls')
        t.sleep(1)
        c=0
        while c<=100:
            c+=1
            print("tick | "+str(c))
            t.sleep(1)
            
            os.system('cls')
            c+=1
            print("tock | "+str(c))
            t.sleep(1)
            os.system('cls')
slep()
