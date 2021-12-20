import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule

a = np.random.randn(4,4)
a = np.array([[1.0,2.0,1.0, 0.0],[1.0,2.0,1.0, 0.0],[0.0,0.0,7.0, 0.0],[0.0,0.0,7.0, 0.0]])
a_max = int(np.amax(a))
a = a.astype(np.float32)
b = np.array([0 for _ in range(a_max+1)])
b = b.astype(np.float32)
a_gpu = cuda.mem_alloc(a.nbytes)
b_gpu = cuda.mem_alloc(b.nbytes)
cuda.memcpy_htod(a_gpu, a)
cuda.memcpy_htod(b_gpu, b)

N = np.array([2,2])
N = N.astype(int)
n_gpu = cuda.mem_alloc(N.nbytes)
cuda.memcpy_htod(n_gpu, N)


mod = SourceModule("""
  __global__ void hist(float *a, float *b, int *N)
  {
    //int idx = threadIdx.z * blockDim.y * blockDim.x + threadIdx.y*blockDim.x + threadIdx.x;
    int idx = threadIdx.x + threadIdx.y*4;
    //int idx = threadIdx.y * blockDim.x + threadIdx.x;  
    //int idx = blockIdx.y * blockDim.y * blockDim.x * N[0] + threadIdx.y * blockDim.x * N[0] + blockIdx.x * blockDim.x + threadIdx.x;
    float value = a[idx];
    atomicAdd(&(b[(int)value]), 1); 
  }
  """)
func = mod.get_function("hist")
func(a_gpu, b_gpu, n_gpu, block=(4,4,1), grid=(1,1))
# block=(400,1,1), grid=(1,1))

a_hist = np.empty_like(b)
cuda.memcpy_dtoh(a_hist, b_gpu)
print(a_hist)
print(a)
