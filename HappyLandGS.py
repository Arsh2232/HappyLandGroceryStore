print("Welcome to HappyLand Grocery Stroe!")
userNumItem=input("please enter the number of items purchased to get discount: ")
while not userNumItem.isnumeric():
    userNumItem=input("You did not enter a digit. Please enter in digits: ")

userNumItem=int(userNumItem)
userInp = input("Please enter cost in dollar. For instance, 2.85 is Two Dollars and Eightyfive cents : ")
convCents = float(userInp)*100
if userNumItem<10:
    print("Total amount without discount is ", userInp,"\n You did not get any discount today:(")
elif userNumItem>=10 and userNumItem<=19:
    amount = 0.1*convCents
    amountD = amount/100
    print("You get 10 percent discount!\nTotal amount is", amountD )
elif userNumItem>=20 and userNumItem<=39:
    amount = 0.20*convCents
    amountD = amount/100
    print("You get 20 percent discount!\nTotal amount is ", amountD)
elif userNumItem>=40:
    amount = 0.40*convCents
    amountD = amount/100
    print("You get 40 percent discount and a free gift item!\nCollect your gift at the main desk\nTotal amount is",amountD)
print("Thank you for shopping at HappyLand Grocery! ")
