class Result {

    /*
     * Complete the 'gradingStudents' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY grades as parameter.
     */

    public static List<Integer> gradingStudents(List<Integer> grades) {
    // Write your code here
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < grades.size(); i++){
            if(grades.get(i) < 38 || grades.get(i) % 5 < 3)  
                result.add(grades.get(i));
            else 
                result.add((grades.get(i) / 5) * 5 + 5);
        }
        
        return result;
    }

}
