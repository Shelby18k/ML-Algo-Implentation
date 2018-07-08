# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 11:37:13 2018

@author: TushaR
"""

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self,visualization=True):
        self.visualization = visualization
        self.colors = {1: 'r',-1: 'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    
    # train
    def fit(self, data):
        pass
    
    def predict(self, features):
        # sign(x.w+b)
        classification = np.sign(np.dot(np.array(features),self.w) + self.b)