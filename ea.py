import numpy as np
import matplotlib.pyplot as plt
import time


# ------------- SA 退火不稳定态 --------------
def sa_jc(x, n):
    select_point = np.random.randint(len(x))
    signal = True
    while signal:
        random_point = np.random.randint(n)
        if random_point != x[select_point]:
            x[select_point] = random_point
            signal = False

    return x


# ------------- GA 算法参数 --------------
population = 100
iteration = 1000
mutate = 0.2
cross = 0.8


# ------------- GA 交叉与变异 --------------
def jc():
    pass


def by():
    pass


def select():
    pass

# ------------- 模型参数 --------------
k = 5
n = 50
z = 8349.497103
p_list = [
[	0.00,238.36,24.68,3.99,36.49,13.38,259.10,15.21,19.26,515.49,13.25,5.45,12.38,12.36,423.01,103.56,299.89,409.62,14.50,169.88,98.64,36.67,57.92,281.40,10.76,123.48,199.37,215.65,28.09,145.93,17.99,16.81,218.58,28.67,100.34,22.29,131.69,8.94,348.82,19.42,19.82,64.74,181.39,8.91,68.07,156.92,2.88,136.29,53.94,70.31,],
[	238.36,0.00,6.35,4.91,51.00,18.32,224.88,22.49,9.04,497.46,2.36,7.02,3.45,30.20,30.44,114.01,487.09,383.99,2.05,227.94,115.18,23.90,95.69,95.51,15.13,72.34,301.84,132.54,5.44,7.10,13.23,14.63,335.26,22.77,430.34,72.91,179.31,1.84,66.82,37.41,37.08,57.18,195.65,11.93,5.39,61.22,8.20,83.90,55.49,8.75,],
[	24.68,6.35,0.00,3.05,12.19,52.59,17.44,29.33,16.74,2.11,23.04,23.28,21.68,32.56,18.65,27.77,16.37,15.14,15.96,12.13,12.56,19.99,9.93,33.01,15.20,12.86,19.41,15.32,12.57,15.02,14.14,12.84,12.56,20.00,12.68,15.05,21.63,50.71,58.50,8.08,8.51,18.90,16.98,11.70,10.68,53.61,17.04,18.76,11.80,16.93,],
[	3.99,4.91,3.05,0.00,11.20,11.92,14.82,14.52,10.91,12.68,10.88,12.86,14.47,14.54,11.05,14.25,11.59,13.59,14.33,15.16,14.45,12.22,11.52,13.43,13.89,13.71,15.29,14.19,11.44,12.98,13.97,12.46,11.00,14.77,13.74,13.40,12.11,11.44,13.89,11.54,11.69,14.24,15.52,11.37,11.18,12.97,14.44,14.48,12.20,11.53,],
[	36.49,51.00,12.19,11.20,0.00,25.48,30.62,53.94,56.14,52.42,8.05,13.05,9.57,5.88,2.65,5.32,6.55,0.75,11.62,8.78,8.77,36.57,32.40,40.86,8.17,10.37,11.75,15.70,54.19,61.31,21.41,13.56,12.98,33.65,27.26,48.81,49.67,18.73,18.73,6.55,7.20,14.71,16.11,45.06,38.22,45.07,14.21,12.96,29.61,36.00,],
[	13.38,18.32,52.59,11.92,25.48,0.00,42.06,79.97,43.10,34.28,20.84,36.62,21.25,23.28,16.60,17.48,19.19,16.67,11.08,9.37,8.28,13.98,7.95,20.05,15.86,13.67,15.72,21.55,13.23,17.16,12.42,10.80,10.47,12.22,5.91,11.50,6.39,81.76,80.05,16.88,16.85,17.16,26.79,21.03,19.96,81.54,17.31,15.41,11.98,14.72,],
[	259.10,224.88,17.44,14.82,30.62,42.06,0.00,53.07,204.35,199.82,6.77,25.73,13.54,56.66,51.15,55.71,60.30,54.82,20.67,26.34,71.72,28.50,16.06,17.49,4.56,64.99,277.00,27.98,32.16,166.02,8.03,7.64,7.66,21.80,27.04,85.86,93.09,13.28,6.67,2.82,2.79,94.58,238.01,34.15,89.56,97.09,17.60,18.87,31.98,130.97,],
[	15.21,22.49,29.33,14.52,53.94,79.97,53.07,0.00,124.98,124.49,18.70,16.97,12.23,64.66,14.45,20.76,12.80,15.17,25.60,21.40,20.33,41.51,28.51,33.31,11.07,9.28,7.81,7.72,8.21,7.36,11.15,13.68,10.31,36.51,37.89,37.23,44.98,22.19,39.73,34.24,33.88,45.15,54.98,6.70,6.14,15.40,1.99,7.33,2.66,7.63,],
[	19.26,9.04,16.74,10.91,56.14,43.10,204.35,124.98,0.00,3.02,2.32,7.47,8.76,10.66,8.64,90.39,87.90,90.40,18.52,18.00,125.33,18.61,9.49,31.83,11.87,24.28,28.72,26.60,49.30,93.97,18.18,16.98,15.05,26.47,21.86,11.44,15.71,34.91,23.18,11.37,11.51,82.06,90.46,9.45,9.04,23.71,22.15,120.72,55.08,94.81,],
[	515.49,497.46,2.11,12.68,52.42,34.28,199.82,124.49,3.02,0.00,18.88,6.28,9.30,111.45,109.51,10.68,10.75,7.33,20.55,201.86,95.89,8.50,79.99,82.58,13.23,50.06,249.02,138.11,68.62,16.84,18.65,16.79,302.92,13.93,14.45,22.43,159.01,18.56,75.11,12.63,12.14,14.53,53.83,30.28,150.78,229.16,24.35,133.36,22.69,84.27,],
[	13.25,2.36,23.04,10.88,8.05,20.84,6.77,18.70,2.32,18.88,0.00,4.77,6.86,7.13,6.97,7.06,6.80,6.78,13.96,14.00,13.90,13.76,13.69,13.90,16.10,16.33,16.22,16.25,16.21,16.08,16.16,16.19,16.15,16.18,16.00,16.33,16.32,6.90,6.73,6.63,6.84,6.83,6.89,6.86,6.72,6.85,4.81,4.88,4.79,5.01,],
[	5.45,7.02,23.28,12.86,13.05,36.62,25.73,16.97,7.47,6.28,4.77,0.00,23.30,18.88,14.21,26.73,11.87,14.95,18.75,13.82,16.04,15.12,11.56,21.77,23.54,20.69,20.06,27.18,21.15,24.77,24.02,20.72,17.18,20.45,24.79,19.68,22.04,33.72,45.10,17.30,17.88,17.80,39.93,20.20,20.44,43.71,19.23,18.94,18.12,23.54,],
[	12.38,3.45,21.68,14.47,9.57,21.25,13.54,12.23,8.76,9.30,6.86,23.30,0.00,27.52,20.20,27.14,21.05,18.53,29.12,27.66,20.29,25.48,17.64,17.20,24.86,17.92,17.93,19.83,17.99,17.97,17.87,18.76,17.06,25.57,22.45,17.41,17.54,26.05,28.04,17.03,17.96,23.82,25.99,22.43,20.08,26.41,21.18,18.10,17.45,23.98,],
[	12.36,30.20,32.56,14.54,5.88,23.28,56.66,64.66,10.66,111.45,7.13,18.88,27.52,0.00,17.70,12.90,11.24,4.66,91.29,25.74,121.66,46.77,3.54,15.44,13.93,125.48,126.66,239.88,47.53,107.83,16.62,13.83,10.40,24.29,20.68,38.75,46.05,80.73,61.19,7.48,6.81,116.34,106.14,34.93,29.90,87.83,11.80,143.73,29.32,121.46,],
[	423.01,30.44,18.65,11.05,2.65,16.60,51.15,14.45,8.64,109.51,6.97,14.21,20.20,17.70,0.00,92.03,253.15,488.75,4.10,201.50,18.82,13.05,40.86,345.79,8.93,78.50,295.92,109.81,9.60,14.72,9.77,10.55,44.30,25.57,432.78,92.77,213.68,10.88,31.96,3.29,3.34,70.16,267.46,8.68,205.29,187.28,20.14,36.86,25.70,90.03,],
[	103.56,114.01,27.77,14.25,5.32,17.48,55.71,20.76,90.39,10.68,7.06,26.73,27.14,12.90,92.03,0.00,89.09,88.67,12.68,7.82,109.03,20.68,46.45,52.91,19.46,118.22,118.38,120.40,5.02,3.60,22.35,23.85,21.76,11.30,4.48,6.33,11.20,26.31,30.50,5.23,4.94,24.83,28.35,45.15,35.07,33.96,14.49,11.35,38.41,32.22,],
[	299.89,487.09,16.37,11.59,6.55,19.19,60.30,12.80,87.90,10.75,6.80,11.87,21.05,11.24,253.15,89.09,0.00,25.74,24.32,212.20,69.88,27.55,28.88,31.64,5.51,45.80,259.05,105.63,11.44,17.82,8.92,6.97,229.92,14.60,35.82,2.12,2.12,4.95,67.79,27.28,26.63,54.79,157.25,6.25,39.26,352.06,25.17,6.84,41.11,78.59,],
[	409.62,383.99,15.14,13.59,0.75,16.67,54.82,15.17,90.40,7.33,6.78,14.95,18.53,4.66,488.75,88.67,25.74,0.00,16.46,172.34,109.70,14.16,108.41,108.89,16.47,133.08,166.65,48.66,14.39,68.68,3.68,2.30,112.87,35.73,364.30,17.43,77.60,9.13,240.64,19.61,20.27,84.15,224.19,6.93,78.54,54.85,16.04,119.19,1.28,43.05,],
[	14.50,2.05,15.96,14.33,11.62,11.08,20.67,25.60,18.52,20.55,13.96,18.75,29.12,91.29,4.10,12.68,24.32,16.46,0.00,43.16,42.19,73.45,39.33,55.16,17.50,13.79,13.15,23.14,16.27,13.78,15.53,14.00,12.28,16.29,15.71,17.29,20.30,31.48,57.23,15.52,15.28,40.58,32.55,25.51,20.34,72.51,15.59,22.07,15.95,17.07,],
[	169.88,227.94,12.13,15.16,8.78,9.37,26.34,21.40,18.00,201.86,14.00,13.82,27.66,25.74,201.50,7.82,212.20,172.34,43.16,0.00,76.64,25.41,10.97,11.29,16.85,81.27,269.91,88.56,52.65,20.25,22.52,14.53,13.37,37.01,113.33,80.26,390.34,14.24,317.47,19.88,20.32,25.71,46.99,23.57,35.87,337.53,1.04,140.57,22.88,55.43,],
[	98.64,115.18,12.56,14.45,8.77,8.28,71.72,20.33,125.33,95.89,13.90,16.04,20.29,121.66,18.82,109.03,69.88,109.70,42.19,76.64,0.00,29.98,39.50,39.17,12.05,11.08,14.96,13.89,18.47,15.63,20.71,19.83,18.40,31.01,33.78,8.26,6.32,5.98,8.46,38.60,38.12,102.44,102.02,29.59,31.77,29.47,20.82,21.76,33.79,35.77,],
[	36.67,23.90,19.99,12.22,36.57,13.98,28.50,41.51,18.61,8.50,13.76,15.12,25.48,46.77,13.05,20.68,27.55,14.16,73.45,25.41,29.98,0.00,33.67,33.47,14.77,14.69,18.88,16.72,14.94,20.96,15.68,16.16,12.03,24.39,26.58,27.01,26.35,27.61,31.36,7.11,7.03,14.54,12.66,12.87,11.45,6.40,2.00,1.69,1.62,7.66,],
[	57.92,95.69,9.93,11.52,32.40,7.95,16.06,28.51,9.49,79.99,13.69,11.56,17.64,3.54,40.86,46.45,28.88,108.41,39.33,10.97,39.50,33.67,0.00,1.12,0.89,1.49,1.77,1.90,33.98,34.33,19.44,19.76,19.10,24.25,24.59,35.57,36.06,7.12,7.32,5.83,6.26,12.31,12.46,14.25,15.08,14.54,18.04,19.08,16.29,17.15,],
[	281.40,95.51,33.01,13.43,40.86,20.05,17.49,33.31,31.83,82.58,13.90,21.77,17.20,15.44,345.79,52.91,31.64,108.89,55.16,11.29,39.17,33.47,1.12,0.00,17.68,31.58,109.63,50.08,48.13,132.60,28.58,27.12,385.69,21.79,417.77,85.39,251.55,21.72,156.21,32.99,33.59,34.94,128.59,23.26,38.60,42.22,17.69,131.56,48.10,43.56,],
[	10.76,15.13,15.20,13.89,8.17,15.86,4.56,11.07,11.87,13.23,16.10,23.54,24.86,13.93,8.93,19.46,5.51,16.47,17.50,16.85,12.05,14.77,0.89,17.68,0.00,42.13,47.22,42.91,42.36,43.90,48.82,45.21,40.94,46.91,47.64,48.31,40.78,42.46,43.42,41.55,41.46,47.53,48.54,43.67,42.71,47.24,41.60,40.98,41.77,43.76,],
[	123.48,72.34,12.86,13.71,10.37,13.67,64.99,9.28,24.28,50.06,16.33,20.69,17.92,125.48,78.50,118.22,45.80,133.08,13.79,81.27,11.08,14.69,1.49,31.58,42.13,0.00,44.50,41.32,16.99,19.39,3.75,4.78,1.43,34.46,33.87,37.20,39.71,16.99,16.90,0.88,0.55,102.95,102.16,31.49,31.42,33.58,7.78,8.66,56.77,117.80,],
[	199.37,301.84,19.41,15.29,11.75,15.72,277.00,7.81,28.72,249.02,16.22,20.06,17.93,126.66,295.92,118.38,259.05,166.65,13.15,269.91,14.96,18.88,1.77,109.63,47.22,44.50,0.00,69.26,31.60,132.12,27.22,22.48,20.75,30.53,27.92,90.63,88.27,16.50,12.51,22.56,23.15,98.12,232.57,25.63,104.97,102.69,12.35,143.60,9.39,100.60,],
[	215.65,132.54,15.32,14.19,15.70,21.55,27.98,7.72,26.60,138.11,16.25,27.18,19.83,239.88,109.81,120.40,105.63,48.66,23.14,88.56,13.89,16.72,1.90,50.08,42.91,41.32,69.26,0.00,73.78,112.74,16.16,12.58,10.26,22.90,17.56,43.76,42.92,28.21,18.33,2.23,2.79,87.21,82.73,42.57,10.69,7.47,20.85,39.99,18.03,91.22,],
[	28.09,5.44,12.57,11.44,54.19,13.23,32.16,8.21,49.30,68.62,16.21,21.15,17.99,47.53,9.60,5.02,11.44,14.39,16.27,52.65,18.47,14.94,33.98,48.13,42.36,16.99,31.60,73.78,0.00,92.54,25.01,24.73,22.04,38.05,35.45,36.57,36.22,15.53,11.70,23.03,23.18,26.35,27.36,33.50,35.71,38.50,11.67,14.51,29.16,30.03,],
[	145.93,7.10,15.02,12.98,61.31,17.16,166.02,7.36,93.97,16.84,16.08,24.77,17.97,107.83,14.72,3.60,17.82,68.68,13.78,20.25,15.63,20.96,34.33,132.60,43.90,19.39,132.12,112.74,92.54,0.00,21.87,18.87,18.98,23.21,18.53,79.10,80.48,18.17,22.92,29.55,29.68,62.39,61.13,34.68,27.17,31.95,21.23,24.51,30.95,11.96,],
[	17.99,13.23,14.14,13.97,21.41,12.42,8.03,11.15,18.18,18.65,16.16,24.02,17.87,16.62,9.77,22.35,8.92,3.68,15.53,22.52,20.71,15.68,19.44,28.58,48.82,3.75,27.22,16.16,25.01,21.87,0.00,14.36,10.32,18.43,12.40,12.87,18.18,16.37,17.60,11.30,11.43,17.37,19.63,13.36,11.58,12.69,6.88,9.83,4.32,8.95,],
[	16.81,14.63,12.84,12.46,13.56,10.80,7.64,13.68,16.98,16.79,16.19,20.72,18.76,13.83,10.55,23.85,6.97,2.30,14.00,14.53,19.83,16.16,19.76,27.12,45.21,4.78,22.48,12.58,24.73,18.87,14.36,0.00,413.18,13.72,17.54,89.22,127.61,18.01,130.59,22.62,22.86,5.52,13.23,16.75,57.99,342.47,1.23,118.56,7.58,86.20,],
[	218.58,335.26,12.56,11.00,12.98,10.47,7.66,10.31,15.05,302.92,16.15,17.18,17.06,10.40,44.30,21.76,229.92,112.87,12.28,13.37,18.40,12.03,19.10,385.69,40.94,1.43,20.75,10.26,22.04,18.98,10.32,413.18,0.00,2.33,347.93,21.48,43.34,13.49,248.01,14.56,14.41,2.40,287.27,17.96,65.52,203.84,5.84,152.94,23.47,35.66,],
[	28.67,22.77,20.00,14.77,33.65,12.22,21.80,36.51,26.47,13.93,16.18,20.45,25.57,24.29,25.57,11.30,14.60,35.73,16.29,37.01,31.01,24.39,24.25,21.79,46.91,34.46,30.53,22.90,38.05,23.21,18.43,13.72,2.33,0.00,37.65,43.15,38.75,13.44,19.89,11.91,11.53,12.46,20.32,16.64,14.88,16.76,21.75,22.90,21.03,26.70,],
[	100.34,430.34,12.68,13.74,27.26,5.91,27.04,37.89,21.86,14.45,16.00,24.79,22.45,20.68,432.78,4.48,35.82,364.30,15.71,113.33,33.78,26.58,24.59,417.77,47.64,33.87,27.92,17.56,35.45,18.53,12.40,17.54,347.93,37.65,0.00,11.49,123.77,6.76,108.96,0.32,1.12,11.76,45.44,37.76,33.71,149.20,16.04,40.62,57.05,99.88,],
[	22.29,72.91,15.05,13.40,48.81,11.50,85.86,37.23,11.44,22.43,16.33,19.68,17.41,38.75,92.77,6.33,2.12,17.43,17.29,80.26,8.26,27.01,35.57,85.39,48.31,37.20,90.63,43.76,36.57,79.10,12.87,89.22,21.48,43.15,11.49,0.00,99.00,18.08,19.44,16.90,17.15,17.70,22.90,24.37,27.11,29.24,21.55,16.67,42.28,44.89,],
[	131.69,179.31,21.63,12.11,49.67,6.39,93.09,44.98,15.71,159.01,16.32,22.04,17.54,46.05,213.68,11.20,2.12,77.60,20.30,390.34,6.32,26.35,36.06,251.55,40.78,39.71,88.27,42.92,36.22,80.48,18.18,127.61,43.34,38.75,123.77,99.00,0.00,18.22,61.74,2.65,2.49,54.44,124.30,10.55,75.65,94.54,13.21,31.59,5.37,11.00,],
[	8.94,1.84,50.71,11.44,18.73,81.76,13.28,22.19,34.91,18.56,6.90,33.72,26.05,80.73,10.88,26.31,4.95,9.13,31.48,14.24,5.98,27.61,7.12,21.72,42.46,16.99,16.50,28.21,15.53,18.17,16.37,18.01,13.49,13.44,6.76,18.08,18.22,0.00,19.24,4.80,4.92,15.27,21.18,17.30,5.64,53.40,5.41,9.03,4.52,8.92,],
[	348.82,66.82,58.50,13.89,18.73,80.05,6.67,39.73,23.18,75.11,6.73,45.10,28.04,61.19,31.96,30.50,67.79,240.64,57.23,317.47,8.46,31.36,7.32,156.21,43.42,16.90,12.51,18.33,11.70,22.92,17.60,130.59,248.01,19.89,108.96,19.44,61.74,19.24,0.00,19.83,20.13,76.35,261.01,30.72,36.55,338.31,9.21,101.01,42.26,43.43,],
[	19.42,37.41,8.08,11.54,6.55,16.88,2.82,34.24,11.37,12.63,6.63,17.30,17.03,7.48,3.29,5.23,27.28,19.61,15.52,19.88,38.60,7.11,5.83,32.99,41.55,0.88,22.56,2.23,23.03,29.55,11.30,22.62,14.56,11.91,0.32,16.90,2.65,4.80,19.83,0.00,36.09,35.36,35.89,30.04,30.15,30.22,11.30,11.39,11.91,11.92,],
[	19.82,37.08,8.51,11.69,7.20,16.85,2.79,33.88,11.51,12.14,6.84,17.88,17.96,6.81,3.34,4.94,26.63,20.27,15.28,20.32,38.12,7.03,6.26,33.59,41.46,0.55,23.15,2.79,23.18,29.68,11.43,22.86,14.41,11.53,1.12,17.15,2.49,4.92,20.13,36.09,0.00,101.49,0.41,3.65,5.66,125.17,19.82,58.55,19.58,71.65,],
[	64.74,57.18,18.90,14.24,14.71,17.16,94.58,45.15,82.06,14.53,6.83,17.80,23.82,116.34,70.16,24.83,54.79,84.15,40.58,25.71,102.44,14.54,12.31,34.94,47.53,102.95,98.12,87.21,26.35,62.39,17.37,5.52,2.40,12.46,11.76,17.70,54.44,15.27,76.35,35.36,101.49,0.00,88.90,30.20,29.15,31.23,13.22,13.25,25.95,32.68,],
[	181.39,195.65,16.98,15.52,16.11,26.79,238.01,54.98,90.46,53.83,6.89,39.93,25.99,106.14,267.46,28.35,157.25,224.19,32.55,46.99,102.02,12.66,12.46,128.59,48.54,102.16,232.57,82.73,27.36,61.13,19.63,13.23,287.27,20.32,45.44,22.90,124.30,21.18,261.01,35.89,0.41,88.90,0.00,24.74,110.95,112.01,20.18,152.33,51.02,22.96,],
[	8.91,11.93,11.70,11.37,45.06,21.03,34.15,6.70,9.45,30.28,6.86,20.20,22.43,34.93,8.68,45.15,6.25,6.93,25.51,23.57,29.59,12.87,14.25,23.26,43.67,31.49,25.63,42.57,33.50,34.68,13.36,16.75,17.96,16.64,37.76,24.37,10.55,17.30,30.72,30.04,3.65,30.20,24.74,0.00,23.01,26.20,4.36,4.64,1.12,4.20,],
[	68.07,5.39,10.68,11.18,38.22,19.96,89.56,6.14,9.04,150.78,6.72,20.44,20.08,29.90,205.29,35.07,39.26,78.54,20.34,35.87,31.77,11.45,15.08,38.60,42.71,31.42,104.97,10.69,35.71,27.17,11.58,57.99,65.52,14.88,33.71,27.11,75.65,5.64,36.55,30.15,5.66,29.15,110.95,23.01,0.00,2.69,3.61,163.39,3.23,34.37,],
[	156.92,61.22,53.61,12.97,45.07,81.54,97.09,15.40,23.71,229.16,6.85,43.71,26.41,87.83,187.28,33.96,352.06,54.85,72.51,337.53,29.47,6.40,14.54,42.22,47.24,33.58,102.69,7.47,38.50,31.95,12.69,342.47,203.84,16.76,149.20,29.24,94.54,53.40,338.31,30.22,125.17,31.23,112.01,26.20,2.69,0.00,18.03,150.36,20.90,87.35,],
[	2.88,8.20,17.04,14.44,14.21,17.31,17.60,1.99,22.15,24.35,4.81,19.23,21.18,11.80,20.14,14.49,25.17,16.04,15.59,1.04,20.82,2.00,18.04,17.69,41.60,7.78,12.35,20.85,11.67,21.23,6.88,1.23,5.84,21.75,16.04,21.55,13.21,5.41,9.21,11.30,19.82,13.22,20.18,4.36,3.61,18.03,0.00,84.17,82.36,85.59,],
[	136.29,83.90,18.76,14.48,12.96,15.41,18.87,7.33,120.72,133.36,4.88,18.94,18.10,143.73,36.86,11.35,6.84,119.19,22.07,140.57,21.76,1.69,19.08,131.56,40.98,8.66,143.60,39.99,14.51,24.51,9.83,118.56,152.94,22.90,40.62,16.67,31.59,9.03,101.01,11.39,58.55,13.25,152.33,4.64,163.39,150.36,84.17,0.00,48.98,135.38,],
[	53.94,55.49,11.80,12.20,29.61,11.98,31.98,2.66,55.08,22.69,4.79,18.12,17.45,29.32,25.70,38.41,41.11,1.28,15.95,22.88,33.79,1.62,16.29,48.10,41.77,56.77,9.39,18.03,29.16,30.95,4.32,7.58,23.47,21.03,57.05,42.28,5.37,4.52,42.26,11.91,19.58,25.95,51.02,1.12,3.23,20.90,82.36,48.98,0.00,136.25,],
[	70.31,8.75,16.93,11.53,36.00,14.72,130.97,7.63,94.81,84.27,5.01,23.54,23.98,121.46,90.03,32.22,78.59,43.05,17.07,55.43,35.77,7.66,17.15,43.56,43.76,117.80,100.60,91.22,30.03,11.96,8.95,86.20,35.66,26.70,99.88,44.89,11.00,8.92,43.43,11.92,71.65,32.68,22.96,4.20,34.37,87.35,85.59,135.38,136.25,0.00,],
]
p = np.array(p_list)
t_list = [559,37, 223, 453, 128, 657, 81, 897, 529, 312,
     258,495, 63, 66, 72, 128, 337, 717, 305, 40,
     30, 665, 82, 251, 224, 162, 142, 379, 61, 58,
     425,60, 33, 162, 199, 572, 63, 85, 22, 246,
     467,29, 62, 193, 257, 485, 150, 24, 11, 235,
     120,826, 125, 713, 81, 383, 435, 15, 194, 431,
     130,336, 148, 93, 667, 210, 432, 641, 176, 362,
     13, 2, 589, 101, 57, 196, 52, 427, 787, 331,
     162,57, 372, 109, 795, 249, 0, 11, 31, 179,
     253,154, 204, 184, 29, 126, 11, 655, 98, 259
]
t = np.array(t_list)
# 记录最好的目标值和解
best_show = 10000
best_value = list()
best_solution = list()


# ---------- 生成初始解 -----------
x = np.zeros((population, k))
for pop in range(population):
    x[pop] = np.random.choice(n, k)


# ---------- 计算 y_ij -----------
def calculate_y(n, x):
    y = np.zeros((n, n))
    for i in x:
        for j in x:
            if i != j:
                y[i, j] = 1
                y[j, i] = 1
    return y


# ---------- 计算目标函数 ------------
def aim_value(z, x, y, p, n):
    aim_one = 0
    aim_two = 0
    for i in range(len(x)):
        aim_one += t[x[i]]
        for j in range(n):
            aim_two += y[i, j] * p[i, j]

    return z - aim_one - 0.5 * aim_two


start_time = time.time()
# ------------- GA --------------
for iter in range(iteration):
    y = calculate_y(n, x)
    func_value = aim_value(z, x, y, p, n)
    jc()
    by()
    select()

end_time = time.time()
print("算法总耗时：{}.".format(end_time-start_time))
plt.plot(best_value)
plt.xlabel("iteration")
plt.ylabel("optimal value")
plt.title("SA")
plt.show()
# print("最优的值为:", min(best_value))