#Movie Ticket Hw1
#Patrick Leimer 01/25/24

print("Available movies today:\nA)12 Strong: 1)2:30 2)4:40 3)7:50 4)10:50\nB)Coco: 1)12:40 2)3:45\nC)The Post: 1)12:45 2)3:35 3)7:05 4)9:55")

movChoice = input("Movie choice: ")
movTime = int(input("Showtime: "))
duePayment = 0
showTimesA, showTimesB, showTimesC = 4, 2, 4
#max amount of tickets purchased at one time is 30, so tickets can't be <30
if( ((movChoice == 'A' and movTime <= showTimesA) or (movChoice == 'B'and movTime <= showTimesB) or (movChoice == 'C' and movTime <= showTimesC)) and movTime != 0 ):
    adultTic, kidsTic = int(input("Adult tickets: ")), int(input("Kid tickets: "))

    if(adultTic < 30 and kidsTic < 30):
        if(movChoice == 'A'):
            duePayment = (adultTic*12.45) + (kidsTic*9.68)
            print("Total cost: $", duePayment)
        if(movChoice == 'B'):
            if(movTime == 1):
                duePayment = (adultTic*11.17) + (kidsTic*8)
                print("Total cost: $", duePayment)
            else:
                duePayment = (adultTic * 12.45) + (kidsTic * 9.68)
                print("Total cost: $", duePayment)
        if(movChoice == 'C'):
            if(movTime == 1):
                duePayment = (adultTic*11.17) + (kidsTic*8)
                print("Total cost: $", duePayment)
            else:
                duePayment = (adultTic * 12.45) + (kidsTic * 9.68)
                print("Total cost: $", duePayment)

    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")