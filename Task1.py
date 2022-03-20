#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 22:06:03 2022

@author: tahaelmoudden
"""

import pandas as pd
import numpy as np 
import matplotlib as plt


path_in = '/Users/tahaelmoudden/Desktop/wave.txt'
path_to ='/Users/tahaelmoudden/Desktop/header.txt'

def header_sav (path_in, path_to):
    data = pd.read_csv(path_in)
    header = data.iloc[0:11,0]
    header.to_csv(path_to, index =False)
    absorb = pd.read_csv(path_in, delimiter = '\t', header = 13)
    return absorb


absorb = header_sav(path_in, path_to)
steps = 3
#problem de rawnge +1-1
def equalizer_1(data,steps):
    data_one =pd.DataFrame()
    list_name = np.concatenate((data.columns.values[:2],(data.columns.values[2:].astype(float)).astype(int)))
    
    data_name = data.set_axis(list_name,axis=1, inplace=False)
    beg =list_name[2]
    end = list_name[-1]
    space= end-beg
    data_one["Time1"] = data_name.iloc[:,0]
    data_one["time"] = data_name.iloc[:,1]
    for i in range(space):
        name = beg+i
        data_one[name] = data_name[name].mean(axis = 1)
    if steps != 1:

        data_two = pd.DataFrame()
        data_two["Time1"] = data_name.iloc[:,0]
        data_two["time"] = data_name.iloc[:,1]
        for i in range(space//2 ):
            cor1, cor2 = (2+steps*i), (2+steps*i+steps)
   
            if cor2 >= len(data_one.columns.values):
                break
  
            name_in = (data_one.columns.values[cor1]+data_one.columns.values[cor2])//steps
            data_two[name_in] = data_one[data_one.columns[cor1:cor2]].mean(axis=1)
        data_one =data_two
    return data_one

def waves_over_time(wave_1, wave_2, data):
    waves_difference = pd.DataFrame()
    waves_difference["time"] = data.iloc[:,1]
    waves_difference ["value"] = data[wave_1]- data[wave_2]
    waves_difference.plot(x = "time",y="value", color="red")
    return  waves_difference
    
def better_plotting (data, path):
    time= data.iloc[:, 0]
    time_correction =( time -1540456324789)/1000
    data["time"] = time_correction
    data.plot(x = "time",y="value", color="red")
    plt.pyplot.xlabel('x values')
    plt.pyplot.ylabel('y values')
    plt.pyplot.title('plotted x and y values')
    plt.pyplot.legend(['line 1'])
    plt.pyplot.savefig('plot.png', dpi=300, bbox_inches='tight')
    return data

def all_plotting(data, dat_Reduced):
    plotage =plt.pyplot.plot(data.iloc[0,2:])
    plotage =plt.pyplot.plot(dat_Reduced.iloc[0,2:])
    
    
    
    
hhh = equalizer_1(absorb,steps)
lolol=waves_over_time(331,321,hhh)
#aaaaaaaaaa= better_plotting(lolol,456)
#all_plotting(absorb,hhh)
