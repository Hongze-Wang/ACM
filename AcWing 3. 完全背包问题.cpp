// AcWing 3. 完全背包问题

#include <bits/stdc++.h>
using namespace std;

int const maxn = 1005;

int main() {
    int n, m;
    int a[maxn], b[maxn];
    int dp[maxn];
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        scanf("%d %d", &a[i], &b[i]);
    }
    for(int i=0; i<n; i++) {
        for(int j=a[i]; j<=m; j++) {
            dp[j] = max(dp[j], dp[j-a[i]]+b[i]);
        }
    }
    printf("%d", dp[m]);

    return 0;
}
