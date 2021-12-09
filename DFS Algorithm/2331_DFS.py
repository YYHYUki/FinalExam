def number_square(number, square):    # square P each number
    return sum([int(i) ** square for i in str(number)])
 
def dfs(A, P, visited, count):    # DFS implementation
    if visited[A]:    # if occur repeated number
        return visited[A] - 1
    visited[A] = count
    temp = number_square(A, P)
    count += 1
    return dfs(temp, P, visited, count)
 
A, P = map(int, input().split())
visited = [0] * 250000    # maximum case(236196 is approximately 250000)
count = 1
print(dfs(A, P, visited, count))