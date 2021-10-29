###
### Author: Xin Li.
### Description: The first program named encrypter.py
### The job of this program will be to encrypt (“mix”
### or “shuffle”) the lines of a text file, but do it
### in such a way that it can be un-done later with a
### separate program (which you will also write).
###
import random
def main():
    random.seed(125)
    file_name = input('Enter a name of a text file to encrypt:\n')
    file = open(file_name, 'r')
    lst_text = []
    lst_index = []
    encryted = open('encrypted.txt', 'w')
    index = open('index.txt', 'w')
    lines = file.readlines()
    i = 1
    for line in lines:
        lst_text.append(line)
        lst_index.append(i)
        i += 1
    for count_2 in range (5):
        for count in range (len(lst_index)):
            a =  random.randint(0,i-2)
            b =  random.randint(0,i-2)
            k = lst_index[a]
            lst_index[a] = lst_index[b]
            lst_index[b] = k
            c = lst_text[a]
            lst_text[a] = lst_text[b]
            lst_text[b] = c
    string_text = ''
    string_index = ''
    for k in range(len(lst_index)):
        encryted.write(str(lst_text[k]))
        index.write(str(lst_index[k])+'\n')
    index.close()
    encryted.close()
    file.close()
main()
