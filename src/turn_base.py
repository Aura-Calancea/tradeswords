#Trade Swords   
#05.11.2018
#CeVA

import sys
import os
import time
import cmd
import textwrap
import random
import copy
import subprocess
import pprint

########## Set Screen ##########
def set_screen(rows, columns):
    cmd = "printf"
    param = "\"\e[8;"                                   #ce e asta? 
    param += str(rows) + ";" + str(columns) + "t\""
    subprocess.call([cmd, param])
    print()

def print_game(left_array, right_array, player_att, player_def):
    border_size = 1
    border_char = " * "
    announcement_size = 2
    decision_size = 1
    left_right_spacing = 100
    rows = max(len(left_array), len(right_array)) + (border_size * 2) + announcement_size + decision_size
    columns = 10 + 10 + left_right_spacing + (border_size * 2)
    set_screen(rows, columns)
    state = border_char * columns

    for i in range(min(len(left_array), len(right_array))):
        spacing_size = columns - len(left_array[i].name) - len(right_array[i].name) - (border_size * 2)
        state += border_char + (" " * spacing_size) + right_array[i].name + border_char

    for i in range(min(len(left_array), len(right_array)), max(len(left_array), len(right_array))):
        if i >= len(left_array):
            spacing_size = columns - len(right_array[i].name) - (border_size * 2)
            state += border_char + (" " * spacing_size) + right_array[i].name + border_char
        elif i >= len(right_array):
            spacing_size = columns - len(left_array[i].name) - (border_size * 2)
            state += border_char + (" " * spacing_size) + left_array[i].name + border_char

    announcement = "Player" + player_att.name + ", Unit" + player_att.eroi[0].name + "bla bla" + player_def.name + ", unit"
    decision = "Player " + player_def.name + "turn, unit " + player_att.eroi[0].name + "turn. Choose target:"

    state += border_char + announcement + (" " * (columns - len(announcement) - border_size * 2))+ border_char
    state += border_char + decision + (" " * (columns - len(decision) - border_size * 2)) + border_char
    state += border_char * columns
    print (state)



class Unit:

    maxHP = 100

    def __init__(self):                                      #se creaza doar pt metodele din clasa ( ) 
        self.name         
        self.damage
        self.armor 
        self.cost
        self.HP

    def take_dammage(self, damageE):
        self.HP = self.HP + self.armor - damageE
        return self.HP

    def create_unit(self):
        a = self.__class__()
        return a

    @property
    def show_cost(self):
        print(self.cost)

class low_Heroes(Unit):

    cost = 25

class Gardian(low_Heroes):

    def __init__(self):
        self.name = 'Gardian'
        self.damage = 15
        self.armor = 4
        self.HP = self.maxHP


class Spadasin(low_Heroes):

    def __init__(self):
        self.name = 'Spadasin'
        self.damage = 14
        self.armor = 5
        self.HP = self.maxHP
        

class Prastier(low_Heroes):

    def __init__(self):
        self.name = 'Prastier'
        self.damage = 13
        self.armor = 2
        self.HP = self.maxHP

class mid_Heroes(Unit):

    cost = 33

class Arcas(mid_Heroes):

    def __init__(self):
        self.name = 'Arcas'
        self.damage = 20
        self.armor = 6
        self.HP = self.maxHP

class Hoplit(mid_Heroes):

    def __init__(self):
        self.name = 'Hoplit'
        self.damage = 18
        self.armor = 7
        self.HP = self.maxHP

class Calaret(mid_Heroes):

    def __init__(self):
        self.name = 'Calaret'
        self.damage = 16
        self.armor = 8
        self.HP = self.maxHP
class high_Heroes(Unit):

    cost = 50

class Cavaler(high_Heroes):

    def __init__(self):
        self.name = 'Cavaler'
        self.damage = 25
        self.armor = 10
        self.HP = self.maxHP

class Centaur(high_Heroes):

    def __init__(self):
        self.name = 'Centaur'
        self.damage = 23
        self.armor = 9
        self.HP = self.maxHP

class Ciclop(high_Heroes):

    def __init__(self):
        self.name = 'Ciclop'
        self.damage = 22
        self.armor = 10
        self.HP = self.maxHP

