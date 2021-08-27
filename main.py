import random
import string
from time import sleep

length = int(input('Password Length: '))
counter = 1
while True:
    if counter == 20000:
        print('Enter Y To Continue Infinite Times(This May Hang Your Device  If You Have Low Ram And Continue Running This Programme More then 10 Minutes!\nEnter N To Stop The Programme!')
        ui = input('Your Reply: ')
        if ui =='Y':
            break
        elif ui == 'N':
            pass
        else:
            print('Wrong Input!')
            sleep(1)
    password = ''.join(random.choice(string.ascii_letters + string.punctuation) for i in range(length))
    print('Password No',counter,'is :',  password)
    counter+=1