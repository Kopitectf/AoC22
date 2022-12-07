import os 
import time

parent_dir = '/home/kopite/Desktop/aco22/day7'
with open ("input.txt", "r") as input:
    Lines = input.readlines()
    for line in Lines:
      command = line.split()

      if 'cd' == command[1]:
        time.sleep(.1)
        working_dir = os.getcwd()
        if command[2] == '/':
          os.chdir(parent_dir+'/fs')
        elif command[2] == '..':
          os.chdir('..')
        else:
          os.chdir(working_dir+'/' + command[2])

      elif 'ls' == command[1]:
        time.sleep(.1)

      else:
        time.sleep(.1)
        if command[0] =='dir':
          os.mkdir(command[1])
          print(f" mkdir {command[1]} result: {os.path.exists(command[1])}")
        else:
          with open(command[1], 'w') as outfile:
            outfile.write(command[0])
