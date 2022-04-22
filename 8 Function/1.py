import math

def calculate(frac1, frac2):
    # Please finish this function
    frac3 = {}
    d = frac1["denominator"] * frac2["denominator"]
    n = frac1["numerator"] * frac2["denominator"] + frac2["numerator" ] * frac1["denominator"]
    Gcd = math.gcd(n, d)
    frac3["numerator"] = n // Gcd
    frac3["denominator"] = d // Gcd
    return frac3

numerator1 = int(input())
denominator1 = int(input())
numerator2 = int(input())
denominator2 = int(input())

fraction1 = {"numerator": numerator1, "denominator": denominator1}
fraction2 = {"numerator": numerator2, "denominator": denominator2}
result = calculate(fraction1, fraction2)
if result["denominator"] == 1:
    print(result["numerator"])
else:
    print(result["numerator"], '/', result["denominator"], sep='')