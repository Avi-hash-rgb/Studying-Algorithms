#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

void dfsRecursive(int node, const vector<vector<int>>& adj, vector<bool>& visited){
    visited[node] = true;
    cout << node << " ";
    for(int neighbour: adj[node]){
        if(!visited[neighbour]){
            dfsRecursive(neighbour, adj, visited);
        }
    }

    // Time Complexity: O(V + E) where,
    // Where V is the number of nodes and E is the number of edges in the graph.
}

void dfsIterative(int snode, const vector<vector<int>>& adj, int v){
    vector<bool> visited(v, false);
    stack<int> st;
    st.push(snode);
    
    while(!st.empty()){
        int node = st.top();
        st.pop();
        
        if(!visited[node]){
            visited[node] = true;
            cout << node << ' ';
        }

        for(auto it = adj[node].rbegin(); it != adj[node].rend(); ++it){
            int neighbour = *it;
            if(!visited[neighbour]) st.push(neighbour);
        }
    }

    // Same as the recursive DFS: O(V + E)
}

int32_t main() {
    int v; cin >> v;
    vector<vector<int>> adj(v);
    adj[0].push_back(1);
    adj[0].push_back(2);
    adj[1].push_back(0);
    adj[1].push_back(3);
    adj[1].push_back(4);
    adj[2].push_back(0);
    adj[3].push_back(1);
    adj[4].push_back(1);
    
    vector<bool> visited(v, false);
    cout << "DFS Recursive Traversal starting from vertex 0: ";
    dfsRecursive(0, adj, visited); 
    cout << endl;

    cout << "DFS Iterative Traversal starting from vertex 0: ";
    dfsIterative(0, adj, v); 
    cout << endl;
}
