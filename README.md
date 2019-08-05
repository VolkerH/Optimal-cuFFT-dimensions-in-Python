[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VolkerH/Optimal-cuFFT-dimensions-in-Python/master?filepath=Optimal%20Dimensions%20for%20cuFFT.ipynb)

# Optimal cuFFT dimensions in Python
Code snippets to calculate optimal array dimensions for cuFFT (see https://docs.nvidia.com/cuda/cufft/index.html) in Python.

This repo contains the following:

* `rainbow_cufft_pad.py` a python file without dependencies that will quickly find the closest optimal array dimension for a given input value by looking it up in a rainbow table. Usage: simple import and call `lookup_larger` or `lookup_smaller`. The rainbow tables contains
values for what I consider reasonable input sizes. Use the Jupyter notebook to create a larger rainbow table if required. 
* `factorization_cufft_pad.py` provides python functions that find the closest optimal dimension for a given input value by factorization. This has additional dependencies and is considerably slower than the table lookup. However, it hanles edge cases better.
* [An explanatory Jupyter notebook](https://github.com/VolkerH/Optimal-cuFFT-dimensions-in-Python/blob/master/Optimal%20Dimensions%20for%20cuFFT.ipynb) This notebook illustrates the usage of both methods and also contains the code that generates the rainbow table. You can run this notebook in your web browser by clicking on the _launch binder_ button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VolkerH/Optimal-cuFFT-dimensions-in-Python/master?filepath=Optimal%20Dimensions%20for%20cuFFT.ipynb)
## See also

for related approaches see:

* `findOptimalDimension` in https://github.com/dmilkie/cudaDecon/blob/master/RL-Biggs-Andrews.cpp uses recursive modulo operations for testing
* `scipy.fftpack` https://github.com/scipy/scipy/blob/maintenance/1.3.x/scipy/fftpack/helper.py#L99 used to use a rainbow table to be fast for small array sizes but had a fallback. This has meanwhile changed (haven't looked in detail at their new code).
