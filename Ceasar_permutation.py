def read_file(dt):
    file=open(dt, "r")
    data=file.read()
    file.close()
    return data
    

def read_file_key(dt):
    try:
        with open(dt,"r") as files:
                list_permute_supper=files.readline()
                if list_permute_supper.islower():
                    list_permute_supper=list_permute_supper.upper()
                list_permute_lower=files.readline()
                if list_permute_lower.isupper():
                    list_permute_lower.lower()
        return list(list_permute_supper),list(list_permute_lower)
    except FileNotFoundError:
        print("File khong ton tai. \n")
    except Exception as e:
        print(f"Da xay ra loi {e}")
        
def ceasar_encryt_permute(list_permute_supper,list_permute_lower,data_plaintext,path_encrypt):
    list_encrypt=[]
    list_alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_alphabet_lower='abcdefghijklmnopqrstuvwxyz'
    for i in data_plaintext:
        if i.isalpha():
            if i.isupper():
                if i in list_alphabet_upper:
                    position=list_alphabet_upper.index(i)
                    new_position=(position)%26
                    list_encrypt.append(list_permute_supper[new_position])
            else:
                if i in list_alphabet_lower:
                    position=list_alphabet_lower.index(i)
                    new_position=(position)%26
                    list_encrypt.append(list_permute_lower[new_position])
        else:
            list_encrypt.append(i)
    file=open(path_encrypt, "w")
    data=file.write(''.join(list_encrypt))
    file.close()

dt=input("Nhap duong dan file can ma hoa: ")
data_plaintext=read_file(dt)
key_permute=input("Nhap vao duong dan luu bang hoan vi: ")
list_permute_supper, list_permute_lower=read_file_key(key_permute)
# print(list_permute_supper,list_permute_lower)
path_encrypt=input("Nhap vao duong dan luu file ma hoa: ")
ceasar_encryt_permute(list_permute_supper,list_permute_lower,data_plaintext,path_encrypt)
