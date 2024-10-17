bought=int(input("price:"))
sell=int(input("sold:"))
if sell>bought :
    print("You made a prophit")
    num=sell-bought
    print("you made :",num)
else:
    print("You made a loss")
    num=sell-bought
    print("You lost :",num)