#!/usr/bin/python3

# parse and return number of failed login attempts

loginfail = 0
keystone_file = open("/home/student/mycode/2025-01-mycode/attemptlogin/keystone.common.wsgi","r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()

for line in keystone_file_lines:
    if"- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed login attempts is: ", loginfail)
keystone_file.close()
