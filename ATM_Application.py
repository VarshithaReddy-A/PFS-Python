bal=100000
card=input("Enter the card (c):")
if card=="c":
    print("welcome pooja")
    pas=int(input("Enter Password:"))
    if pas==1234:
        print("1.Balance Enquiry 2.Withdraw ")
        option=int(input("Enter your choice:"))
        match option:
            case 1:
                print("Your account balance is:",bal)
            case 2:
                amount=int(input("Enter Withdraw Amount: "))
                if amount<=bal:
                    bal -= amount
                    print("Remaining Balance:",bal)
                else:
                    print("Insufficient Balance")
            case _:
                print("Invalid option")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Card!")
                
