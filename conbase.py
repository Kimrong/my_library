def fromDecimal(num, base):
    result=[]
    try:
        while(divmod(num,base)!=(0,0)):
            result.append(num%base)
            num/=base
            num=int(num)
        result.reverse()
        int_result = int(''.join(map(str, result)))
        return int_result
    except ZeroDivisionError as e:
        print(e)

def toDecimal(num, base):
    list_num=[int(digit) for digit in str(num)]
    list_num.reverse()
    result=0
    for x in range(0,len(list_num)):
        result+=list_num[x]*(base**x)
    return result

def convertBase(num, before_base, after_base):
    if before_base==10:
        return fromDecimal(num,after_base)
    elif after_base==10:
        return toDecimal(num,before_base)
    else:
        num=toDecimal(num,before_base)
        return fromDecimal(num,after_base)
