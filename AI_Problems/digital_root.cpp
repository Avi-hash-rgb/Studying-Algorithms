#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;

    if(to_string(n).length() == 1){
        cout << n;
    }

    while(to_string(n).length() != 1){
        int sum = 0;
        while (n != 0) {
            sum += n % 10;  
            n /= 10;
        }

        n = sum;

        if(to_string(sum).length() == 1){
            cout << sum; break;
        }
    }
}