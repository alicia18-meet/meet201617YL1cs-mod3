#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

my_user=UserAccount('Alicia', 'alicia123', 'Im not vegan')

#Three things are missing from the line below - fill them in
#my_user=UserAccount('Alicia', 'alicia123', 'Im not vegan')

#Call the print_secret method (function) - it takes one input - a guess for the password.

    

#Use the wrong password as inp

my_user.print_secret('wrongpass') 

#Use the right password here
my_user.print_secret('alicia123')
