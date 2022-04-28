def solution(X, Y, K, A, B):
    N = len(A) + 1
    A.append(X)
    A.append(0)
    B.append(Y)
    B.append(0)
    L = [A[i]-A[i-1] for i in range(N)]
    H = [B[i]-B[i-1] for i in range(N)]
    L.sort(reverse=True)
    H.sort(reverse=True)
    size = lambda x, y: L[x]*H[y]
    high = size(0, 0)
    low = size(N-1, N-1)
    val = high + 1
    while low <= high:
        mid = (low+high)>>1
        row = 0
        col = N-1
        cnt_big = 0
        cnt_big_eq = 0
        flag = False
        # get the count of number bigger than mid
        while row < N and col >= 0:
            area = size(row, col)
            if mid < area:
                cnt_big += col+1
                row += 1
            elif mid == area:
                flag = True
                col -= 1
            else:
                col -= 1
        # get the count of numbers bigger or equal mid
        if flag:
            row = 0
            col = N-1
            while row < N and col >= 0:
                area = size(row, col)
                if mid <= area:
                    cnt_big_eq += col+1
                    row += 1
                else:
                    col -= 1
        if cnt_big < K:
            if K <= cnt_big_eq:
                return mid
            high = mid-1
        elif cnt_big == K:
            break
        else:
            low = mid+1
    # Find the smallest value which bigger than mid
    row = 0
    col = N-1
    while row < N and col >= 0:
        area = size(row, col)
        if area > mid:
            if val > area:
                val = area
            row += 1
        else:
            col -= 1
    return val

