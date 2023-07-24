struct DSU {
    std::vector<int> f, siz;
    DSU(int n) : f(n), siz(n, 1) { std::iota(f.begin(), f.end(), 0); }
    int leader(int x) {
        while (x != f[x]) x = f[x] = f[f[x]];
        return x;
    }
    bool same(int x, int y) { return leader(x) == leader(y); }
    bool merge(int x, int y) {
        x = leader(x);
        y = leader(y);
        if (x == y) return false;
        if(x < y)   f[y] = x;
        else f[x] = y;
        return true;
    }
    int size(int x) { return siz[leader(x)]; }
};
class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        DSU dsu(26);
        for(int i = 0; i < s1.length(); i++){
            int x = s1[i] - 'a', y = s2[i] - 'a';
            dsu.merge(x, y);
        }
        string ans = "";
        for(int i = 0; i < baseStr.length(); i++){
            int leader = dsu.leader(baseStr[i] - 'a');
            ans += (char) (leader + 'a');
        }
        return ans;
    }
};
