/*
 * array A[] of length N
 * return Max(P-Q)
 * which (P, Q) such that A[P]<=A[Q]
 */
int solution(int A[], int N) {
    int *B = (int *)malloc(N*sizeof(int));
    int i;
    int cnt = 0;
    int result = -1;
    for(i = 0; i < N; i++)
    {
        if(cnt == 0 || A[i] < A[B[cnt-1]])
        {
            B[cnt] = i;
            cnt++;
        }
    }
    for(i = N-1; i >= 0 && cnt > 0; i--)
    {
        while(cnt > 0 && A[i] >= A[B[cnt-1]])
        {
            if(i - B[cnt-1] > result){
                result = i-B[cnt-1];
            }
            cnt--;
        }
    }
    return result;
}

