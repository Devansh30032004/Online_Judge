#include <stdio.h>

int main() {
    int weight;

    // Read the weight from input
    scanf("%d", &weight);

    // Check if the weight is even
    if (weight % 2 == 0) {
        // Check if the weight is not 2
        if (weight != 2) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    } else {
        printf("No\n");
    }

    return 0;
}