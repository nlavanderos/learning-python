precio = 5
cadenas = ['(4+5)**2',
           '(1, 2, 3)',
           '["I", "II", "III"]',
           '{"a":1, "b":2, "c":3}',
           'len("Python")',
           '20 * precio',
           '__import__("platform").python_version()']

for cadena in cadenas:
   
    try:
         print(cadena, "=>", eval(cadena), "Tipo:",type(eval(cadena)))

    except SyntaxError:
        print('Se ha producido un error de sintaxis')