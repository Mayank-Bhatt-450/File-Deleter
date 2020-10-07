import time
import os
print '------------------------------------------------------------------------------'
print ' DESTROYER                             '
print '------------------------------------------------------------------------------'
time.sleep(0.5)
print '''
 If The File To Be Deleted Is In The Same Folder Of The Destroyer
 
 Then No Need To Write The Etension Of The File, Name Is Enough !

 
'''
time.sleep(0.5)
while True :
    try:
        print
        n=raw_input(' Enter the name along with extension of the file to be destroyed : ')
        if n=='self-destruct' :
            x=open('Destroyer.py','w')
            x.close
            print
            print ' Self Destruct started       Bye  Bye'
            print
            print ' Destroying .',
            for i in range(12):
                time.sleep(0.5)
                print '.',
            print
            print
            print ' I am nothing more than an empty file'
            print
            time.sleep(0.5)
            print ' Press enter to exit . . . . . . . !'
            raw_input()
        else :
            os.remove(n)
            print
            print
            print ' Destroying  file .',
            for i in range(8):
                time.sleep(0.5)
                print '.',
            print
            print
            print ' File has been destroyed'
            print
            time.sleep(0.5)
            print ' Press enter to exit . . . . . . . !'
            raw_input()
        break
    except :
        print
        print ' You entered invalid file name '
        continue

