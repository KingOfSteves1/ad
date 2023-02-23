import time as t
import os
import random as r
#vars

cmaze=False
rizz = False
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
    global rizz
    global pdeath
    os.system('cls')
    c=""
    route=""
    hrul=False
    maze=False
    print("--------------------")
    print("Welcome to Hard Game")
    print("--------------------")
    t.sleep(1.5)
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
    elif route ==69:
        rizz =True
        print("nice")
        t.sleep(1)
        pdeath = "niice"
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
#first part of game
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
#manager attack
def attack():
    global pdeath
    print("You've summoned the casino manager!")
    t.sleep(1)
    print("You see him start to attack from below.\n What do you do?")
    c=input("Up(1) Down(2) Slash(3) Poke(4) Run(5)\n")
    if c=="1":
        print("You manage to slice him from above!")
        t.sleep(1)
        print("You see him try to poke you! What do you do?")
        c=input("Down(2) Slash(3) Poke(4) Run(5)\n")
        if c=="2":
            print("You die!")
            pdeath = "poked by manager"
            death()
        elif c=="3":
            print("You manage to slash him!")
            t.sleep(1)
            print("You see him try to attack from above! What do you do?")
            
            c=input("Down(2) Slash(3) Run(5)\n")
            if c=="2":
                print("You manage to slash him!")
                t.sleep(1)
                print("You defeated the Manager!")
                #win
                t.sleep(1)
                print("You finally beat THE HARD GAME!(The cowards way)")
                print("------------------------------------------------")
                print("Haha just kidding.")
                c=input("Wanna play it for real? y | n\n")
                if c=="y":
                    cmaze=False
                    rizz=False
                    enter()
                else:
                    pdeath = "ur bad"
                    death()

            elif c=="3":
                print("You die!")
                pdeath = "attacked from above"
                death()
            else:
                print("OK then. Weird. Start over.")
                attack()
        elif c=="4":
            print("You manage to deflect his attack! Try again!")
            attack()
        else:
            print("OK then. Weird. Start over.")
            attack()
    elif c=="2":
        print("You deflected his attack! Try again!")
        attack()
    elif c=="3":
        print("You deflected his attack! Try again!")
        attack()
    elif c=="4":
        print("You die!")
        pdeath="sliced by manager"
        death()
    else:
        print("OK then. Weird.")
        attack()
#next part of game
def women():
    global rizz
    global pdeath
    c = input("Do u like women??\nyes|no\n")
    if rizz ==True:
        print("You finished the women via cheating!")
        slepp()
    elif c=="yes":
        print("Women")
        t.sleep(10)
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
        #dicestuff
        t.sleep(3)
        c = input("Do you wish to proceed?\ny|n\n")
        if c =="n":
            pdeath = "Lack of Courage, you then keel over and died"
            death()
        elif c =="y":
            t.sleep(2)
            print("You need to roll above a 5.")
            print("---------------------------")
            t.sleep(1)
            c=r.randint(1,20)
            print(c)
            t.sleep(2)
            if c <= 5:
                pdeath = "Lack of Rizz"
                death()
            else:
                print("You rolled a "+str(c)+", which is greater than that of 5, you live.")
                print("-------------------------------------------------------------------")
                t.sleep(2)
                print("You need to roll above a 15.")
                print("----------------------------")
                t.sleep(2)
                c=r.randint(1,20)
                print(c)
                if c<=15:
                    pdeath="no rizz"
                    death()
                else:
                    print("You rolled a "+str(c)+", which is greater then that of 15, you live.")
                    print("--------------------------------------------------------------------")
                    t.sleep(2)
                    print("You need to roll a 20.")
                    print("----------------------")
                    t.sleep(2)
                    c=r.randint(1,20)
                    print(c)
                    if c<=19:
                        print("you suck at gambling \nNow you must fight the casino")
                        attack()
                        
                        
                    else:
                        slepp()
        else:
            pdeath="why did u do this"
            death()
    else:
        pdeath ="you brought this upon urself"
        death()
#next phase of game
def slepp():
    global pdeath
    global cmaze
    global rizz
    print("--------------------------")
    print("You have entered THE BEDROOM!")
    print("--------------------------")
    t.sleep(2)
    rb = r.randint(1,8)
    print("You have 8 options on your side(1), on your back(2) on your face(3) on your feet(4) crisscross apple sauce (5) on a plane (WITH SNAKES)(6) with eyes open(7) Smelling like cheese(8).")
    z=input("")
    if str(z) == rb:
        print("time for a patience challenge")
        t.sleep(2)
        print("reddy go")
        os.system('cls')
        t.sleep(1)
        c=0
        while c<400:
            c+=1
            print("tick | "+str(c))
            t.sleep(1)
            if c==69:
                print("nice")
            os.system('cls')
            c+=1
            print("tock | "+str(c))
            t.sleep(1)
            if c==69:
                print("nice")
            os.system('cls')
            #beat game
        print("You finally beat THE HARD GAME!")
        print("-------------------------------")
        print("Haha just kidding.")
        c=input("Wanna play it for real? y | n\n")
        if c=="y":
            cmaze=False
            rizz=False
            enter()
        else:
            pdeath = "ur bad"
            death()
    else:
        pdeath = "you cant breath you dead boi"
        death()

attack()
