import os

#open() to open a file from a directory
#read() to read the content of file
file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")
if(os.path.exists("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")):
    print(file.read())
else:
    print("file does not exists")
#close() to close the file to free up memory
file.close()

file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")
file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")
if(os.path.exists("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")):
    #readline() to read a line from a file
    print("Reading a line")
    print(file.readline(15))
else:
    print("file does not exists")
file.close()

#open a file in append mode
#file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md", "a")
#file.write("    - Basic syntax & fundamentals of python")
#file.close()

print("Reading the file after writing")
file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")
if(os.path.exists("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\README.md")):
    print(file.read())
else:
    print("file does not exists")
file.close()

#create a new file with
if(os.path.exists("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt")):
    print("file already exists")
else:
    file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt", "a")
file.close()

file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt")
print(file.read())
file.close()

#file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt", "a")
#file.write("Python code is writing again & again")
#file.close()

file = open("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt")
print(file.read())
file.close()

#os.remove to remove the file when
print("removing the file demo.txt...")
os.remove("C:\\Users\dhiraj.solanki\Desktop\Dhiraj\Dhiraj\Projects\LearningPython\demo.txt")


