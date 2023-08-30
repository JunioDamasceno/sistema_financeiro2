dic = {"Nome": 'Junio', "Extrato":[]}
teste = ["maça", "banana", "mamão"]
dic["Extrato"] = teste
print(dic)
dic["Extrato"].insert(len(dic["Extrato"]), "Limão")
print(dic)

a = dic.get("Extrato")
a.append("pera")
print("\nO valor de 'a' é: {}".format(a), type(a))

dic.update({"Extrato": a})

print("\n", dic)
b = ['Cao', 'gato', 'macaco']
c = {"Nome": 'Bruno', "Extrato": ['ave', 'porco', 'grilo', 'cobra', 'baleia']}
dic.append(c)
dic2 = {"Nome": 'Wesley Safadão', "Extrato": b}
dic.update(dic2)
print("\nAtualizado", dic)