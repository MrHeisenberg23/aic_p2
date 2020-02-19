#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TIPO_PRINT_ERROR a

// data types to change types
typedef int data;


void type_data(char**);


int main (int argc, char** argv)
{
    time_t t;
    data **ptr1, **ptr2, **ptr3;
    int N, col1, row2, col2;
    srand ((unsigned) time (&t));
    int i, j, k;
    printf ("\nEnter the value of N : ");
    //scanf ("%d", &N);

    // number of elements
    N = atoi(argv[1]);

    char ** type;
    type_data(type);

    ptr1 = (data **) malloc (sizeof (data *) * N);
    ptr2 = (data **) malloc (sizeof (data *) * N);
    ptr3 = (data **) malloc (sizeof (data *) * N);

    for (i = 0; i < N; i++) {
        ptr1[i] = (data *) malloc (sizeof (data) * N);
	       ptr2[i] = (data *) malloc (sizeof (data) * N);
	        ptr3[i] = (data *) malloc (sizeof (data) * N);
    }

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            ptr1[i][j] = (data)rand()/(data)(RAND_MAX);
	           ptr2[i][j] = (data)rand()/(data)(RAND_MAX);
        }
    }

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            ptr3[i][j] = 0;
            for (k = 0; k < N; k++)
               ptr3[i][j] = ptr3[i][j] + ptr1[i][k] * ptr2[k][j];
	       /*ptr3[i][j] = sqrt(ptr1[i][j]);*/
        }
    }

    /* Printing the contents of third matrix. */

    printf ("\n\nFinal Matrix :");
    for (i = 0; i < N; i++) {
        printf ("\n\t");
        for (j = 0; j < N; j++)
            printf (" %4%s", ptr3[i][j],type);
    }

    printf ("\n");
    return (0);
}


/**
  * Write the data type in the changeable as argument
  *
  * @param data: char* pointer to write the data type
  */
void type_data(char** data) {
  switch(sizeof(data)) {
    case sizeof(int):
      *data = 'i';
    break;

    case sizeof(float):
      *data = 'f';
    break;

    case sizeof(short int):
      *data = 'hi';
    break;

    case sizeof(unsigned short int):
      *data = 'hu';
    break;

    case sizeof(unsigned int):
      *data = 'u';
    break;

    case sizeof(double):
      *data = 'f';
    break;

    case sizeof(long double):
      *data = 'lf'
    break;

    default:
      *data = TIPO_PRINT_ERROR;
    break;
  }
}
