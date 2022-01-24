#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

static void swap(int *xp, int *yp){
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubble_sort(int arr[], int n){
   int i, j;
   bool swapped;
   for (i = 0; i < n-1; i++)
   {
     swapped = false;
     for (j = 0; j < n-i-1; j++)
     {
        if (arr[j] > arr[j+1])
        {
           swap(&arr[j], &arr[j+1]);
           swapped = true;
        }
     }

     // IF no two elements were swapped by inner loop, then break
     if (swapped == false)
        break;
   }
}


int main(){
    int arr_sz = 10000;
    int arr[arr_sz];
    for (int i = 0; i < arr_sz; i++){
        arr[i] = rand();
    }
    bubble_sort(arr, arr_sz);

    /*
    for(int j = 0; j < arr_sz; j++) {
            printf("%d ", arr[j]);
    }
     */

    return 0;
}

