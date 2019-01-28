class ClassA():

    def __init__(self):
        self.example = "Superclass"


    def my_method(self, a, b):
        print("This is " + str(a) + " and " + str(b))


class ClassB(ClassA):

    def my_method(self, a):
        print("This is only " + str(a))



if __name__ == "__main__":

    object_a = ClassA()
    object_b = ClassB()


    object_a.my_method("fish", "chips")

    object_b.my_method("potatoes")
    object_b.my_method("fish", "chips")

    
    
