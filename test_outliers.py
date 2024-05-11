import pandas as pd 
import numpy as np 

from outliers import find_outliers

def gen_data(size, num_outliers):
    """Generates data in size of 'size' and with num_outliers outliers 
    Returns generated data and expected outliers"""

    regular = np.random.randint(700, 710, size)
    low = np.random.randint(1, 25, num_outliers // 2)
    high = np.random.randint(10000, 10100, num_outliers-len(low))

    data = np.concatenate([regular, low, high])
    expected = np.concatenate([low, high])
    np.random.shuffle(data)

    return pd.Series(data), pd.Series(expected)

def test_bench_outliers(benchmark):
    size = 10000 # The size of the data set
    num_outliers = 10 # Number of outliers

    data, expected = gen_data(size, num_outliers)
    indices = benchmark(find_outliers, data)
    outliers = data.loc[indices]
    assert set(expected) == set(outliers), 'Bad result'