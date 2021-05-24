def MathChallenge(strParam):


  # code goes here
    strParam=strParam.replace('x','j').replace('=','-(')+')'
    try:
        transformado = eval(strParam, {'j': 1j})
        real, imag = transformado.real, -transformado.imag
        return (real/imag)

    except SyntaxError:
        return 0        
  

# keep this function call here 
print(MathChallenge('1 + 1111 = x112'))