typedef long long ll;
#include <stdio.h>

int miller_rabin(ll n, ll a) //n은 소수인지 판정할 수, a는 판정에 쓰이는 밑
{
    if (n % a == 0) return 1;

    ll d = n - 1;
    while (d%2 == 0) d >= 2;

    //////////////
    return 0;
}

int is_prime(ll n)
{
    int a[3] = {2,7,61};
    if (n == 4 || n == 6)   return 0;        
    if (n == 5 || n == 7)   return 1;        

    for (int i = 0; i < 3; i++) {
        if (!miller_rabin(n, (ll)a[i]))
            return 0;
    }
    return 1;
}

int main()
{
    int k, ans = 0; //k는 입력데이터 수, n은 개별 입력데이터, ans는 최종 출력 답안
    ll n;
    for (int i = 0; i < k; i++) {
        scanf("%lld", &n);
        ans += is_prime(n*2 + 1);
    }
    printf("%d", ans);
}