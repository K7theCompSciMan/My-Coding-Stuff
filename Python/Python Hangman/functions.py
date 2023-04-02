import turtle as t
def guess():
  while True:
    letterguess = input("Guess a letter: ")
    if letterguess.isalpha() and len(letterguess) == 1:
      return letterguess
    else:
      print("Please enter a single letter")

def board():
  t.penup()
  t.goto(-25,-50)
  t.pendown()
  t.left(90)
  t.forward(150)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(25)
  t.penup()
  
def head():
  t.goto(10,60)
  t.pendown()
  t.circle(15)
  t.penup()

def body():
  t.goto(25,45)
  t.pendown()
  t.forward(70)
  t.penup()
  
def lleg():
  t.goto(25,-25)
  t.pendown()
  t.right(45)
  t.forward(35)
  t.penup()

def rleg():
  t.goto(25,-25)
  t.pendown()
  t.left(90)
  t.forward(35)
  t.penup()
   
def larm():
  t.goto(25,20)
  t.pendown()
  t.right(135)
  t.forward(35)
  t.penup()
  
def rarm():
  t.goto(25,20)
  t.pendown()
  t.left(180)
  t.forward(35)
  t.penup()
  
def correct(guess,word):
  where = 'L'
  yes = False
  for letter in word:
    if guess == letter:
      yes = True
      where = word.index(letter)
      break 
    else:
      continue
  if yes == True:
    if where == 0:
      print(f"That letter is the {where+1}st of the word")
    elif where == 1:
      print(f"That letter is the {where+1}nd of the word")
    else:
      print(f"That letter is the {where+1}rd of the word")
    return("Yes")  
  else:
    print("Sorry, that letter is not in the word.")
    return("No")
    
    
      
