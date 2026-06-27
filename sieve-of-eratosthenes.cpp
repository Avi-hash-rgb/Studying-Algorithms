#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL);
#define endl "\n

// This code basically prints the sieve of eratosthenes in a certain manner.

int main() {
    fastio;
    int n; cin >> n;
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i] && (long long)i * i <= n) {
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;
        }
    }

    for(int i = 2; i <= n; i++){
        if(is_prime[i]) cout << i << " ";
    }
    cout << endl;
    // Time complexity: O(n log log n)
    // Space complexity: O(n)
}
