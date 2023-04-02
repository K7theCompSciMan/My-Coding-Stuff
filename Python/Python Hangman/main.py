import functions, random
print("Welcome to HangAardvark! All letters are lowercase fyi.")
list_of_words = ['wassup']
word = random.choice(list_of_words)
functions.board()
count = 0
right = 0
for i in range(6):
  letterguess = functions.guess()
  yesorno = functions.correct(letterguess,word)
  if yesorno == "No":
    count= count+1
    if count == 1:
      functions.head()
      continue
    elif count == 2:
      functions.body()
      continue
    elif count == 3:
      functions.lleg()
      continue
    elif count == 4:
      functions.rleg()
      continue
    elif count == 5:
      functions.larm()
      continue
    elif count == 6:
      functions.rarm()
      continue
  else:
    right +=1
if right == len(word):
  print("GOOD JOB YOU GUESSED THE WORD!")
else:
  print("NICE TRY, BUT YOU LOST!")
