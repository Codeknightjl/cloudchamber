import cv2
import numpy as np
def find_if_close (cnt1, cnt2):
    row1, row2 = cnt1.shape [0], cnt2.shape [0]
    for i in range(row1):
        for j in range (row2):
            dist = np.linalg.norm(cnt1 [i]- cnt2 [j])
            if abs(dist) < 100:
                return True
            elif i == row1 -1 and j == row2 -1:
                return False
def join_contours (contours):
    LENGTH = len(contours)
    status = np.zeros((LENGTH,1))
    for i in range(LENGTH):
        status[i] = i
    for i, cnt1 in enumerate(contours):
        if i != LENGTH-1:
            for j, cnt2 in enumerate(contours[i+1:]):
                if status[i] == status[j]:
                    continue
                dist = find_if_close (cnt1, cnt2)
                if dist == True:
                    val = min(status [i], status [j])
                    status [i] = status [j] = val

    unified = []
    maximum = int(status.max())+1
    for i in range(maximum):
        pos = np.where(status==i)[0]
        if pos.size != 0:
            cont = np.vstack(contours[i] for i in pos)
            hull = cv2.convexHull(cont)
            unified.append(hull)
    return unified
