#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    static long total_points = 1<<22;
    int points_in_circle = 0;
    int tid;
    unsigned int seed;
#pragma omp parallel for private(tid, seed) reduction(+:points_in_circle)
    for (int i = 0; i < total_points; i++) {
        tid = omp_get_thread_num();
        //printf("%d\n", tid);
        seed = (unsigned int)rand() ^ (12345 * tid);
        double x = (double) rand_r(&seed) / RAND_MAX;
 	double y = (double) rand_r(&seed) / RAND_MAX;
        //printf("x=%f\n", x);
        //printf("y=%f\n\n", y);
 	if (x * x + y * y <= 1)
 		points_in_circle++;
    }
 printf("Estimate of pi = %f\n", 4.0 * points_in_circle / total_points);
 return 0;
}
