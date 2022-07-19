import random



play=True
while (play==True):
  num=random.randint(1,10)
  win=False
  attemps=5
  while (attemps>0):
    guess= int( input("guess the number:  "))
    if (guess==num):
        win=True
        break
    else:
      print("nope")
      print(f" {attemps} attempts left")
      attemps -=1
  if (win==True):
    print("Congrats! you won")
    print(f"you got it in {6-attemps} tries")
  else:
    print("you lose")
  answer=input("do you want to play again?")
  if (answer.upper()=="YES"):
    play=True
  else:
    play=False