def show_list(l):
    for ind, val in enumerate(l):
        print(ind, ":", vars(val))

def show_list_opt(l):
    for ind, val in enumerate(l):
        print(ind, ":", vars(val), "cost:", val.cost)


class Player:
    
    def __init__(self, name):
        self.name = name   
        self.eroi = []
        self.gold = 100

    def current_gold(self, obj):
        c_gold = self.gold - obj.cost
        self.gold = c_gold
        return (self.gold)

    def show_name(self):
        print(self.name)
        print(self.gold)
        #return "Numele este %s si are %i gold" % (self.name , self.gold)

    def check_gold( self, lista, inputj, lista2, i):
        if self.gold >= lista[inputj].cost:                
            lista2[i] = copy.copy(lista[inputj])
            self.eroi.append(lista2[i])
            self.current_gold(lista[inputj])
            show_list(self.eroi)
        else:
            print("You don't have enough gold to hire %s, try a cheaper one! \n" %lista[adaug].name)
        

    def complete_list(self, lista):
        a = ""
        b = ""
        c = ""
        d = ""
        i = 0
        alpos = [a, b, c, d]
        while i < len(alpos) and self.gold > 24:
            self.show_name()
            adaug = int(input("Which hero would you like to hire"))
            if adaug > 8:
                print("Please enter a valid number less than 9")
            else:
                self.check_gold(lista, adaug, alpos, i)
            i += 1
        else:
            print("You have hired:")
            show_list(self.eroi)

    def choice(self, lista):
        arebani = True
        while arebani:
            adaug = int(input("Which hero would you like to hire"))
            if adaug > 8:
                print("Please enter a valid number less than 9")
            else:    
                if lista[adaug].cost <= self.gold and self.gold >0 :
                    self.show_name()    
                    self.eroi.append(lista[adaug].create_unit())
                    self.current_gold(lista[adaug])
                    show_list(self.eroi)
                else:
                    arebani = False
        else:
            print("You don't have any more gold to hire a hero, here are your heroes: \n")
            show_list(self.eroi)

def start():
    os.system("clear")
    name1 = input("Before we start, please tell me your name. \n--> ")
    p1 = Player(name1)
    name2 = input("Wy thank you %s. Now tell me your opponent's name, please. \n" %p1.name)
    p2 = Player(name2)
    menu() 

def menu(Player, lista):
    os.system("clear")
    print("So... %s, today you will be battling.\n" %(Player.name))
    print("You have recieved 100 gold so let's hire some heroes to fight for you\n")
    print("Here are the avaliable heroes, choose wisely:\n")
    show_list_opt(lista)
    Player.complete_list(lista)
    os.system("clear")

def randomize(lista_eroi):
    random.shuffle(lista_eroi)
    show_list(lista_eroi)

def afisare_eroi(Player):
    print("The heroes fighting for %s are:"%(Player.name) )
    randomize(Player.eroi)
    
class Game():
    p1 = Player("CeVA")
    p2 = Player("Dax")

    jucatori = [p1, p2]

    pA = 0
    eA = 0 #(indexul eroului activ)

    def check_activ(pA):
        if  jucatori[pA].eroi[eA].HP == 0:
            eA += 1
        else:
            print("Eroul tau activ este: %s" %jucatori[pA].eroi[eA].name)
        return jucatori[pA].eroi[eA]

    def do_turn():
        #show liste eroi
        afisare_eroi(p1)                                                                    
        afisare_eroi(p2)
        if pA == 0:    
            #show erou activ (vf si daca are viata)
            check_activ(pA)
            #get input erou pe care il ataca
            alegere = int(input("%s, pick the hero you want to atack. \n" %jucatori[pA].name))
            #take_damage 
            take_damage(p2.eroi[alegere], p1.eroi[eA].damage)
            pA = 1
        else: 
            #invers
            playerActive = p1


def check_hero_life(jucatori):
    if jucatori[0].eroi[0].HP > 0:
        print("Erou activ")
        attack(jucatori)
    else:
        jucatori[0].eroi[0].HP = 0
        print("%s has been killed"%jucatori[0].eroi[0].name)
        jucatori[0].eroi.pop(0)
        attack(jucatori)


