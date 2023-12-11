import re

def till_siffra(siffra: str) -> str:
    match(siffra):
        case "on"   | "1": return "1"
        case "tw"   | "2": return "2"
        case "thre" | "3": return "3"
        case "four" | "4": return "4"
        case "fiv"  | "5": return "5"
        case "six"  | "6": return "6"
        case "seve" | "7": return "7"
        case "eigh" | "8": return "8"
        case "nin"  | "9": return "9"
        case _           : raise Exception("ingen siffra: " + siffra)

def hitta_tal(rad: str) -> int:
    siffror = re.findall(r"on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e)|[1-9]", rad)
    första_siffran = till_siffra(siffror[0])
    sista_siffran  = till_siffra(siffror[-1])
    tal = första_siffran + sista_siffran
    print(tal + ": " + rad[:-1])
    return int(tal)

input = open("./1/input.txt", "r")
alla_tal = [hitta_tal(x) for x in input]
input.close()

res = sum(alla_tal)

print(res)
