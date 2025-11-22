# This is Used to Automation Library
import os

#for checking the current directory path in which you are working
print(f"Current Working Directory : {os.getcwd()}")

#for changing the directory
os.chdir("E:\Devops")
print(f"Current Working Directory : {os.getcwd()}")
os.chdir("E:\Devops\Python-Scripting")
print(f"Current Working Directory : {os.getcwd()}")
print(f"List of files in currect location", os.listdir())
