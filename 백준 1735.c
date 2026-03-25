#include <stdio.h>

int gcd(int a, int b)
{
    if (b > a) {
        int temp = a;
        a = b;
        b = temp;
    }

    int r;
    while (b) {
        r = a % b;
        a = b;
        b = r;
    }

    return a;
}

int main()
{
    int a,b,c,d, over, below; // a/b + c/d = over/below
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);

    over = a*d + b*c;
    below = b*d;

    int factor = gcd(over, below);
    over /= factor;
    below /= factor;

    printf("%d %d\n", over, below);
}