#include <iostream>
#include "AGGREGATE.H"

//fct that returns min element in an array
float min(float arr[], int size){

    if (arr== 0){
        std::cout << "Error! array is null" << std::endl;

    }else{
        float temp=arr[0];

        for (int i=0; i<size;i++){
            if(temp>arr[i]) {
            temp=arr[i];
        }

        }
        return temp;

        }
   
}
//fct that returns max element in an array
float max(float arr[], int size){
    if (arr=0){
        std::cout << "Error! array is null" << std::endl;

    }
    float temp=arr[0];

    for (int i=0; i<size;i++){
        if(temp<arr[i]) {
         temp=arr[i];
      }

    }
    return temp;
}
//fct that returns the sum of the elements in an array
float sum(float arr[], int size) {
     if (arr=0){
        std::cout << "Error! array is null" << std::endl;

    }
     int sum = 0; 

    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
     
    return sum; 
}
//fct that returns the sum of the elements in an array
float avg(float arr[], int size){
    if (arr=0){
        std::cout << "Error! array is null" << std::endl;

    }
    int sum = 0;
    for (int i=0; i<size; i++)
       sum += arr[i];
 
    return sum/size;
}

   

//fct that returns the avg of max and min of an array
float pseudo_avg(float arr[], int size){
    if (arr=0){
        std::cout << "Error! array is null" << std::endl;
    }
    
    float avg= max(arr, size)+ min(arr,size);
    return avg/2;
    
}
