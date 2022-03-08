import numpy as np
from numpy.lib.stride_tricks import as_strided
from typing import Callable
from pyterator import iterate


PADDING_SIZE = 2
WINDOW_SIZE = (3,3)
DTYPE = np.uint16
WINDOW = np.array([[256,128,64],[32,16,8],[4,2,1]], dtype=DTYPE)


def get_algorithm(f) -> list:
    raw_algorithm = next(f).strip()
    return [i for i, ch in enumerate(raw_algorithm) if ch=='#']

def get_padding_value(algorithm: list) -> Callable:
    if 0b111111111 not in algorithm and 0b000000000 in algorithm:
        return lambda i: i%2  
    else:
        return lambda _: 0

def enhance(X: np.ndarray, algorithm: list, pad_value: int) -> np.ndarray:
    """Enhances a non-padded 2D array"""

    X = np.pad(X, (PADDING_SIZE,), constant_values=pad_value).astype(DTYPE)
    h, w = X.shape
    
    # Define output fields
    shape = (h-2, w-2) + WINDOW_SIZE
    strides = tuple(stride*X.itemsize for stride in [h, 1, h, 1])
    
    # 2D convolution
    fields = as_strided(X, shape=shape, strides=strides)
    binaries = np.tensordot(fields, WINDOW)
    
    # Convert to light and dark pixels
    return np.isin(binaries, algorithm) * 1

def get_initial_img(f) -> list:
    f.seek(0)
    return (
        iterate(f).skip(2).filter_map(str.strip)
        .map(lambda line: [1 if x=='#' else 0 for x in line])
        .to_list()
    )

if __name__ == '__main__':
    f = open("day19.txt", "r")

    algorithm = get_algorithm(f)
    padding_value = get_padding_value(algorithm)

    img = get_initial_img(f)
    for i in range(50):
        img = enhance(img, algorithm, padding_value(i))

    print(img.sum())
    f.close()