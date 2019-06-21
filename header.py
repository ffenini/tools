## from PIL import Image, ImageDraw, ImageFont, ImageColor # image command from Pillow library
import time
import datetime
import pandas as pd
import numpy as np
import scipy as sp
import string
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *  ##### in order to use the MATLAB-like API
import periodictable as pt #### periodic table ex. mass of Cr = pt.Cr.mass
import os,shutil
from scipy.constants import * #codata ####to access physical constant
from scipy.interpolate import *
from scipy.stats import *
import periodictable as pt #### periodic table ex. mass of Cr = pt.Cr.mass
from inspect import currentframe, getframeinfo 
from PIL import Image, ImageDraw, ImageFont, ImageColor # image command from Pillow library
import matplotlib.image as mpimg
from matplotlib.patches import Circle
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from decimal import getcontext, Decimal #setting the precisions of the digits in the output
from matplotlib.cbook import get_sample_data
frameinfo = getframeinfo(currentframe())

#from IPython.display import display, HTML
#get_ipython().magic('matplotlib inline')
matplotlib.rcParams.update({'font.size': 20, 'font.family': 'serif'})


import plotly
plotly.__version__
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='filfe', api_key='0ptV4cglDaHsYvvT9Xu8')
from plotly.tools import FigureFactory as FF
import plotly.graph_objs as go
import peakutils  ###finding peaks
from savitzky_golay import *
from pHcalc.pHcalc import Acid, Neutral, System

from collections import OrderedDict #for ordering the lists imported, see XRD general plotting chromites
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition, mark_inset)
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from FW_calculator import *  #tool for calculating Formula weights of chemical formulas
def cm2inch(a):
    inch = 2.54
    a=a/inch
    return a

def list_files1(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith('.' + extension)]

def cv_splitter(voltage,current):
    cv,cur=[],[]
    check=[]
    voltage_list=voltage.tolist()
    current_list=current.tolist()
    data={}
    cycle=1
    for i in voltage_list:
        vi=voltage_list.index(i)
        check.append((i,0))
        if check[vi][0]==check[0][0] and vi>0:
            if check[0][1]==0:
                cv.append(i)
                cur.append(current_list[vi])
                check[0][0]=1
            else:
                ciclo={'Voltage':cv,'Current':cur} #creating the new entry for data frame
                cycle_name='C'+str(cycle) #defining the name of the new entry
                cycle=cycle+1 #moving to next cycle
                check=[] #resetting counter
                data[cycle_name]=ciclo #inserting new entry
                voltage_list=voltage_list[vi:] 
                current_list=current_list[vi:]
                if  len(voltage_list)==0: # in order to avoid to create a phantom entry 'C lastcyc +1 ':{'Voltage':[],'Current':[]}
                    break
        else:
            cv.append(i)
            cur.append(current_list[vi])    
    
    return data
        