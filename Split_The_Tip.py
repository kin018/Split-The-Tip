meal=float(input("Enter dinner amount?: "))
guests=int(input("Enter number of guest:"))
tip= 1.15 #Tip amount...In this example we use 15%
total_cost= (meal/guests) * tip
print("With Tip, you each pay:$ %.2f" % total_cost)