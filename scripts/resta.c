#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[]) {
  if (argc == 3){
    double a= atof(argv[1])-atof(argv[2]);
    printf("%f\n",a);
  }
}
