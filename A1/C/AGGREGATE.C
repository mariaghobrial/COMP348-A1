//
//  AGGREGATE.c
//  Q3Q4a1_comp348
//
//  Created by Maria Ghobrial on 2022-05-13.


#include "AGGREGATE.H"


//  AGGREGATE.c
//  a1.comp348

//  Created by Maria Ghobrial on 2022-05-11.

#include <stdio.h>
#include <stdlib.h>


//fct that returns min element in an array
float min(float arr[], int size){
    if ( arr== NULL || size <= 0){
        printf("FATAL ERROR at fucntion min at LINE %d\n", __LINE__);
        exit(1);
        // printf("program terminated", _ab);
        
    }
    
    float temp=arr[0];
    for (int i=0; i<size;i++){
        if(temp>arr[i]) {
            temp=arr[i];
        }
        
    }
    // printf("The min is: %f\n",temp);
    return temp;
    
}
//fct that returns max element in an array
float max(float arr[], int size){
    if (arr == 0 || size <=0){
        printf("FATAL ERROR at function max at LINE %d\n", __LINE__);
        // printf("program terminated", _ab);
        
    }
    
    float temp=arr[0];
    
    for (int i=0; i<size;i++){
        if(temp<arr[i]) {
            temp=arr[i];
        }
        
    }
    // printf("The max is: %f\n",temp);
    return temp;
}
//fct that returns the sum of the elements in an array
float sum(float arr[], int size) {
    if (arr == 0 || size <=0){
        printf("FATAL ERROR at function sum at LINE %d\n", __LINE__);
        // printf("program terminated", _ab);
        
        
    }
    
    int sum = 0;
    
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    //  printf("The sum is: %f\n",sum);
    return sum;
}
//fct that returns the sum of the elements in an array
float avg(float arr[], int size){
    if (arr == NULL || size <=0){
        printf("FATAL ERROR at function avg at LINE %d\n", __LINE__);
        // printf("program terminated", _ab);
    }
    
    int sum = 0;
    for (int i=0; i<size; i++)
        sum += arr[i];
    
    
    //  printf("The average is: %f\n",sum/size);
    return sum/size;
}



//fct that returns the avg of max and min of an array
float pseudo_avg(float arr[], int size){
    if (arr == NULL || size <= 0){
        printf("FATAL ERROR at function pseudo_avg at LINE %d\n", __LINE__);
        // printf("program terminated", _ab);
    }
    
    
    float avg= max(arr, size)+ min(arr,size);
    //  printf("The pseudo avg is: %f\n",avg/2);
    return avg/2;
    
}
