#-*-coding:utf-8-*-
import math
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab

#RGB与HSV的转换
def H_S_V(filename):
    img = cv2.imread(filename,cv2.IMREAD_COLOR)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    aH, aS, aV = cv2.split(HSV)
    H = np.array(aH).flatten()
    S = np.array(aS).flatten()
    V = np.array(aV).flatten()
    return H, S, V



def calcu(H, S, V, H1, S1, V1):
    R = 100.0;
    angle = 30.0;
    h = R * math.cos(angle / 180 * math.pi)
    r = R * math.sin(angle / 180 * math.pi)

    sum = 0.0
    for i in range(0, len(H)):
        # HSV三维空间坐标计算公式
        x1 = r * V[i] * S[i] * math.cos(H[i] / 180.0 * math.pi)
        y1 = r * V[i] * S[i] * math.sin(H[i] / 180.0 * math.pi)
        z1 = h * (1 - V1[i]);

        x2 = r * V1[i] * S1[i] * math.cos(H1[i] / 180.0 * math.pi)
        y2 = r * V1[i] * S1[i] * math.sin(H1[i] / 180.0 * math.pi)
        z2 = h * (1 - V2[i])

        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2

        sum = sum + dx * dx + dy * dy + dz * dz
        eucli_dean = math.sqrt(sum)
        return eucli_dean

# if __name__ == 'main':
H1, S1, V1 = H_S_V('pic1.jpg')
H2, S2, V2 = H_S_V('pic2.jpg')
eucli_dean = calcu(H1, S1, V1,H2, S2, V2 )
print(eucli_dean)

