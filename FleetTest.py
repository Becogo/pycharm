# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 08:19:41 2020

@author: gz01588
"""


import  asammdf
import pathlib
import numpy as np
import matplotlib.pyplot as plt

####################


def get_varible(mdffilepath,keyvarible):
    mdf = asammdf.MDF(mdffilepath,use_display_names=1,remove_source_from_channel_names=1)
    resampledmdf = mdf.resample(raster=0.1)
    keyvariblesignal=resampledmdf.get(keyvarible)
    keyvaribletime=keyvariblesignal.timestamps
    keyvarible=keyvariblesignal.samples
    
    return keyvarible
    


#########################

#直方图


def getallkeyvarible3():
    
    keyvarible=entry.get()
    
    # 从GUI 获得输入
    
    p = pathlib.Path(r'E:\01.Project\01. GDI\09. A39-II\广州大学城 fleet test\DATA(A39-2 Fleet test)')
    print(p)
    # 获取文件夹对象
    pys = p.glob('*.dat')
    
    #pys是经过yield产生的迭代器
    
    
    keyvarible3=[get_varible(pp,keyvarible) for pp in pys]
    
    #迭代获得所有文件的变量
    
    keyvarible3min=[np.min(i) for i in keyvarible3]
    keyvarible3mmax=[np.max(i) for i in keyvarible3]
    
    plt.figure(1)
    
    from math import pi,sin
    
    
    
    x_cycles = list(range(1,len(keyvarible3min)+1))
    
    plt.scatter(x_cycles,keyvarible3min,s=np.pi*4**2,color='red',marker='o',alpha=0.5,label='%s'%keyvarible)
    
    maxline=[1.05]*len(keyvarible3min)
    minline=[0.95]*len(keyvarible3min)
    
    x=np.arange(len(keyvarible3min))+1
    
    plt.plot(x,maxline,label="maxline",color="red",linewidth=2)
    
    plt.plot(x,minline,label="minline",color="blue",linewidth=2)
    
    
    plt.xlabel('Number of Cycle')
    #设置纵坐标的标题
    # plt.text(23, 45, r'$\mu=15, b=3$')
    
    plt.ylabel('%s'%keyvarible) #绘制y轴
    # plt.title("Histogram : $\mu=mu$,$\sigma=sigma$'")#中文标题 u'xxx' 
    plt.title('fleet test')

    plt.grid(True)  #网格线挂起
    
   
    #设置整个图片的标题
    
    plt.legend(loc='upper right')

    # 展示出我们的图片
    plt.show()
    
    plt.figure(2)
    
    mu =np.mean(keyvarible3min) #计算均值
    sigma =np.std(keyvarible3min)
    
    # 对数据进行切片，将数据按照从最小值到最大值分组，分成20组
    bins = np.linspace(min(keyvarible3min),max(keyvarible3min),20)

# 这个是调用画直方图的函数，意思是把数据按照从bins的分割来画
    plt.hist(keyvarible3min,bins,color = 'steelblue',edgecolor = 'black',label='%s'%keyvarible)
    
    
    from scipy.stats import norm
    y = norm.pdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y 
    
    plt.plot(bins, y, 'r--') #绘制y的曲线
    
    plt.xlabel('%s'%keyvarible)
    #设置纵坐标的标题
    # plt.text(23, 45, r'$\mu=15, b=3$')
    
    plt.ylabel('Probability') #绘制y轴
    # plt.title("Histogram : $\mu=mu$,$\sigma=sigma$'")#中文标题 u'xxx' 
    plt.title("Histogram : $\mu=%s $\sigma= %s"%(mu, sigma))

    # plt.grid(True)  #网格线挂起
    
    plt.grid(axis='y', alpha=0.75)
    #设置整个图片的标题
    
    plt.legend(loc='upper right')

    # 展示出我们的图片
    plt.show()

#######################################
# GUI
import tkinter

win = tkinter.Tk()
win.title("变量提取")
win.geometry("400x100+200+50")

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win, text="提取", command=getallkeyvarible3)
button.pack()

win.mainloop()
