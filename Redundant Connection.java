class Solution {
    int [] vertices;
    public int[] findRedundantConnection(int[][] edges) {
        vertices = new int [edges.length + 1];

        for(int i = 1; i < vertices.length; i++)
            vertices[i] = i;
        for(int i = 0; i < edges.length; i++){
            if(!union(edges[i][0], edges[i][1]))
                return edges[i];
        }
        return null;
    }
    public int find(int vertex){
        int temp = vertex;
        while(vertex != vertices[vertex]){
            vertex = vertices[vertex];
        }
        //path compression or collapsing find the time complexity becomes amortized constant time
        while(temp != vertex){
            int parent = vertices[temp];
            vertices[temp] = vertex;
            temp = parent;
        }
        return vertex;
    }
    public boolean union(int v1, int v2){
        int root1 = find(v1);
        int root2 = find(v2);
        if(root1 == root2)
            return false;
        vertices[root1] = root2;
        return true;
    }
}
