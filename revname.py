# Function which accepts the user's first and last name and prints them in reverse
def getname():
    fname = input('Enter your First Name:')
    lname = input('Enter your Last Name:')
    print(f'Reversed Name is {lname [::-1]} {fname[::-1]}')
