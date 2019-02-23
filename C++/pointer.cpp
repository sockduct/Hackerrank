#include <cstdlib>
#include <stdio.h>

void update(int *a, int *b) {
    const int orig_a = *a, orig_b = *b;

    *a = orig_a + orig_b;
    *b = abs(orig_a - orig_b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

