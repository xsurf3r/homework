recepte = {"cukurs":0.6, "kanelis":0.008,"aboli":2.0, "udeni":0.2 }
cena = {"cukurs":0.75, "kanelis":0.3, "aboli":0.0, "udeni":0.0 }

cukurs = 0.75
kanelis = 0.3
aboli =0.0
udeni =0.0

num = recepte["cukurs"]
num2 = recepte['kanelis']
sum = cukurs+kanelis
while (num != 0):
    sum = num + num2
    num = num // 10
print("recepte: ", sum)