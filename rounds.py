import random
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
                    print("Dealer shoots himself! Bang!! \n You win!! \n")
                    choice="dealer"
                if(num==0)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    print("Dealer shoots himself! It's a dud!! \n ")
                    choice="dealer"
                if(num==1)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-1
                    bullets=bullets-1
                    dud=dud-0
                    print("Dealer shoots YOU! \nBang!! \nYou LOSE!! \n")
                    choice="player"
                if(num==1)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    print("Dealer shoots YOU! It's a dud!! \n ")
                    choice="player"
            else:
                chk=int(input("Whom do you want to shoot: \n Press 1 for Dealer \n Press 0 to test your luck "))
                if(chk==0)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-1
                    bullets=bullets-1
                    dud=dud-0
                    print("YOU shoot yourself! \nBang!! \n You are dead \nYou LOSE!! \n")
                    choice="player"
                if(chk==0)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    print("YOU shoot yourself! \nIt's a dud!! \n ")
                    choice="player"
                if(chk==1)and(revolver[i]==1):
                    config.life_dealer=config.life_dealer-1
                    config.life_player=config.life_player-0
                    bullets=bullets-1
                    dud=dud-0
                    print("You shoot the DEALER! \nBang!! \nDealer dies\n You win!! \n")
                    choice="dealer"
                if(chk==1)and(revolver[i]==0):
                    config.life_dealer=config.life_dealer-0
                    config.life_player=config.life_player-0
                    bullets=bullets-0
                    dud=dud-1
                    print("You shoot the DEALER! \nIt's a dud!! \n ")
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