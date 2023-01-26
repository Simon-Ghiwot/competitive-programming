class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            s = i
            for j in range(i+1,len(arr)):
              if arr[j] < arr[i]:
                  s = j
            arr[s],arr[i]= arr[i],arr[s]
        return arr
