import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list = np.array(list)
    list = np.reshape(list, (3, 3))
    print(list)

    calculations = {
        'mean': [np.mean(list, 0).tolist(), np.mean(list, 1).tolist(), np.mean(list)],
        'variance': [np.var(list, 0).tolist(), np.var(list, 1).tolist(), np.var(list)],
        'standard deviation': [np.std(list, 0).tolist(), np.std(list, 1).tolist(), np.std(list)],
        'max': [np.max(list, 0).tolist(), np.max(list, 1).tolist(), np.max(list)],
        'min': [np.min(list, 0).tolist(), np.min(list, 1).tolist(), np.min(list)],
        'sum': [np.sum(list, 0).tolist(), np.sum(list, 1).tolist(), np.sum(list)]
    }
    print(calculations)
    return calculations
calculate([2,6,2,8,4,0,1,5,7])
