print("-----------Day12----------")

#switch case
n=input("enter element : ")
match n:
    case "sunday":
        print("Today is weekend",n)
    case "monday":
        print("working day",n)
    case "tuesday":
        print("working day",n)
    case "wednesday":
        print("working day",n)
    case "thrusday":
        print("working day",n)
    case "friday":
        print("working day",n)
    case "saturday":
        print("weekend",n)
    case _ if n!="hhhh":
        print("value not found")
    case _:
        print("not matched")
    