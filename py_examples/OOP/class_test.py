class Test:
    class_var = "class data"
    
    def __init__(self, *args): #constructer for Test
        print(len(args))
        if len(args) is 0:
            print("zero")
        elif len(args) is 1:
            print("one")
        elif len(args) is 2:
            print("two")

a = Test("a")
b = Test("b", "this")
c = Test(1, 2, 3)

print()
print("Test = ",Test.class_var)
print("a = ", a.class_var)
print("b = ", b.class_var)
print()

b.class_var = "changed string" 
Test.class_var = "test string" #will change all object class data if it has not been changed on that instance

print("Test = ",Test.class_var)
print("a = ", a.class_var) #note how the value of a changes because a.class_data has not been modified after construction
print("b = ", b.class_var)