print("Contrato de Vendas Fiat")
nome = "Luciano" 
sobrenome = "Vitor Pereira Bernardes dos Santos"
cpf = "12345678901"
var1 = float(input("Digite o valor do Uno 99:"))
var2 = float(input("Digite o valor da venda da moto X1:"))
var3 = (var1+var2)

print(cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:11]+" / "+nome+" "+sobrenome)
print("A quantidade de digitos do cpf é:",len(cpf))

print("A Ultima letra do nome é:",nome[-1])

 
print("Eu",nome,sobrenome,"do documento",cpf,"declaro que recebi no mês de novembro de 2022 a quantia de ",var1,"na venda do Fiat Uno 99 e a quantia de",var2,"na venda da moto X1, somando a quantia de",var3)

