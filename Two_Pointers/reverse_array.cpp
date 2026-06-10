#include<bits/stdc++.h>
using namespace std;

int reverseArray(vector<int> arr){
    int left = 0, right = arr.size() - 1;
    while(left < right){
        swap(arr[left], arr[right]);
        left++; 
        right--;
    }

    for(int i: arr){
        cout << i << " ";
    }
}

int main(){
    int n; cin >> n;
    vector<int> arr(n);

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    reverseArray(arr);
}