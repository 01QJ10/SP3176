#!/usr/bin/env python
# coding: utf-8

# In[58]:


def c_predictor(actual, predicted, dist_1, dist_2):
    
    # The function returns speed of light in m/s
    # actual and predicted are actual & predicted dates of emergnece/ immersion in Julian Days
    # dist_1 & dist_2 are distance from the Earth to Io in M km
    
    dist_1 = dist_1*10**9
    dist_2 = dist_2*10**9
    d_t = abs(actual - predicted)*24*3600
    d_D = abs(dist_1 - dist_2)
    return d_D / d_t

def synodic_counter(actual, n):
    
    # The function returns the predicted date of emergence/ immersion after n synodic period
    
    return actual + (n*1.769861)
    
    