def attack(jucatori):  
    alegere = int(input("%s, you will atack with %s. Pick the one you want to atack. \n" %(jucatori[0].name, jucatori[0].eroi[0].name)))
    if alegere > len(jucatori[1].eroi)-1:
        print("Please choose a number under %s" %len(jucatori[1].eroi))
        attack(jucatori)
        #alegere = int(input))
        #show_list(jucatori[1].eroi)
    else:
        Unit.take_dammage(jucatori[1].eroi[alegere], jucatori[0].eroi[0].damage)
        show_list(jucatori[0].eroi)
        show_list(jucatori[1].eroi)
        if jucatori[1].eroi[alegere].HP < 0:
            print("%s has been killed"%jucatori[1].eroi[alegere].name)
            jucatori[1].eroi.pop(alegere)
        else:
            print("Hero still alive, let's continue.")
        jucatori[0].eroi += [jucatori[0].eroi.pop(0)]
        jucatori += [jucatori.pop(0)]
    
def fight(jucatori):
    #vieti = []
    #for i in range(len(jucatori[0].eroi)):
    #    vieti.append(jucatori[0].eroi[i].HP)
    #x = sum(vieti)
    while len(jucatori[0].eroi) > 0:
        os.system("clear")
        print("Here are %s's heroes"%jucatori[1].name)
        show_list(jucatori[1].eroi)
        check_hero_life(jucatori)       
    else:
        print("GAME OVER!!!! \n %s won!!!"%jucatori[1].name)

if __name__ == '__main__':

    print(Spadasin.create_unit())
    os._exit(1)
     ############################## Instantiere Unitati (Eroi) ####################################################
    
    p = Prastier()
    g = Gardian()
    s = Spadasin()
    a = Arcas()
    h = Hoplit()
    cal = Calaret()
    cav = Cavaler()
    cent = Centaur()
    cic = Ciclop()

    ############################### Sfarsit Clas Unit  ###############################################################
    k = [p, g, s, a, h, cal, cav, cent, cic]

    
    #######################################     START     ##########################################################
    #for cls in Unit.__subclasses__():
    #    for cl in cls.__subclasses__():
            #show_list(cl)
    #        cl.show_cost()
            #v = cl.__dict__.keys()
            #x = self.create_unit()
            #print(x)
        #print(cls.cost, show_list(subs))
            #print(cl.cost)
    #print(Arcas.show_cost)
    #os._exit(1)
    os.system("clear")
    
    name1 = input("Before we start, please tell me your name. \n--> ")
    p1 = Player(name1)
    name2 = input("Wy thank you %s. Now tell me your opponent's name, please. \n" %p1.name)
    p2 = Player(name2)

    #set_screen()
    #player_choice()
    #start()
    #player_start = random_player(players)           ca sa alegem cine ataca primul


    ############################## Afisare erou cu toate statisticile #############################################  
    menu(p1, k)
    os.system("clear")
    print("Good luck... now is %s's turn to choose!"%p2.name)                   #functia cu timpul sa apara scrisul ca si cand atunci ar fi tastat
    menu(p2, k)   
    os.system("clear")
    #print("The heroes fighting for %s are:"%(p1.name), " "*10, "The heroes fighting for %s are:"%(p2.name))   cum fac sa impart ecranul in 2?
    
    ##################################################### Cine incepe ############################################################################
    jucatori = [p1, p2]
    print_game(p1.eroi, p2.eroi, jucatori[0], jucatori[1])
    print("%s will be the fist to atack" %random.choice(jucatori).name)
    ind = jucatori.index(random.choice(jucatori))
    if ind == 0:
        #fight()
        print(list(jucatori))
    else:
        jucatori += [jucatori.pop(0)]
        #fight()
        print(jucatori[0].name)
    
    
    afisare_eroi(p1)                              #afiseaza lista eroilor deja randomizata!!!!                                      
    afisare_eroi(p2)
    ###################################################### Lupta #################################################################################
    os.system("clear")

    pprint(jucatori)
    os._exit(1)
    fight(jucatori)
    #check if player still active
    #check if hero still active
    #atack
    #take turn
            




    os._exit(1)
    #def create_copy():
