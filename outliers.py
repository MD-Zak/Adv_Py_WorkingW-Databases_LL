def find_outliers(data):
    """find outliers in data and return their index."""
    outliers = data[(data - data.mean()).abs() > 2 * data.std()]
    return outliers.index