class Solution {
    private List<List<String>> result;
    private Set<Integer> col;
    private Set<Integer> posDiagonal;
    private Set<Integer> negDiagonal;
    public List<List<String>> solveNQueens(int n) {
        result = new ArrayList<>();
        col = new HashSet<>();
        posDiagonal = new HashSet<>();
        negDiagonal = new HashSet<>();

        backtracking(0, new ArrayList<>(), n);
        return result;
    }
    private void backtracking(int row, List<String> current, int size){
        if(size == current.size())
            result.add(new ArrayList<>(current));
        
        for(int c = 0; c < size; c++){
            if(col.contains(c) || posDiagonal.contains(row + c) || negDiagonal.contains(c - row + size - 1))
                continue;
            char [] queen = new char[size];
            Arrays.fill(queen, '.');
            queen[c] = 'Q';
            current.add(new String(queen));
            col.add(c);
            posDiagonal.add(row + c);
            negDiagonal.add(c - row + size - 1);
            backtracking(row + 1, current, size);
            col.remove(c);
            posDiagonal.remove(row + c);
            negDiagonal.remove(c - row + size - 1);
            current.remove(current.size() - 1);
        }
    }
}
