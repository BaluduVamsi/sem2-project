import random
class Rock_Paper_Scissor:
    
    options=["rock","paper","scissor"]

    def __init__(self):
        self.no_of_games=0
        self.player_wins=0
        self.computer_wins=0

    def generator(self):
        return random.choice(Rock_Paper_Scissor.options)
    
    def verification(self,comp_choice,user_choice):
        if comp_choice==user_choice:
            self.no_of_games+=1
            return "its a draw!"
        if comp_choice=="rock":
            if user_choice=="paper":
                self.player_wins+=1
                self.no_of_games+=1
                return "user won!"
            else:
                self.computer_wins+=1
                self.no_of_games+=1
                return "computer won!"
        elif comp_choice=="paper":
            if user_choice=="scissor":
                self.player_wins+=1
                self.no_of_games+=1
                return "user won!"
            else:
                self.computer_wins+=1
                self.no_of_games+=1
                return "computer won!"
        else:
            if user_choice=="rock":
                self.player_wins+=1
                self.no_of_games+=1
                return "user won!"
            else:
                self.computer_wins+=1
                self.no_of_games+=1
                return "computer won!"
           
user=Rock_Paper_Scissor()
num=int(input("no of games: "))
print()
while(num!=0):
    string1=input("Rock/Paper/Scissor\nuser choice: ").lower()
    if string1!="rock" and string1!="paper" and string1!="scissor":
        print("invalid choice!")
        print()
        continue
    string2=user.generator()
    print(f"computer choice: {string2}")
    print(user.verification(string2,string1))
    num-=1
    print()
print(f"no of games played: {user.no_of_games}")
print(f"player wins: {user.player_wins}")    
print(f"computer wins: {user.computer_wins}")
print("over all->user won" if user.player_wins>=user.computer_wins else "over all->computer won")
 