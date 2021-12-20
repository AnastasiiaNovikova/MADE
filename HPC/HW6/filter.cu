#include <stdint.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include <stdio.h>

// kernel
__global__ void Process()
{
    // threadIdx.x
    // threadIdx.y
    // threadIdx.z

    // blockIdx.x
    // blockIdx.y
    // blockIdx.z

    // blockDim.x
    // blockDim.y
    // blockDim.z
    int globalIdx = threadIdx.z * blockDim.x * blockDim.y + threadIdx.y * blockDim.x + threadIdx.x;
    globalIdx+=blockDim.x*blockDim.y*blockDim.z*(blockIdx.z * gridDim.x * gridDim.y + blockIdx.y * gridDim.x + blockIdx.x);
}


int main()
{

    int width, height, bpp;

    unsigned char * rgb_image = stbi_load("/content/drive/MyDrive/cats_and_dogs_small/oxana.jpeg", &width, &height, &bpp, 1);
 
    if (rgb_image == nullptr){
        printf("errror\n");
    }
    else{
        printf("width: %d\n", width);
        printf("height: %d\n", height);
        printf("bpp: %d\n", bpp);
        printf("Length of array: %lu\n", (long unsigned int)( sizeof(rgb_image) / sizeof(rgb_image[0]) ));
         
        printf("%d\n", rgb_image[0]);
        printf("size: %lu\n", sizeof(rgb_image));
        printf("last %d\n", rgb_image[1041120]);
        for(int i=0; i<=2000000; i++){
            if (rgb_image[i] == 0){
                printf("last is: %d\n", i);
                break;
            }
            //printf("%d\n", rgb_image[i]);
        }
    }

    stbi_image_free(rgb_image);
    printf("This is done on CPU\n");

    //Process<<<dim3(2,2,2),dim3(2,2,2)>>>();
    //cudaDeviceSynchronize();
    return 0;
}
