def readcc(txtfile):
    txt_list = []
    with open(txtfile, "r") as file:
        contents = file.readlines()
    for num in contents:
        num = num.strip("\n")
        txt_list.append(num)
    return txt_list
    #print(contents)
    #print(txt_list)
#readcc("chkcc.txt")