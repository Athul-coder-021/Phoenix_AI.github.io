try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)

except Exception as e:
    print("An error occurred:", e)