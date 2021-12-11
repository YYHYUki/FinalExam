n=int(input())
coordinate=[]

for _ in range(n):
    (x,y)= list(map(int,input().split()))
    coordinate.append((x,y))

sorted_coordinate=sorted(coordinate)

for i in sorted_coordinate:
    print(i[0], i[1])