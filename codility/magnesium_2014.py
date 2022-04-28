def solution(N, A, B, C):
    '''
    N intersections, level(C[i]) of road between two intersections(A[i], B[i]).
    return the longest path which has ascending level
    '''
    M = len(C)
    D = sorted([(C[i], i) for i in range(M)])

    E = [[0,0] for i in range(M)]
    F = [0] * N

    i = 0
    while i < M:
        level = D[i][0]
        j = i
        while i < M and D[i][0] == level:
            a = A[D[i][1]]
            b = B[D[i][1]]
            E[i][0] = F[b] + 1
            E[i][1] = F[a] + 1
            i+=1;
        for k in range(j, i):
            a = A[D[k][1]]
            b = B[D[k][1]]
            if E[k][0] > F[a]:
                F[a] = E[k][0]
            if E[k][1] > F[b]:
                F[b] = E[k][1]
    return max(F)

# print solution(2, [0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0],[4,4,5,6,7,8,9,10,11])

