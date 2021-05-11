import numpy
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from pylab import show, title, xlabel, ylabel, subplot
import cmath
import itertools

cexp = numpy.vectorize(cmath.exp)
cabs = numpy.vectorize(abs)


def fourier_series(arr):
    """ computes the fourier series coefficients of input signal

    Parameters
    -----------
    arr : numpy array
            input discrete time signal

    Returns
    --------
    out : complex,list
          fourier series coefficients
    """

    n = len(arr)

    w = 2 * cmath.pi / n
    arr = arr[0:n]
    nn = numpy.arange(0, n)
    r = cexp(-1j * w * nn)

    output = [complex(0)] * n
    for k in range(n):
        r = arr * cexp(-1j * w * nn * k)
        output[k] = np.sum(r)

    # print(output)

    return output


# def IFourierSeries(input):
#     """ function reconstructs the signal from fourier series coefficients
#
#     Parameters
#     ---------
#     input : cmath list
#             fourier series coefficients
#
#     Returns
#     -----------
#     out : numpy arrary
#           reconstructed signal
#
#     """
#     N = len(input)
#     w = 2 * cmath.pi / N
#     k = numpy.arange(0, N)
#     output = [complex(0)] * N
#     for n in range(N):
#         r = input * cexp(-1j * w * n * k)
#         output[n] = np.mean(r)
#
#     # print(output.__class__)
#
#     return output


def fourier_sinusoids(source, F, w, Fs, synthesis=None):
    """ the function generates a discrete time sinusoid, computes the fourier series coefficients and plots the time
    and frequency data

        Parameters
        ----------
        source : numpy array
                 the source!

        F : numpy array
            sinusoidal frequency components

        w  : numpy array
             the weights associated with frequency components

        Fs : Integer
             sampling frequency

        synthesis : int
                    if 1 ,reconstructs signal and plots the original and reconstructed
                    signal

    """

    if synthesis is None:
        synthesis = 0

    ts = 1.0 / Fs
    xs = numpy.arange(0, 1, ts)

    # print(xs)

    signal = numpy.zeros(np.shape(xs))

    # print(signal)
    # print("===================================================")

    for i in range(len(F)):
        omega = 2 * np.pi * F[i]
        signal = signal + w[i] * numpy.sin(-omega * xs)
    # plot the time domain signal
    # print(signal)
    # print("===================================================")
    # subplot(2, 1, 1)
    # plt.plot(range(0, len(signal)), signal)
    # xlabel('Time')
    # ylabel('Amplitude')
    # title('time domain')

    # compute the fourier series coefficient

    r1 = fourier_series(source)
    # print(len(r1))
    a1 = cabs(r1)
    # a1 = a1[50:250]
    # plt.plot(np.abs(r1))
    # plt.show()

    # if synthesis == 0:
    #     # plot the frequency domain signal
    #     L = len(a1)
    #     fr = np.arange(0, L)
    #     subplot(2, 1, 2)
    #     plt.stem(fr, a1, 'r')  # plotting the spectrum
    #     xlabel('Freq (Hz)')
    #     ylabel('|Y(freq)|')
    #     title('complete signal')
    #     ticks = np.arange(0, L + 1, 25)
    #     plt.xticks(ticks, ticks)
    #     show()

    # if synthesis == 1:
    #     rsignal = IFourierSeries(r1)
    #     print(np.allclose(rsignal, signal))
    #
    #     subplot(2, 1, 2)
    #     plt.stem(xs, signal)
    #     xlabel('Time')
    #     ylabel('Amplitude')
    #     title('reconstructed signal')
    #     show()


def source():
    return itertools.cycle((np.sin(0), np.sin(1 / 3 * pi), np.sin(2 / 3 * pi), np.sin(3 / 3 * pi), np.sin(4 / 3 * pi),
                            np.sin(5 / 3 * pi), np.sin(6 / 3 * pi)))


def run_algorithm(filename, column_number):
    mode = 2
    x = 0
    cont = []
    cont_x = []

    with open(filename, 'r') as file:
        string_array = np.array(file.readlines())
        float_array = []

        for i in range(len(string_array)):
            for j in range(len(string_array[i].split(' ')) - 1):
                if j == column_number:
                    float_array.append(float(string_array[i].split(' ')[j]))

    n = len(float_array)

    for i in range(n):
        cont.append(np.cos(x))
        cont_x.append(x)
        x += 0.001

    # plt.plot(cont_x, cont)
    # plt.show()

    # vals = source()
    # x = np.array([next(vals) for _ in range(n)])
    x = np.array(float_array)
    # plt.plot(x)
    # plt.show()

    # Compute the FFT
    w = np.fft.fft(x)

    freq = np.fft.fftfreq(n, 1)

    threshold = 10
    idx = np.where(abs(w) > threshold)[0][-1]

    max_f = abs(freq[idx])

    # plt.subplot(211)
    # plt.scatter([max_f, ], [np.abs(w[idx]), ], s=100, color='r')
    # plt.plot(freq[:int(n / 2)], abs(w[:int(n / 2)]))
    # plt.xlabel(r"$f$")

    # plt.subplot(212)
    # plt.plot(1.0 / freq[:int(n / 2)], abs(w[:int(n / 2)]))
    # plt.scatter([1 / max_f, ], [np.abs(w[idx]), ], s=100, color='r')
    # plt.xlabel(r"$1/f$")
    # plt.xlim(0, 20)

    # plt.show()

    # print("hello")
    # print(np.mean(cont))
    # print("===================")

    # plt.plot(pow(np.abs(np.fft.fft(cont)), 2))
    # plt.plot(cont_x, cont)
    # plt.show()

    if mode == 0:
        f = cont_x
        f = np.array(f)
        w = numpy.ones(f.shape)
        # plot the time domain signal and fourier series component
        fourier_sinusoids(x, f, w, 200)

    if mode == 1:
        f = [10, 20]
        f = np.array(f)
        w = numpy.ones(f.shape)
        fourier_sinusoids(x, f, w, 300)

    if mode == 2:
        f = [10]
        f = np.array(f)
        # print(f)
        w = numpy.ones(f.shape)
        # plot the time domain signal and fourier series component
        fourier_sinusoids(x, f, w, 300)

    print(1 / max_f)
    return 1 / max_f != len(float_array), 1 / max_f
