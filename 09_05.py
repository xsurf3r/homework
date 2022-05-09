# Dota programma, kuras uzdevums ir aprēķināt riņķa laukumu
# Testēšana: 3 ----> 28.26
#r = float(input("Ieraksti riņķa rādiusu: "))
#pi = 3.14
#laukums = pi * r**2
#print(f"Riņķa laukums ir {laukums}")


# Dota programma, kuras uzdevums ir izvadīt lietotāja ievadīto vārdu 
# unuzvārdu apgrieztā secībā (starp vārdu un uzvārdu ir jābūt atstarpei)
# Testēšana: Anna Bērziņa -----> Bērziņa Anna
#vards = input("Ievadi vārdu: ")
#uzvards = input("Ievadi uzvārdu: ")
#print (uzvards,vards)


#Dota programma, kuras uzdevums ir - lietotāja ievadītos skaitļus (kasatdalīti ar komatiem), izdrukāt kā sarakstu(list) un kortežu(tuples)
#Testēšana: 1,2,3,4,5,6 -----> Saraksts: ['1','2','3','4','5','6']
# -----> Kortežs: ('1','2','3','4','5','6')
#vertibas = input("Ievadi skaitļus, atdalot tos ar komatiem: ")
#saraksts = vertibas.split(",")
#kortezs = tuple(saraksts)
#print('Saraksts : ',saraksts)
#print('Kortežs : ',kortezs)


#Dota programma, kuras uzdevums ir izvadīt pirmo un pēdējo krāsu no dotā saraksta
#Testēšana: ------> Sarkans, melns
#krasu_saraksts = ["Sarkans","Zaļš","Balts","Melns"]
# print( "%s, %s"%(krasu_saraksts[0],krasu_saraksts[-1]))


#Dota programma, kuras uzdevums ir veikt sekojošo matemātisko darbību ar
#Testēšana: 5 ----> 615
# a = int(input("Ievadi veselu skaitli: "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)


#Dota programma, kuras uzdevums ir izvadīt lietotāja ievadītā mēneša kalendāru
#Testēšana: 2015 ---------> May 2015
# 4 ---------> Mo Tu We Th Fr Sa Su
# 1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
# import calendar
# y = int(input("Ievadi gadu : "))
# m = int(input("Ievadi mēnesi : "))
# print(calendar.month(y, m))


#Dota programma, kuras uzdevums ir salīdzināt doto ciparu (n) ar 17, ja n irlielāks par 17, tad nepieciešams atgriezt šo skaitļu starpību dubultā, bet, jan ir mazāks vai vienāds ar 17, nepieciešams atgriezt šo skaitļu starpību
#Testēšana: starpiba(22) -----> 10
# starpiba(14) -----> 3
# def starpiba(n):
#     if n <= 17:
#         return (17 - n)
#     else:
#         return (n - 17) * 2
# print(starpiba(22))
# print(starpiba(14))