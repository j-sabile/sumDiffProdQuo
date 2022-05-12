def evaluate(x, y):
    print("\nSum:", list[x] + list[y])
    print("Difference:", list[x] - list[y])
    print("Product:", list[x] * list[y])
    print("Quotient:", list[x] / list[y])
    print("Quotient w/out decimal places:", list[x] // list[y], "\nRemainder:", list[x] % list[y], "\n")

while 1:
    list = []
    try:
        list.append(int(input("1st number: ")))
        list.append(int(input("2nd number: ")))
        list.append(int(input("3rd number: ")))
        break
    except:
        print("Please enter only numbers.\n")

while 1:
    choice = input("\n[1] 1st and 2nd number\n[2] 2nd and 3rd number\n[3] 1st and 3rd number\nChoice: ")
    if choice == "1":
        evaluate(0,1)
        break
    elif choice == "2":
        evaluate(1,2)
        break
    elif choice == "3":
        evaluate(0,2)
        break
    else:
        print("Please enter a valid number.")
