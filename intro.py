class PythonIntro:
    def __init__(self, name):
        self.name = name
        print(f"Welcome {name}! Let's learn some Python!")
        
    def hello_world(self):
        print("Hello, World!")
        
    def variables(self):
        x = 5
        y = 7
        z = x + y
        print(z)
        
    def loops(self):
        for i in range(10):
            print(i)
            
    def conditionals(self, age):
        if age >= 18:
            print("You are an adult.")
        else:
            print("You are a minor.")
            
intro = PythonIntro("John")
intro.hello_world()
intro.variables()
intro.loops()
intro.conditionals(21)
