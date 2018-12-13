import cmath
import imageio
import cv2
import numpy as np
from math import log, ceil
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt


def omega(p, q):
    return cmath.exp((2.0 * cmath.pi * 1j * q) / p)



def fft(x):
    n = len(x)

    if n == 1:
        return x

    Feven, Fodd = fft(x[0::2]), fft(x[1::2])
    combined = [0] * n

    for m in range(int(n/2)):
        combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
        combined[int(m + n/2)] = Feven[m] - omega(n, -m) * Fodd[m]

    return combined

def pad2(x):
    m, n = np.shape(x)
    M, N = 2 ** int(ceil(log(m, 2))), 2 ** int(ceil(log(n, 2)))
    F = np.zeros((M, N), dtype=x.dtype)
    F[0:m, 0:n] = x

    return F, m, n


def fft2(f):
    f, m, n = pad2(f)
    return np.transpose(fft(np.transpose(fft(f)))), m, n

def ifft2(F, m, n):
    f, M, N = fft2(np.conj(F))
    f = np.matrix(np.real(np.conj(f)))/(M*N)
    return f[0:m, 0:n]

def plot_spectrum(im_fft):
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5), cmap=plt.cm.gray)
    plt.colorbar()

a = np.arange(4).reshape(2,2)
fourier = fft2(a)
real_fft = np.abs(fourier[0])
img_fft = np.imag(fourier[0])
print(type(real_fft))
inv = -fourier[0]
print(fourier[0][0][0])
k = np.arange(4, dtype=complex).reshape(2,2)
for i in range (a.shape[0]):
    for j in range (a.shape[1]):
        k[i][j] = complex(real_fft[i][j], img_fft[i][j])
i_fourier = ifft2(fourier[0], a.shape[0], a.shape[1])
print(real_fft)
print(k)



