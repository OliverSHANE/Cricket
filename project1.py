import random
a=["Rock","paper","Scissor"]
computer_choice=random.choice(a)

computer_score=0
player_score=0

while True:
    player_choice=input("Enter your choice")
    if player_choice==computer_choice:
        print("tie")
        computer_score+=1
        player_score+=1
    elif player_choice=="Rock":
       if computer_choice=="paper":
           print("Computer wins")
           computer_score+=1
       if computer_choice=="Scissor":
           print("Player wins")
           player_score+=1
    elif player_choice=="Scissor":
        if computer_choice=="Rock":
           print("Computer wins")
           computer_score+=1
        if computer_choice=="paper":
            print("Player wins")
            player_score+=1
    elif player_choice=="paper":
        if computer_choice=="Scissor":
            print("Computer wins")
            computer_score+=1
        if computer_choice == "Rock":
            print("player wins")
            player_score += 1
    else:
        print("Final scores")
        print("player_score:", computer_score)
        print("computer_score:", computer_score)
        break