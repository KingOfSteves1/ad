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
    t.sleep(3)
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
    t.sleep(1.5)
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
        c=input("")
        rmc=r.randint(1,3)
        if c==rmc:
            rmc=r.randint(1,3)
            print("You got it right!")
            t.sleep(1)
            print("-----------")
            print("You move on")
            t.sleep(1)
            print("-----------")
            print("You have 3 options forward(1), right(2) and left(3).")
            c=input("")
            if c==rmc:
                rmc=r.randint(1,3)
                print("You got it right!")
                t.sleep(1)
                print("-----------")
                print("You move on")
                t.sleep(1)
                print("-----------")
                print("You have 3 options forward(1), right(2) and left(3).")
                c=input("")
                if c==rmc:
                    rmc=r.randint(1,3)
                    print("You got it right!")
                    t.sleep(1)
                    print("-----------")
                    print("You move on")
                    t.sleep(1)
                    print("-----------")
                    print("You have 3 options forward(1), right(2) and left(3).")
                    c=input("")
                    if c==rmc:
                        rmc=r.randint(1,3)
                        print("You got it right!")
                        t.sleep(1)
                        print("-----------")
                        print("You move on")
                        t.sleep(1)
                        print("-----------")
                        print("You have 3 options forward(1), right(2) and left(3).")
                        c=input("")
                        if c==rmc:
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
    print("womnen")
enter()
