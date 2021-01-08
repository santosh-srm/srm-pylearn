""" 25_simple_if.py """

name = input("enter your name : ")
message = "Hello friend!"

if(name != ""):
    message = f'{name}!'
print(message)

if(name == ""):
    message = input(f'Name can''t be empty. Enter name: ')

print(f'The entered name is: {message}')   

"""
Output
enter your name : Samarth
Samarth!
The entered name is: Samarth!
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/25_simple_if.py
enter your name : 
Hello friend!
Name cant be empty. Enter name: Sandy
The entered name is: Sandy
"""