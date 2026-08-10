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

def validate_credit_card(cc_dict):
    valid = cc_dict['valid format']
    final_valid  = []
    step1_valid = []
    final_sum = []
    
    for num in valid:
        count = 0
        temp_list = []
        temp_str = ""
        while count < len(num):
            if count % 2 == 0:
                double = int(num[count])*2
                if double >=10:
                    double = str(double)
                    double = int(double[0]) + int(double[1])
                temp_list.append(double)
            else:
                temp_list.append(num[count])
            count += 1
        for i in temp_list:
            temp_str += str(i)
        step1_valid.append(temp_str)
    for i in step1_valid:
        total = 0
        for digit in i:
            total += int(digit)
        final_sum.append(total)
    for i in range(len(valid)):
        if final_sum[i] % 10 == 0:
            final_valid.append(valid[i])
    return(final_valid)
    #print(valid)
    #print(step1_valid)
    #print(final_sum)
    #print(final_valid)


#test_list = readcc("chkcc.txt")
#cc_dict = checkcc_format(test_list)
#validate_credit_card(cc_dict)