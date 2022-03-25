#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Christina Chen 
czxc@bu.edu
Assignment 9 task 1
Monte Carlo Sumulation for Stock returns 
Functions include 
class definition for MCStockSimulator, generate_simulated_stock_returns(self), 
generate_simulated_stock_values(self), plot_simulated_stock_values(self, num_trials = 1)

"""

import numpy as np 
import matplotlib.pyplot as plt #produce graphs 
import math 

class MCStockSimulator: 
    '''class definition for a stocksimulator'''
    
    def __init__(self, s, t, mu, sigma, nper_per_year): 
        '''constructor for class with paramaters 
        s (the current stock price in dollars),
        t (the option maturity time in years),
        mu (the annualized rate of return on this stock),
        sigma (the annualized standard deviation of returns),
        nper_per_year (the number of discrete time periods per year)'''
        self.s = s
        self.t = t
        self.mu = mu 
        self.sigma = sigma 
        self.nper_per_year = nper_per_year
        
        
        
    def __repr__(self): 
        
        '''returns a string representation of the stock simulator'''
        string = f'MCStockSimulator (s=${self.s:.2f}, t={self.t:.2f} (years), mu={self.mu:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year})'
        return string 
    

    
    def generate_simulated_stock_returns(self):
        '''generate and return a np.array (numpy array) containing 
        a sequence of simulated stock returns over the time period t
        '''
        
        dt = 1 / self.nper_per_year #length of period
        periods = int(self.t * self.nper_per_year) #length of array or number of returns 
        #period = np.arange(periods)
       
        z = np.random.normal(size = periods) #have to specify size here, make an array on this variable
        
        returns = (self.mu - ((self.sigma ** 2) / 2))  * dt 
        returns += z * self.sigma * (dt ** 0.5)
        
         
        # #annual_return = self.mu + z * self.sigma 
        # for i in range(periods): waitt use numpy array functionality! Prof said don't need for loop
        #     discrete_period_return = (self.mu - ((self.sigma ** 2) / 2 ) * dt + z * self.sigma * (dt ** 0.5))
        #     a = np.append(a, discrete_period_return)
        
        return returns 
      
        
      
        
    def generate_simulated_stock_values(self):
          '''will generate and return a np.array (numpy array) containing a sequence 
          of stock values, corresponding to a random sequence of stock return. 
          '''
         # s_last = self.s no, just index the array 
          returns = self.generate_simulated_stock_returns() #generates an array of stock returns 
          #returns *= math.e ** (returns) 
          
          a = np.zeros(len(returns) + 1) #need an extra element to print current self.s
          a[0] = self.s #current stock price is the first element
          #a = [a[i-1] * math.exp(returns[i - 1]) for i in range(1, len(a))] #messed up current price, you need to index?
          
          for i in range(1, len(a)):
                  a[i] = a[i-1] * math.exp(returns[i - 1])
          
         
          return a 
       
        
           
    
    def plot_simulated_stock_values(self, num_trials = 1):
          '''that will generate a plot of of num_trials series of simulated stock returns. 
          num_trials is an optional parameter; if it is not supplied, the default value of 1 will be used.
          '''
          
           #if type(num_trials) != None: 

          simulate = np.array( [self.generate_simulated_stock_values() for i in range(num_trials)] ) #takes into account if type(num_trials) == None? 
          plt.plot(simulate.T)
         # print(simulate)
          plt.title(f'{num_trials} simulated trials')
          plt.ylabel('$ value')
          plt.xlabel('years')
          

  
if __name__ == '__main__': 
    
    # sim = MCStockSimulator(100, 1, 0.1, 0.3, 250)
    # print(sim)
    # # sim = MCStockSimulator(100, 1, 0.10, 0.30, 2)
    # # print(sim.generate_simulated_stock_returns())
    
    
    # #sim = MCStockSimulator(100, 1, 0.10, 0.30, 4)
 
    
    
    # sim = MCStockSimulator(100, 2, 0.10, 0.30, 24)
    # print(sim.plot_simulated_stock_values())

    
    # sim = MCStockSimulator(100, 2, 0.10, 0.30, 250)
    # sim.plot_simulated_stock_values(5)
 
    sim = MCStockSimulator(100, 2, 0.10, 0.30, 24)
    print(sim.generate_simulated_stock_values())
    
    
    
    