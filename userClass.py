class User:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def print_user(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Age: ", self.age)


# Driver function to test the User class
def main():
    # Create a User object
    user1 = User("John Doe", 5000, 30)
    
    # Call the print_user method to display the user's details
    user1.print_user()

# Run the driver function
main()