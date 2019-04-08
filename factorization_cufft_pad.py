from sympy.ntheory import factorint
import warnings
import numpy as np

def is_optimal_for_cuFFT(n: int, allowed_factors) -> bool:
    factorization = factorint(n)
    if len(factorization) == 0: # factorint(1) returns empyt dict
        return False
    factors = set(factorization.keys())
    return factors.issubset(set(allowed_factors))
    
def _closest_optimal(n: int, search_next_largest: bool, allowed_factors) -> int:
    while(not is_optimal_for_cuFFT(n, allowed_factors) and n>=1):
        if search_next_largest:
            n += 1
        else:
            n -= 1
    # edge case: decreasing search with start value smaller than allowed factor
    if n < min(allowed_factors):
        
        warnings.warn(f"{n}One provided dimension is smaller than smallest allowed factor and search direction is decreasing")
        return(min(allowed_factors))
    return n

def closest_optimal(n, search_next_largest: bool=True, allowed_factors=(2,3,5,7)):
    """ Finds closest optimal array dimensions for cuFFT
    
    Parameters
    ----------
    n : iterable of integers
        Input dimensions
    search_next_largest : bool
        if True (default) search closest optimal dimensions that are larger or equal to original
        otherwise look for smaller ones. 
    allowed_factor: tuple of integers
        allowed factors in decomposition. Defaults to (2,3,5,7) which are the factors listed in 
        the cuFFT documentation. 
    
    Returns
    -------
    np.array of ints
        optimal dimensions for cuFFT
        
        
    See also
    --------
    https://docs.nvidia.com/cuda/cufft/index.html
    
    """
    n = np.asarray(n)
    scalar_input = False
    if n.ndim == 0:
        n = n[None] 
        scalar_input = True
    ret = np.array([_closest_optimal(ni, search_next_largest, allowed_factors) for ni in n])
    if scalar_input:
        return ret[0]
    return ret