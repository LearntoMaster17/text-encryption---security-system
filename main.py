# Coding & Decoding Challenge:

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string
# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import random, string

a = input("Enter the message: ")
o = int(input("If you want to Code type- 0 OR Decode type- 1: "))

def code(m):
    x = []
    msglist = m.split(' ')
    for wrd in msglist:
        if len(wrd) <= 2:
            y = wrd[::-1]
            x.append(y)
        else:
            z = wrd[1:] + wrd[0]
            char = string.ascii_letters + string.digits       # a-zA-Z + 0-9 = a-zA-Z0-9
            r = ''.join(random.choices(char, k=3))            # random.choices returns a list of any 3 random characters from char.
            l = ''.join(random.choices(char, k=3))            # join is used to join list of string which is returned by random.choices()
            z1 = r+z+l
            x.append(z1)
    print(*x)

# print(string.ascii_letters)                                        output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)                                               output: 0123456789
# print(random.choices(string.ascii_letters + string.digits, k=3))   output: ['G', 'm', '3']  (random output)

def decode(m):
    x = []
    msglist = m.split(' ')
    for wrd in msglist:
        if len(wrd) <= 2:
            y = wrd[::-1]
            x.append(y)
        else:
            z = wrd[3:-3]
            z1 = z[-1] + z[:-1]
            x.append(z1)
    print(*x)

if o == 0:
    code(a)
elif o == 1:
    decode(a)
else:
    ("Invalid input")
