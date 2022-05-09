float min(float arr[], int size);
float max(float arr[], int size);
float sum(float arr[], int size);
float avg(float arr[], int size);
float pseudo_avg(float arr[], int size);
float (*aggregates[5])(float arr[], int size) = {min, max, sum, avg, pseudo_avg};
