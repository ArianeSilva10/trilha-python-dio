def calculadora(operacao):
    def soma(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mult(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
    match operacao:
        case "+":
            return soma
        
        case "-":
            return sub
        
        case "*":
            return mult
        
        case "/":
            return div
    

# retorna a referência destas funções internas
print(calculadora("+"))
print(calculadora("-"))
print(calculadora("*"))
print(calculadora("/"))


# formas de saídas com a função

print(calculadora("+")(2, 3))

op = calculadora('-')
print(op(2, 3))

op = calculadora('*')
print(op(2, 3))

op = calculadora('/')
print(op(2, 3))

