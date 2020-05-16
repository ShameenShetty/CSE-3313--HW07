from scipy.signal import spectrogram
from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

import sys


def processTones(name, L, fs, samplesPerTone) :
    """
        We read the data from csv file using np.genfromtxt, where we assign a type
        float to it (dtype=float), and we split by commas (delimiter=",")
    """
    csvData = np.genfromtxt(name, dtype=float, delimiter=",")


    # fb is the freq that the bandpass is designed to pass, depending on the frequencies
    fb = np.array([697, 770, 852, 941, 1209, 1336, 1477])

    # our filter coefficients for the filters fb, fb is a 2D array which has a length of
    # len(fb)
    filterCoeff = [[] * L for _ in range(len(fb))]
    
    #h is the array holding all the filter coeff for all values of fb
    h = []

    """
        For the below nested for loop, we generate the filter coefficients for each value of 
        fb (697, 770, 852, etc), and store it in filterCoefficient. Then once all the
        values have been generated, we append that to h
    """
    fbLen = len(fb)
    for i in range(fbLen):
        f_b = fb[i]
        for n in  range(L):
            theta = (2 * np.pi * f_b * n) / fs
            result = (2 * np.cos(theta)) / L
            filterCoeff[i].append(result)
        h.append(filterCoeff[i])


    convolvedOutput = []
    meanValues = []

    fig1, axs1 = plt.subplots()
    axs1.set_title('Frequency Responses of Bandpass Filters')

    for i in range(fbLen):
        convolveResult = np.convolve(h[i], csvData)

        convolvedOutput.append(convolveResult)

        meanResult = np.mean(convolveResult[:4000]**2)
        meanValues.append(abs(meanResult))

        w, h = freqz(filterCoeff[i], 1, fs = fs)
        plt.plot(abs(w), abs(h))


    # Here we are finding the highest and secondHighest values for np.mean(y**2)
    # to find what are the specific tones in the signal
    highest = max(meanValues[0], meanValues[1])
    secondHighest = min(meanValues[0], meanValues[1])
    highestPos = 0
    secondHighestPos = 0
    for i in range(2,len(meanValues)):  
        if meanValues[i]>highest:  
            secondHighest=highest 
            highest=meanValues[i]
            highestPos = i
        elif meanValues[i]>secondHighest and highest != meanValues[i]:  
            secondHighest=meanValues[i]
            secondHighestPos = i 
        else: 
            if secondHighest == highest: 
                secondHighest = meanValues[i] 

    firstFreq = fb[highestPos]
    secFreq = fb[secondHighestPos]
    """ Getting the spectrogram for the specific set of tones in the filter bank """
    t = np.arange(0, 1, 1/fs)
    x = []
    for i in range(fbLen):
        f_b = fb[i]
        x_i = list(np.cos(2 * np.pi * f_b * t))
        x = x + x_i
        x = np.array(x)
    
    f, t, Sxx = spectrogram(x, fs)
    plt.figure()
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Spectogram for a specific set of tones")
    
    plt.show()

#############  main  #############
if __name__ == "__main__":
    filename = "tones.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone, 
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)
    
    print(phoneNumber)
