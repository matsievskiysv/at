#!/usr/bin/env python3

import pandas as pd
import pylab as plt

data = pd.read_csv('data.csv', delimiter=',')

data.slices.unique()

for rad, radname in [('with', 'With longitudinal motion'),
                     ('without', 'Without longitudinal motion')]:
    plt.figure(figsize=(7, 5), dpi=200)
    for scheduler in data.scheduler.unique():
        d = data[data.scheduler == scheduler]
        plt.scatter(d.threads, d[rad], label=scheduler)
    plt.legend()
    plt.grid()
    plt.title(radname)
    plt.xlabel("Threads")
    plt.ylabel("Time, [s]")
    plt.savefig(f"{rad}.png")
    plt.close()
