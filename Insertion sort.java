class Result {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
        for(int i = 1; i < arr.size(); i++){
            int j = i;
            int value = arr.get(i);
            while(j != 0 && arr.get(j - 1) > value){
                arr.set(j, arr.get(j - 1));
                for(int k = 0; k < arr.size(); k++)
                    System.out.print(arr.get(k) + " ");
                System.out.print("\n");
                j--;
            }
            arr.set(j, value);
        }
        for(int k = 0; k < arr.size(); k++)
            System.out.print(arr.get(k) + " ");
    }

}
