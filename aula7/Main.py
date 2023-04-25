from Conta import Conta
c1 = Conta()
# print(c1.getSaldo())
# c1.setSaldo(20)
# print("Novo saldo: "+str(c1.getSaldo()))
print("saldo " +str(c1.Saldo))
c1.saldo = 30 
print("saldo " +str(c1.Saldo))
c1.depositar(100)
print("saldo apos deposito: " +str(c1.Saldo))

c1.sacar(200)
print("saldo apos saque :" +str(c1.Saldo))


# = -
# - = __s