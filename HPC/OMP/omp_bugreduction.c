#include <omp.h>
#include <stdio.h>
#include <stdlib.h>


float dotprod(float * a, float * b, size_t N, float sum)
{
    int i, tid;
    #pragma omp parallel shared(sum)
    {
    float cur_sum = 0.0;
    //int nthreads;
    //nthreads = omp_get_num_threads();
    //printf("Number of threads = %d\n", nthreads);

    tid = omp_get_thread_num();

#pragma omp for
    for (i = 0; i < N; ++i)
    {
        cur_sum += a[i] * b[i];
        printf("%f, %f\n", a[i], b[i]);
        printf("tid = %d i = %d\n", tid, i);
    }
    #pragma omp critical
    {
        sum += cur_sum;
    }
    printf("sum is: %f\n", sum);
    }

    return sum;
}

int main (int argc, char *argv[])
{
    const size_t N = 100;
    int i;
    float sum;
    float a[N], b[N];


    for (i = 0; i < N; ++i)
    {
        a[i] = b[i] = (double)i;
    }

    sum = 0.0;
    //int nthreads;

    //#pragma omp parallel for reduction(+: sum)
    //for (i = 0; i < N; i++)
    //    sum += a[i] * b[i];
    //printf("a*b = %f\n", sum);
    sum = dotprod(a, b, N, sum);

    printf("Sum = %f\n",sum);

    return 0;
}
