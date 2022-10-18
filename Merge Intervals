class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int []> result = new ArrayList<>();
        int prevStart = Integer.MIN_VALUE, prevEnd = Integer.MIN_VALUE;
        for(int [] interval : intervals){
            int start = interval[0], end = interval[1];
            if(start <= prevEnd){
                int [] temp = result.get(result.size() - 1);//merging the last elt in the list to the current elt
                if(temp[0] > start){
                    temp[0] = start;
                    prevStart = start;
                }
                if(temp[1] < end){
                    temp[1] = end;
                    prevEnd = end;
                }
            }
            else{
                result.add(interval);//only add to the list onece all have been merged and the new is unique
                prevStart = start;
                prevEnd = end;
            }
        }
        return result.toArray(new int[result.size()][2]);
    }
}
