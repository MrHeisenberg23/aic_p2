#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (int argc, char **argv)
{
    if(argc != 2) exit(-1);
    time_t t;
    float **ptr1, **ptr2, **ptr3;
    int N, col1, row2, col2;
    srand ((unsigned) time (&t));
    int i, j, k;

    N = atoi(argv[1]);
    ptr1 = (float **) malloc (sizeof (float *) * N);
    ptr2 = (float **) malloc (sizeof (float *) * N);
    ptr3 = (float **) malloc (sizeof (float *) * N);

    for (i = 0; i < N; i++) {
        ptr1[i] = (float *) malloc (sizeof (float) * N);
	ptr2[i] = (float *) malloc (sizeof (float) * N);
	ptr3[i] = (float *) malloc (sizeof (float) * N);
    }
    
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            ptr1[i][j] = (float)rand()/(float)(RAND_MAX);
	    ptr2[i][j] = (float)rand()/(float)(RAND_MAX);
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
            printf (" %4f", ptr3[i][j]);
    }

    printf ("\n");
    return (0);
}
