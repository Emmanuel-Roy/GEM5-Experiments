#include <cstdio>

#define ARRAY_SIZE 1024*1024

int main() {
    static float A[ARRAY_SIZE], B[ARRAY_SIZE], C[ARRAY_SIZE];
    for (int i = 0; i < ARRAY_SIZE; i++) {
        C[i] = A[i] + B[i];
    }
    // Make sure loop isn't optimized out. We want to test as much data as possible!
    printf("C[0] = %f\n", C[0]);
    return 0;
}