import numpy as np

def rotation3D(coord, alpha, beta, gamma):
    """ """
    num = len(coord)
    Rx = np.mat([[1.,              0.,             0.],
                 [0.,  np.cos(alpha), np.sin(alpha)],
                 [0., -np.sin(alpha), np.cos(alpha)]])

    Ry = np.mat([[ np.cos(beta), 0., np.sin(beta)],
                 [0.,             1.,            0.],
                 [-np.sin(beta), 0., np.cos(beta)]])

    Rz = np.mat([[np.cos(gamma) , np.sin(gamma), 0.],
                 [-np.sin(gamma), np.cos(gamma), 0.],
                 [             0.,             0., 1.]])
    Rmat = Rx * Ry * Rz
    com = np.average(coord, axis=0)
    #coordR = (coord - com) * Rmat + com
    coordR = np.round(coord * Rmat, 2)
    return coordR.tolist()
