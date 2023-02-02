class library:
    # def __init__(self): #it is a constructor in python
         # self.name=x
    lib=[]
    def gett(self,x):
        self.bok=x
        self.lib.append(self.bok) #appending the book name in the list
           
    def noOfBook(self):
        return self.lib #returning the lib list
    
    def show(self):
        print(f"Book is { self.lib}") 
      
print("*********Library Management*************")
print("1. Add Books")
print("2. No of Book")
print("3. Print Books")
print("4. Exit")

obj=library() #create library obj
while True:
    x=int(input("Enter Your Opction : "))

    if(x==1):
        book=input("Enter Book Name : ")
        obj.gett(book)#passing book to list
    elif(x==2):
        print(f"No of Book is : {len(obj.noOfBook())}")#getting no of book
    elif(x==3):
        obj.show() #display all book name
    else:
        print("wrong input")
        exit()
    if(x>3):
        break
        
        

