import random
import string


length = int(input('Password Length: '))
counter = 1
while True:
    password = ''.join(random.choice(string.ascii_letters + string.punctuation) for i in range(length))
    print('Password No',counter,'is :',  password)
    counter+=1