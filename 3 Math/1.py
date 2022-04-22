import math
name = input()
score = eval(input())
final = round(math.sqrt(score) * 10)
print(name, "'s Final grade: ", final, sep='')