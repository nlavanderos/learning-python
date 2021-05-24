#https://www.florin-pop.com/blog/2019/03/jcc-regular-brackets/
def regularBrackets(b) :
    equal = 0
    for i in range(len(b)):
        if b[i] =='(':
            equal+=1
        elif b[i] ==')':
            equal -= 1
    
    return print(equal == 0)


brackets="()()(((())))"
regularBrackets(brackets)