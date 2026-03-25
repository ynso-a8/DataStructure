typedef long long ll;
#include <stdio.h>

int jegob(ll x, ll y, int m)
{
    if (y == 0) return 1;

    ll ans = 1, temp = x %= m;
        
    while (y > 0) {
        if (y & 1)
            ans = (ll)((__int128)ans * temp) % m;
        temp = (temp * temp) % m;
        y >>= 1;  
    }
    return (int)ans;
}

int main()
{
    int num;
    num = jegob(11, 5, 100);
    printf("%d\n", num);
    return 0;
}
