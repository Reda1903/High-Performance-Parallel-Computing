import csv
import matplotlib.pyplot as plt
import sys
import numpy as np
N   = []
gpu_cpu = []
i=0
Ns = sys.argv
Ns = Ns[1:]

fig, ax = plt.subplots()
cmap = plt.get_cmap('gnuplot')
number = len(Ns)
colors = [cmap(i) for i in np.linspace(0, 1, number)]
for n in Ns:
    with open('gpu_with_cpu_' + n + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        N   = []
        gpu_cpu = []
        for row in csv_reader:
            N.append(int(row[0]))
            gpu_cpu.append(int(row[1]))
        plt.plot(N, gpu_cpu, color=colors[i], label='$N={n}$'.format(n=n))
        i=i+1
plt.xlabel('% GPU')
plt.ylabel('Time (ms)')
plt.legend(loc='best')
plt.title('SGEMM time processing when using GPU to compute X% of \n '+
          'the working charge for a multiple dimension N')
plt.savefig('gpu_with_cpu.png')