# Optimal cuFFT dimensions in Python
Code snippet to calculate optimal array dimensions for cuFFT in Python


This repo contains a short python code snippet in the form of a [Jupyter notebook](https://github.com/VolkerH/Optimal-cuFFT-dimensions-in-Python/blob/master/Optimal%20Dimensions%20for%20cuFFT.ipynb) to calculate optimal array dimensions for arrays to use with cuFFT (see https://docs.nvidia.com/cuda/cufft/index.html).

## Requirements

* `sympy`
* `numpy`

## See also

for similar approaches see

* `findOptimalDimension` in https://github.com/dmilkie/cudaDecon/blob/master/RL-Biggs-Andrews.cpp uses recursive modulo operations for testing
* `scipy.fftpack` https://github.com/scipy/scipy/blob/master/scipy/fftpack/helper.py uses a rainbow table to be fast for small array sizes but is otherwise complicated
