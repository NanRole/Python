s = input()
index = s.find(':')
print(s[:index], s[index+2:].replace(',', ''), sep='\n')