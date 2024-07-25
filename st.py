
import string
import random
 
s = input ("Enter your statement: ")
words = s.split (" ")
nwords = []

q = int (input ("Enter 1 for Coding & 0 for Decoding: "))

coding = True if q==1 else False
if (coding):
    for word in words:
        if len(word) >=3:
            r1 = ''.join(random.choices(string.ascii_letters, k=3))
            r2 = ''.join(random.choices(string.ascii_letters, k=3))
            s1 = r1 + word[1:] + word[0] + r2
            nwords.append(s1)

        else:
            nwords.append(word[::-1])
        
    print (' '.join(nwords))
else:
    for word in words:
        if len(word)>=3:
            s2 = word[-4] + word[3:-4] 
            nwords.append (s2)

        else:
            nwords.append(word[::-1])
    print (' '.join(nwords))

