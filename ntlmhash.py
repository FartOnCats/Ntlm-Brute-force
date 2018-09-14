import hashlib 
import os
import random
import binascii
import datetime
starttime = datetime.datetime.now()
def ntlm_attack(filestring):
    input2 = raw_input("input hash to crack: ")

    #dict = ["test","fuck","password","cracker"]
    with open(filestring) as file: # Use file to refer to the file object
        #data = file.readlines()
        for i in file.readlines():    
            i = i.rstrip("\n")
            #print(i.replace(" ", ""))
            
            try:
                passhash = hashlib.new('md4', i.encode('utf-16le')).digest()
                passhash = binascii.hexlify(passhash)
            except UnicodeDecodeError:
                print("unicode error found, a character probably isnt english: " + i)
            
            if(str(passhash).upper() == input2.upper()):
                print("password found! Password is: " + i)
                file.close()
                break
        print "done"
    file.close()
    endtime = datetime.datetime.now()
    timedifference = endtime-starttime;
    a = divmod(timedifference.days * 86400 + timedifference.seconds, 60)
    print str(a[0])+":"+str(a[1])
filepath = raw_input("Wordlist name and path: ")
ntlm_attack(filepath)
