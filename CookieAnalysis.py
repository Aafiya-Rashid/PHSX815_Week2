#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
from time import time
import numpy as np
import matplotlib.pyplot as plt

# import our MySort class from python/MySort.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    t1 = time()
    times1 = Sorter.DefaultSort(times)
    times_avg1 = Sorter.DefaultSort(times_avg)
    t2 = time()
    print('Time Taken for Default Sort: ', t2 - t1)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    
    t3 = time()
    times2 = Sorter.InsertionSort(times)
    times_avg2 = Sorter.InsertionSort(times_avg)
    t4 = time()
    print('Time Taken for Insertion Sort: ', t4 - t3)


    weight_t_av1 = np.ones_like(times_avg1)/len(times_avg1)
    weight_t1 = np.ones_like(times1)/len(times1)
    
    weight_t_av2 = np.ones_like(times_avg2)/len(times_avg2)
    weight_t2 = np.ones_like(times2)/len(times2)



    # Time Averages using Default Sort

    title1 = str(Nmeas) + " measurements/experiment with rate " + str(rate) + " cookies/day"
    fig, ax = plt.subplots()
    ax.hist(times_avg1, 100, weights = weight_t_av1, density = True, alpha = 0.3,  facecolor = 'r', label = 'Using Default Sort')
    ax.set_yscale('log')
    plt.xlabel("Average time between missing cookies (days)")
    plt.ylabel("Probability")
    plt.title(title1)
    plt.grid(color = 'k', ls = 'dashed', lw = 0.75, alpha = 0.2)
    
    quant_25, quant_50, quant_75 = np.quantile(times_avg1, 0.25), np.quantile(times_avg1, 0.5), np.quantile(times_avg1, 0.75)
    quants = [[quant_25, 0.8, 0.26], [quant_50, 1, 0.36],  [quant_75, 0.8, 0.46]]
    for i in quants:
        ax.axvline(i[0], color = 'k', alpha = i[1], ymax = i[2], linestyle = 'dashed')
            

    ax.text(quant_25-.08, 0.18, "25th", size = 10, alpha = 0.85)
    ax.text(quant_50-.09, 0.25, "50th", size = 11, alpha = 0.85)
    ax.text(quant_75-.09, 0.4, "75th", size = 10, alpha = 0.85)
    plt.legend(loc = 'upper right')
    plt.savefig('Times_Average_Default_Sort.pdf')
    plt.show()
    
    
    # Time Averages using Insertion Sort

    title1 = str(Nmeas) + " measurements/experiment with rate " + str(rate) + " cookies/day"
    fig, ax = plt.subplots()
    ax.hist(times_avg2, 100, weights = weight_t_av2, density = True, alpha = 0.3,  facecolor = 'b', label = 'Using Insertion Sort')
    ax.set_yscale('log')
    plt.xlabel("Average time between missing cookies (days)")
    plt.ylabel("Probability")
    plt.title(title1)
    plt.grid(color = 'k', ls = 'dashed', lw = 0.75, alpha = 0.2)
 
    quant_25, quant_50, quant_75 = np.quantile(times_avg2, 0.25), np.quantile(times_avg2, 0.5), np.quantile(times_avg2, 0.75)
    quants = [[quant_25, 0.8, 0.26], [quant_50, 1, 0.36],  [quant_75, 0.8, 0.46]]
    for i in quants:
        ax.axvline(i[0], color = 'k', alpha = i[1], ymax = i[2], linestyle = 'solid')    

    ax.text(quant_25-.1, 0.18, "25th", size = 10, alpha = 0.85)
    ax.text(quant_50-.1, 0.25, "50th", size = 11, alpha = 0.85)
    ax.text(quant_75-.1, 0.4, "75th", size = 10, alpha = 0.85)
    plt.legend(loc = 'upper right')
    plt.savefig('Times_Average_Insertion_Sort.pdf')
    plt.show()
    
    
    
    # Times using Default Sort

    title2 = str(Nmeas) + " measurements/experiment with rate " + str(rate) + " cookies/day"
    fig1, ax1 = plt.subplots()
    ax1.hist(times1, 100, weights = weight_t1,  density = True, alpha = 0.5, facecolor = 'm', label = 'Using Default Sort')
    ax1.set_yscale('log')
    plt.xlabel("Time between missing cookies (days)")
    plt.ylabel("Probability")
    plt.title(title2)
    plt.grid(color = 'k', ls = 'dashed', lw = 0.75, alpha = 0.2)
    plt.legend(loc = 'upper right')
    plt.savefig('Times_Default_Sort.pdf')
    plt.show()




    # Times using Insertion Sort

    title2 = str(Nmeas) + " measurements/experiment with rate " + str(rate) + " cookies/day"
    fig1, ax1 = plt.subplots()
    ax1.hist(times2, 100, weights = weight_t2,  density = True, alpha = 0.5, facecolor = 'c', label = 'Using Insertion Sort')
    ax1.set_yscale('log')
    plt.xlabel("Time between missing cookies (days)")
    plt.ylabel("Probability")
    plt.title(title2)
    plt.grid(color = 'k', ls = 'dashed', lw = 0.75, alpha = 0.2)
    plt.legend(loc = 'upper right')
    plt.savefig('Times_Insertion_Sort.pdf')
    plt.show()
