#!/usr/bin/python3

import os
os.system("tput setaf 1")
os.system("tput setab 4")

print("\t\t welcome to TTS Menu")
x="""
Press1 : To continue...
  """
print(x)
ch=input("enter your choice:")
if int(ch)==1:


	x=input("enter what u want to say :")
	os.system("espeak ,{0}".format(x))
 
