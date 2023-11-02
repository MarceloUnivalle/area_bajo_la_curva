#include <stdio.h>
#include <math.h>

#define MAX_RECT 9000000
#define LIM_BAJ 0
#define LIM_ALT 2

double funcion(double x) {
    double f1 = sin(x);
    double f2 = cos(x);
    return f1*f1*f1 + f2*f2*f2;
}

double area() {
    double base,hbase;
    int i;
    double area;

    base = (double)(LIM_ALT - LIM_BAJ)/(double)MAX_RECT;
    hbase = base/2.0;

    area = 0.0;

    #pragma omp parallel for reduction(+:area) num_threads(2)
    for (i = 0; i < MAX_RECT; i++) {
        area += base*funcion((double)i/(double)MAX_RECT + hbase);
    }
    // printf("Area es %lf\n",area);

    return area;
}