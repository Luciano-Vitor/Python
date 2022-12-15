menor_idade=[]
faixa_ideal=[]
idade_superior=[]
i=0
while i<=10:
    var=(input("Informe seu nome:"))
    var1=int(input("Informe a sua idade por favor:"))
    if var1<18:
        menor_idade.append(var)
        
    elif var1<=45:
        faixa_ideal.append(var)
        
    elif var1>60:
        idade_superior.append(var)
        
    else:
        print("Idade inválida")
    i=i+1

    print("Pessoas jovens:",menor_idade)
    print("Pessoas adultas e trabalhadoras:",faixa_ideal)
    print("Pessoas idosas:",idade_superior)