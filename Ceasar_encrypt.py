def read_file(dt):
    file=open(dt, "r")
    data=file.read()
    file.close()
    return data
def encryt_ceasar(text,shift,dt): #Mã hóa
    text_encry=""
    for i in text:
        if i.isalpha():
            if i.isupper():
                ascii_ofset=65
            else:
                ascii_ofset=97
            char_encry=chr((ord(i)-ascii_ofset+shift)%26+ascii_ofset)
            text_encry+=char_encry
        else:
            text_encry+=i
    file=open(dt,"w")
    data=file.write(text_encry)
    file.close()
dt=input("Nhap duong dan file can ma hoa: ")
data=read_file(dt)
shift=int(input("Nhap khoa k: "))
file=input("Nhap noi can luu: ")
encryt_ceasar(data,shift,file)
