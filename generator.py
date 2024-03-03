################################################
##                                            ##
## #########  #########  #########  ###   ### ##
## ##         ##     ##  ##         ###   ### ##
## #########  #########  #########    #####   ##
## ##         ##     ##         ##     ###    ##
## #########  ##     ##  #########     ###    ##
##                                            ##
## #########  #########  #########  ######### ##
## ##     ##  ##     ##  ##         ##        ##
## #########  #########  #########  ######### ##
## ##         ##     ##         ##         ## ##
## ##         ##     ##  #########  ######### ##
##                                            ##
################################################

#Import generator
import random

#Password include this:
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowercase = uppercase.lower()
symbols = '~`!@#$%^&*№;:?{}[]()/\\|+-='
numbers = '1234567890'

#Enable this all:              #You can off symbols there:
upper, lower, symbol, number = True, True, False, True

#Zero symbol of password
passwordcontained = ''

#Calculating password
if upper:
    passwordcontained += uppercase
if lower:
    passwordcontained += lowercase
if symbol:
    passwordcontained += symbols
if number:
    passwordcontained += numbers

#Length of password
length = 16

#Randomize password and print it
for passwordfunc in range(1):
    password = "".join(random.sample(passwordcontained, length))
    print(password)