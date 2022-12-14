var1=float(input("Digite o valor do seu salário bruto:R$"))
if var1<=1693.72:
    var2=(var1-(8*var1/100))
    print("O valor liquido é:",var2)
    print("Sua contribuição foi de: ", var1*8/100)
elif var1<=2822.90:
    var2=(var1-(9*var1/100))
    print("O valor liquido é:",var2)
    print("Sua contribuição foi de: ", var1*9/100)
elif var1<=5645.80:
    var2=(var1-(11*var1/100))
    print("O valor liquido é:",var2)
    print("Sua contribuição foi de: ", var1*11/100)
else:
    print("Erro na entrada de dados")
