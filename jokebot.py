joke='''Sophia is heading out to the grocery store.
 A programmer tells her: get a liter of milk, and if they have eggs, get 12.
   Sophia returns with 13 liters of milk.
The programmer asks why and Sophia replies: "because they had eggs"'''
# call it three time
def joke_bot():
    user_input=input(("What do you want : ")).lower()
    # use of if_else
    if user_input=="joke":
        print(joke)
    else:
        print("Sorry I only tell jokes")

joke_bot()
joke_bot()
joke_bot()

