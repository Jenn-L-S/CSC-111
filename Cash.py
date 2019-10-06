# Jennifer Smith

# Here is where the amount needed is input.
amount = eval(input('Enter amount to break down into bills: '))
print("Amount: $" + str(amount))

# Here is where Cash.py will break down the amount into various bills and those
# bills will be counted. The assigned bills (n100/50/20/etc) must be converted
# to strings in order to print.
n100 = amount // 100
amount = amount - n100 * 100
print("100s: " + str(n100))

n50 = amount // 50
amount = amount - n50 * 50
print("50s: " + str(n50))

n20 = amount // 20
amount = amount - n20 * 20
print("20s: " + str(n20))
 
n10 = amount // 10
amount = amount - n10 * 10
print("10s: " + str(n10))

n5 = amount // 5
amount = amount - n5 * 5
print("5s: " + str(n5))

n1 = amount // 1
amount = amount - n1 * 1
print("1s: " + str(n1))

# Here we assign the remaining amount to the "Check", to make sure that
# the remainder is 0. As an int, Check does need to be converted to a string
# so that it may be printed.
Check = amount
print("Check: The amount remaining is " + str(Check) + ".")
