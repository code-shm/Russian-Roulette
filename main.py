import random
import tkinter as tk
from tkinter import messagebox
import pygame
from pygame import mixer
from rounds import rounds
import config
def rounds():
    while(True):
        random_numbers = random.sample([1, 2, 3, 4, 5, 6], 3)
        #chambers = 6
        revolver = [0,0,0,0,0,0] 
        for num in random_numbers:
            revolver[num-1]=1
        bullets=3
        dud=3
        choice="dealer"
        for i in range(0,6):
            if choice=="dealer":
                num=1
                if(bullets>=dud):
                    num=1
                else:
                    num=0
                if(num==0)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-1
                    config.life_player=config.life_player-0
                    bullets=bullets-1
                    dud=dud-0
                    mixer.Sound("gunshot.wav").play()  # Play gunshot sound
                    messagebox.showinfo("Result", "Dealer shoots himself! Bang!! \n You win!! \n")
                    choice="dealer"
                if(num==0)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    mixer.Sound("click.wav").play()
                    messagebox.showinfo("Result", "Dealer shoots himself! It's a dud!! \n ")
                    choice="dealer"
                if(num==1)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-1
                    bullets=bullets-1
                    dud=dud-0
                    mixer.Sound("gunshot.wav").play()
                    messagebox.showinfo("Result", "Dealer shoots YOU! \nBang!! \nYou LOSE!! \n")
                    choice="player"
                if(num==1)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    mixer.Sound("click.wav").play()
                    messagebox.showinfo("Result", "Dealer shoots YOU! It's a dud!! \n ")
                    choice="player"
            else:
                chk=int(input("Whom do you want to shoot: \n Press 1 for Dealer \n Press 0 to test your luck "))
                if(chk==0)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-1
                    bullets=bullets-1
                    dud=dud-0
                    mixer.Sound("gunshot.wav").play()
                    messagebox.showinfo("Result", "YOU shoot yourself! \nBang!! \n You are dead \nYou LOSE!! \n")
                    choice="player"
                if(chk==0)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    mixer.Sound("click.wav").play()
                    messagebox.showinfo("Result", "YOU shoot yourself! \nIt's a dud!! \n ")
                    choice="player"
                if(chk==1)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-1
                    config.life_player=config.life_player-0
                    bullets=bullets-1
                    dud=dud-0
                    mixer.Sound("gunshot.wav").play()
                    messagebox.showinfo("Result", "You shoot the DEALER! \nBang!! \nDealer dies\n You win!! \n")
                    choice="dealer"
                if(chk==1)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    mixer.Sound("click.wav").play()
                    messagebox.showinfo("Result", "You shoot the DEALER! \nIt's a dud!! \n ")
                    choice="dealer"
            if(config.life_dealer==0):
                print("You win!!!")
                a=int(input("Press any key to continue: (0 to EXIT)"))
                return a
            elif (config.life_player==0):
                print("Dealer wins!!!")
                a=int(input("Press any key to continue: (0 to EXIT)"))
                return a
            if(i==5):
                return "NO"

# Initializing Pygame
pygame.init()
mixer.init()

# Constants
config.life_dealer = 3
config.life_player = 3

# Function to shoot
def shoot():
    num = random.randint(0, 1)
    return num

# Function to play one round of the game
def play_round():
    ans = rounds()
    if ans == "NO":
        messagebox.showinfo("Round", "Let's go for another round")
        root.after(100, play_round)  # Schedule next round
    elif ans == 0:
        messagebox.showinfo("Round", "Game Over!")
    else:
        messagebox.showinfo("Round", "You survived this round!")

# Function to shoot and display the result
""" def shoot_and_display():
    result = shoot()
    if result == 0:
        mixer.Sound("gunshot.wav").play()  # Play gunshot sound
        messagebox.showinfo("Result", "Dealer wins! You lose one life.")
    else:
        mixer.Sound("click.wav").play()  # Play click sound
        messagebox.showinfo("Result", "You win! Dealer loses one life.")
 """
# Creating Tkinter GUI
root = tk.Tk()
root.title("Russian Roulette Game")

# GUI Components
label = tk.Label(root, text="Russian Roulette Game", font=("Helvetica", 20))
label.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_round)
play_button.pack(pady=5)

""" shoot_button = tk.Button(root, text="Shoot", command=shoot_and_display)
shoot_button.pack(pady=5) """

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=5)

# Main loop
root.mainloop()
