def readcc(txtfile):
    txt_list = []
    with open(txtfile, "r") as file:
        contents = file.readlines()
    for num in contents:
        num = num.strip("\n")
        txt_list.append(num)
    return txt_list

def checkcc_format(credit_cardnumList):
    cc_dict = {}
    invalid_list = []
    valid_list = []
    for cc in credit_cardnumList:
        if cc.isdigit() == True and len(cc) == 16:
            valid_list.append(cc)
        else:
            invalid_list.append(cc)
    cc_dict["invalid format"] = invalid_list
    cc_dict["valid format"] = valid_list
    return cc_dict
    #print(cc_dict)
#test_list = readcc("chkcc.txt")
#checkcc_format(test_list)