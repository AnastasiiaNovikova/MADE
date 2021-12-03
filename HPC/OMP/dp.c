#include <stdio.h>

int main(int argc, char *argv[]) {
 size_t N=500;
 float sum, a[N], b[N];
 int i;
 for (i = 0; i < N; i++) {
 a[i] = (double)i;
 b[i] = (double)i;
 }
 sum = 0;
#pragma omp parallel for reduction(+:sum)
 for (i = 0; i < N; i++)
 sum += a[i] * b[i];
 printf("a*b = %f\n", sum);
}
