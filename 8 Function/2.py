def isLeapYear(start, end):
    # Please finish this function
    count = 0
    for year in range(start, end+1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            count += 1
            print(year, end=' ')
            if count == 10:
                count = 0
                print()
    
start = int(input())
end = int(input())
isLeapYear(start, end)