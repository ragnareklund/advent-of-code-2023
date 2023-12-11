import re

def hitta_tal(rad: str) -> int:
    första_siffran = re.findall(r"\d", rad)[0]
    sista_siffran  = re.findall(r"\d", rad)[-1]
    tal = första_siffran + sista_siffran
    return int(tal)

input = open("./1/input.txt", "r")
alla_tal = [hitta_tal(x) for x in input]
input.close()

res = sum(alla_tal)

print(res)
