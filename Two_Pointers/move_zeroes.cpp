#include<bits/stdc++.h>
using namespace std;

int moveZeroes(vector<int>& arr){
    int slow = 0;
    for(int fast = 0; fast < arr.size(); fast++){
        if(arr[fast] != 0){
            swap(arr[slow], arr[fast]);
            slow++;
        }
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
    moveZeroes(arr);
}