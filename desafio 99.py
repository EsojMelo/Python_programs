def maior(*numeros):
    print("=-" * 20)
    print("Analisando valores passados...")
    maximo = max(numeros)
    posicao = 0
    quantu = len(numeros)
    for quantu in range(0, len(numeros)):
        print(f"{numeros[posicao]}", end=' ')
        posicao += 1
    if sum(numeros) == 0:
        print("Não foram informados valores")
    else:
        print(f"foram informados {quantu + 1} números")
    print(f"O maior valor informado foi {maximo}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(3, 2)
maior(6)
maior(0)
