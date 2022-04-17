import string
import random

password = string.ascii_letters + string.digits
char = ''
file = open("wordlist.txt" , "w")

for x in range(20):
    for x in random.sample(password,random.randint(8,8)):
        char+=x
    file.write(char+'\n')
    char=''
file.close()
print("Wordlist is saved!")

