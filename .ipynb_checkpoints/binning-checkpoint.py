import numpy as np 
import pandas as pd

dataset = pd.read_excel('data/DATA RUMAH.xlsx')
print(dataset.head())

variable = "HARGA"
x = dataset[variable].values
y = dataset.target

from optbinning import MulticlassOptimalBinning

optb = MulticlassOptimalBinning(name=variable, solver="cp")

optb.fit(x,y)

optb.status

binning_table = optb.binning_table
binning_table.build()