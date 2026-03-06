import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if ordinates.size < 3:
        raise ValueError

    prev = ordinates[:-2]
    curr = ordinates[1:-1]
    next = ordinates[2:]

    maximum = (prev < curr) & (curr > next)
    minimum = (prev > curr) & (curr < next)

    indexes = np.arange(1, ordinates.size - 1)

    return (indexes[minimum], indexes[maximum])
