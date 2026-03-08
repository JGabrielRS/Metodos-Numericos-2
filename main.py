import func_printar

def rodar():
    while (True):
        x = float(input("Digite o x para ser calculado a derivada na função x² + 3x + 5: "))
        delta = float(input("Digite o delta de x para o calculo da derivada: "))
        print("Escolha um modo:")
        modo = int(input("Todas as derivadas (1) Apenas as derivadas foward (2) Apenas as derivadas backward (3) Apenas as derivadas centrais (4) "))
        match modo:
            case 1:
                func_printar.printar(x, delta)
                continuar = input("Deseja continuar? (s/n) ").lower()
                if continuar == "s":
                    continue
                else:
                    break
            case 2:
                func_printar.printar_foward(x, delta)
                continuar = input("Deseja continuar? (s/n) ").lower()
                if continuar == "s":
                    continue
                else:
                    break
            case 3:
                func_printar.printar_backward(x, delta)
                continuar = input("Deseja continuar? (s/n) ").lower()
                if continuar == "s":
                    continue
                else:
                    break
            case 4:
                func_printar.printar_central(x, delta)
                continuar = input("Deseja continuar? (s/n) ").lower()
                if continuar == "s":
                    continue
                else:
                    break
            case _:
                print("Ai tu ta é doido")
                break

rodar()