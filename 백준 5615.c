typedef long long ll;
#include <stdio.h>

ll jegob(ll x, ll y, ll m) // x^y % m 연산
{
    if (y == 0) return 1;

    ll ans = 1, temp = x %= m;
        
    while (y > 0) {
        if (y & 1)
            ans = ((__int128)ans * temp) % m;
        temp = (temp * temp) % m;
        y >>= 1;  
    }
    return ans;
}

int miller_rabin(ll n, ll a, ll d, ll s) //n은 소수인지 판정할 수, a는 판정에 쓰이는 밑, n - 1 = d * (2^s), d는 홀수
{
    if (n % a == 0) return 0;

    ll A = jegob(a, d, n); // A = a ^ (d * 2^r), 0<= r < s
    if ( A == 1 || A == n-1 ) return 1;

    for (int r = 1; r < s; r++) {
        A = jegob(A, 2, n);
        if (A == n - 1)
            return 1;
    }

    return 0;
}

int is_prime(ll n)
{
    ll a[3] = {2,7,61};    
    ll s = 0, d = n - 1;

    if (n == 2 || n == 7 || n == 61)    return 1;

    while (d%2 == 0) {
        d >>= 1;
        s++;
    }

    for (int i = 0; i < 3; i++) {
        if (!miller_rabin(n, a[i], d, s))
            return 0;
    }
    return 1;
}

int main()
{
    int k, ans = 0; //k는 입력데이터 수, n은 개별 입력데이터, ans는 최종 출력 답안
    ll n;
    scanf("%d", &k);

    for (int i = 0; i < k; i++) {
        scanf("%lld", &n);
        ans += is_prime(n*2 + 1);
    }
    printf("%d\n", ans);
}