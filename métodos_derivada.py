def f(x):
    return x**2 + 3*x + 5

def derivada_foward(x, delta):
    return (f(x + delta) - f(x))/delta

def derivada_foward_erroO2(x, delta):
    return (-f(x+2*delta)+4*(f(x+delta))-3*(f(x)))/(2*delta)

#derivada com erro O(delta³) ta com erro, tem q ver se a formula ta correta
def derivada_foward_erroO3(x, delta):
    return ((1/3)*f(x+3*delta)-(3/2)*f(x+2*delta)+3*f(x+delta)-(5/3)*f(x))/(1/delta)

def derivada_foward_segundaOrdem(x, delta):
    return (f(x+2*delta) - 2*f(x+delta) + f(x))/(delta ** 2)

def derivada_foward_terceiraOrdem(x,delta):
    return (f(x+3*delta)-3*f(x+2*delta)+3*f(x+delta)-f(x))/delta**3

def derivada_backward(x, delta):
    return (f(x) - f(x - delta))/delta

def derivada_backward_segundaOrdem(x, delta):
    return (f(x) - 2*f(x-delta) + f(x-2*delta))/(delta ** 2)

def derivada_central(x, delta):
    return (f(x + delta) - f(x - delta))/(2*delta)

def derivada_central_segundaOrdem(x, delta):
    return (f(x+2*delta)-2*f(x)+f(x-2*delta))/(4*(delta**2))

def printar(x, delta):
    print( 26 * '=')
    print("Derivadas de primera ordem")
    print( 26 * '=')
    print("Derivada Foward: ", end = "")
    print(derivada_foward(x,delta))
    print("Derivada Backward: ", end = "")
    print(derivada_backward(x,delta))
    print("Derivada Central: ", end = "")
    print(derivada_central(x,delta))
    print( 26 * '=')
    print("Derivadas de segunda ordem")
    print( 26 * '=')
    print("Derivada Foward: ", end = "")
    print(derivada_foward_segundaOrdem(x,delta))
    print("Derivada Backward: ", end = "")
    print(derivada_backward_segundaOrdem(x,delta))
    print("Derivada Central: ", end = "")
    print(derivada_central_segundaOrdem(x,delta))
    print(27 * '=')
    print("Derivadas de terceira ordem")
    print(27 * '=')
    print("Derivada Foward: ", end = "")
    print(derivada_foward_terceiraOrdem(x,delta))

def printar_derivada(x, delta):
    print("Derivada normal:", end="")
    print(derivada_foward(x,delta))
    print("Derivada com erro O(delta)²:", end="")
    print(derivada_foward_erroO2(x,delta))
    print("Derivada com erro O(delta)³:", end="")
    print(derivada_foward_erroO3(x, delta))

def rodar():
    while (True):
        modo = int(input("derivada com erros diferentes (1) ou derivada com diferentes filosofias (2)?"))
        if modo == 1:
            x = float(input("Digite o x para ser calculado a derivada na função x² + 3x + 5: "))
            delta = float(input("Digite o delta de x para o calculo da derivada: "))
            printar_derivada(x, delta)
            continuar = input("Deseja continuar? (s/n)").lower()
            if continuar == "s":
                continue
            else:
                break
        if modo == 2:
            x = float(input("Digite o x para ser calculado a derivada na função x² + 3x + 5: "))
            delta = float(input("Digite o delta de x para o calculo da derivada: "))
            printar(x, delta)
            continuar = input("Deseja continuar? (s/n)").lower()
            if continuar == "s":
                continue
            else:
                break
        else:
            print("Ai tu ta é doido")
            break

rodar()