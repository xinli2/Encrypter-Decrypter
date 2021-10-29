###
### Author: Xin Li.
### Description: After writing encrypter.py, you
### are to write a related program named
### decrypter.py. decrypter.py will take the name
### of a text file and index (key) file, and then
### it will decrypt the text. The program will read
### in these two files, and using the information
### stored within them, it will put the contents back
### in the original order. The decrypted file should
### be saved to a file named decrypted.txt
###

def main():
    encrypted_file_name = input('Enter the name of an encrypted text file:\n')
    index_file_name = input('Enter the name of the encryption index file:\n')
    decrypted = open('decrypted.txt', 'w')
    file_text = open(encrypted_file_name, 'r')
    file_index = open(index_file_name, 'r')
    lines = file_text.readlines()
    index = file_index.readlines()
    lst =[]
    string_lst = ''
    for k in index:
        lst.append(' ')
    for i in range (len(index)):
        lst[int(index[i])-1] = lines[i]
    for count in range (len(index)):
        string_lst +=str(lst[count])
    decrypted.write(string_lst)
    decrypted.close()
    file_text.close()
    file_index.close()
main()
