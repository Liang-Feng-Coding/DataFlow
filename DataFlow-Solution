import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data_file1 = pd.read_csv('20180912_mudstone-1st.csv')
data_file2 = pd.read_csv('dilution_factor.csv')
data_file3 = pd.read_csv('w-2a_value.csv')

isotope = data_file1['isotope']
sensors1 = data_file1.loc[:,'isotope':'smp53']
sensors2 = data_file2.loc[:,'sample':'DF']
sensors3 = data_file3.loc[:,'isotope':'w-2a']

a1 = sensors1['smp1']

# before Rh103
def Rh(i):
    Rh = a1[8]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][8]*sensors1['smp'+str(i)+''][0:9]
    return Rh

# before In115
def In(i):
    In = a1[11]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][11]*sensors1['smp'+str(i)+''][9:12]
    return In

# before Re187
def Re(i):
    Re = a1[33]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][33]*sensors1['smp'+str(i)+''][12:34]
    return Re

# around Bi209
def Bi(i):
    Bi = a1[33]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][33]*sensors1['smp'+str(i)+''][12:34]
    return Bi

# Medium resolution Rh103
def RhM(i):
    RhM = a1[47]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][47]*sensors1['smp'+str(i)+''][39:51]
    return RhM

# High resolution Bi209
def BiH(i):
    BiH = a1[47]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][47]*sensors1['smp'+str(i)+''][39:51]
    return BiH

# spike calibration concat
def spike(i):
    spike = pd.concat([Rh(i),In(i),Re(i),Bi(i),RhM(i),BiH(i)])
    return spike
