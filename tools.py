#Chooses which file to change, creates empty file if file does not exist
#Option 1
def chooseFile():
    file = input("\nWhat file would you like to change?\n")
    my_file = open(file, "a")
    my_file.close()
    return file

#Capitalize all letters in file
#Option 3
def capitalizeAllLetters(filename):
    with open(filename, mode='r+') as f:
       content = f.read()
       f.truncate(0)
       f.seek(0)
       contentUpdated = content.upper()
       f.write(contentUpdated)
       f.close
        
        
        

#Removes every other character from a text file
#Option 8
def removeEveryOtherChar(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        i = 0
        contentUpdated = ""
        for char in content:
            if char.isalpha() or char.isnumeric():
                if (i % 2) == 0:
                    contentUpdated += char
                i += 1 
            else:
                contentUpdated += char
        f.write(contentUpdated)
        f.close




#Replace every character in the file with it's ascii value
#Option 10
def replaceCharacterWithAscii(filename):
    with open(filename, mode='r+') as f:
        content = f.read()
        f.truncate(0)
        f.seek(0)
        contentUpdated = ""
        for char in content:
            contentUpdated += str(ord(char)) + '\n'
        f.write(contentUpdated)
        f.close