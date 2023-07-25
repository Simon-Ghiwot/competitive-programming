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
        siz[x] += siz[y];
        f[y] = x;
        return true;
    }
    int size(int x) { return siz[leader(x)]; }
};
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        DSU dsu(26);
        vector<string> not_equal;
        for(auto cur : equations){
            if(cur[1] == '!')
                not_equal.push_back(cur);
            else{
                int v = cur[0] - 'a';
                int u = cur.back() - 'a';
                dsu.merge(u, v);
            }
        }
        for(auto cur : not_equal){
            int v = cur[0] - 'a';
            int u = cur.back() - 'a';
            if(dsu.same(u, v))
                return false;
        }
        return true;
    }
};
