#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int> &arr, int target) {
    sort(arr.begin(), arr.end());
    int left = 0, right = arr.size() - 1;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            return {arr[left], arr[right]};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {};
}

int main() {
    int n, target;
    if (!(cin >> n >> target)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> result = twoSum(arr, target);

    if (!result.empty()) {
        cout << result[0] << " " << result[1] << endl;
    } else {
        cout << "No Pair found!" << endl;
    }

    return 0;
}