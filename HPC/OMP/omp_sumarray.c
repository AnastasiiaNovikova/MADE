#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv)
{
    const size_t N = 10;

    int a[N];
    int tid;

#pragma omp parallel for
    for (int i = 0; i < N; ++i)
    {
        tid = omp_get_thread_num();
        printf("tid is: %d, i is: %d\n", tid, i);
        a[i] = i;
    }

    int sum = 0;

    for (int i=0; i<N; i++)
    {
    printf("a[%d]=%d\n", i, a[i]);
    }

#pragma omp parallel for reduction(+: sum)
    for (int i = 0; i < N; ++i)
    {
        sum += a[i];
    }

    printf("sum = %d\n", sum);

    return 0;
}
