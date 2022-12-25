print("-----------Day22----------")
letter="hey my name is {} and i am from {}"
letter="hey my name is {1} and i am from {0}"#we can also set index as a parameter
name="ramu"
country="indial"
print(letter.format(name,country))#it can pass value as a argument
price=40.444
print(f"price of dollar is {price:.2f}")#it will only print .after 2 digit
print(f"{2*4}")#we can use for calculation also