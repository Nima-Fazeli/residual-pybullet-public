import matplotlib.pyplot as plt
from matplotlib import ticker, cm
import numpy as np
import pdb
import pandas as pd
from sklearn.metrics import mean_squared_error


def get_error(te, ts):
    rg = 0.0245
    M = 200

    te[:, 2] = np.unwrap(te[:, 2])
    ts[:, 2] = np.unwrap(ts[:, 2])
    
    v1 = te[:, :3] * np.array([1., 1., 0.0245])
    v2 = ts[:, :3] * np.array([1., 1., 0.0245])
    rmse = np.sqrt(mean_squared_error(v1.flatten(), v2.flatten()))

    return rmse

def loadSimData(num=5):
    # load csv file for trajectory
    dataPrefix = './simulated-trajectories/'
    traj = pd.read_csv(dataPrefix + 'trajSim_{}.csv'.format(num)).to_numpy()
    return traj

# load empirical data
def loadEmpData(num=5):
    dataPrefix = './dice-data-processed/'
    traj = pd.read_csv(dataPrefix + 'traj_{}.csv'.format(num)).to_numpy()
    return traj

if __name__ == '__main__':
    trajSim = loadSimData()
    trajEmp = loadEmpData()

    print(np.column_stack((trajSim[:, 0], trajEmp[:, 0])))
