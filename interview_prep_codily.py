

def solution(A):
    if len(A) == 1:
        return 'unknown edge case'
    B = [(i, num) for i, num in enumerate(A)]
    B.sort(key=lambda x: x[1])
    max_dist = 0

    p=0
    q=1
    while q < len(B):
        cur_dist = abs(B[p][0] - B[q][0])
        max_dist = max(cur_dist, max_dist)
        if q+1 < len(B) and B[q+1][1] == B[q][1]:
            pass
        else:
            p=q
        q+=1

    return max_dist




A = [1,4,7,3,3,5]
B = [2,5]
C = [1]
D = [1,2,3,4,5,6]


print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))