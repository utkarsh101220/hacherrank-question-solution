    n=int(input())
    record=[]
    for _ in range(n):
        name = input()
        score = float(input())
        record.append([name,score])
    marks=[]
    for i in range(n):
        marks.append(record[i][1])
    marks = list(set(marks))
    marks.sort()
    second_lowest = marks[1]
    name_list = []
    for i in range(n):
        if(record[i][1] == second_lowest):
            name_list.append(record[i][0])
    name_list.sort()
    for name in name_list:
        print (name)
