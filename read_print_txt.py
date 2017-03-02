#Python program to read and print the lines of a text file

def main():
    #reading the file
    file = open("C:\\Users\\mono\\Desktop\\hd.txt","r")
    lines = file.readlines()
    file.close()
    
    for line in lines:
        print (line)

main()