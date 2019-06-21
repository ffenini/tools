## from PIL import Image, ImageDraw, ImageFont, ImageColor # image command from Pillow library

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *  ##### in order to use the MATLAB-like API
import periodictable as pt #### periodic table ex. mass of Cr = pt.Cr.mass
import os
from scipy.constants import * #codata ####to access physical constant
import periodictable as pt #### periodic table ex. mass of Cr = pt.Cr.mass
from inspect import currentframe, getframeinfo 
frameinfo = getframeinfo(currentframe())
from IPython import get_ipython
from IPython.display import display, HTML
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
import savitzky_golay