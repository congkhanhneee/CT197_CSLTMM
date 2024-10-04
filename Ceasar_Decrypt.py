def read_file(dt):
    file=open(dt, "r")
    data=file.read()
    file.close()
    return data
def  decryt_ceasar(text,left,dt): #Giải Mã
    text_decry=""
    for i in text:
        if i.isalpha():
            if i.isupper():
                ascii_ofset=65
            else:
                ascii_ofset=97
            char_decry=chr((ord(i)-ascii_ofset-left)% 26+ascii_ofset)
            text_decry+=char_decry
        else:
            text_decry+=i
    file=open(dt,"w")
    data=file.write(text_decry)
    file.close()
dt=input("Nhap duong dan file can giai ma: ")
data=read_file(dt)
left=int(input("Nhap khoa k: "))
file=input("Nhap vao duong dan can luu plaintext: ")
decryt_ceasar(data,left,file)
