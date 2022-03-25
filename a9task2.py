#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Christina Chen 
czxc@bu.edu
Assignment 9 task 2
Pricing Path-Dependent Options

Functions include 

class MCStockOption, which inherits from MCStockSimulator, and value(self)

class MCEuroCallOption which inherits from the base class MCStockOption.
class MCEuroPutOption which inherits from the base class MCStockOption.
 
class MCAsianCallOption which inherits from the base class MCStockOption
class MCAsianPutOption which inherits from the base class MCStockOption


class MCLookbackCallOption which inherits from the base class MCStockOption.
class MCLookbackPutOption which inherits from the base class MCStockOption. 



"""


from a9task1 import MCStockSimulator
import numpy as np
import math 

class MCStockOption(MCStockSimulator): 
    '''class MCStockOption, which inherits from MCStockSimulator  
    will encapsulate the idea of a Monte Carlo stock option, and will 
    contain some additional data members
    '''
                                     

    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials): 
         '''s, which is the initial stock price
         x, which is the option’s exercise price
         t, which is the time to maturity (in years) for the option
         r, which is the annual risk-free rate of return
         sigma, which is the annual standard deviation of returns on the underlying stock
         nper_per_year, which is the number of discrete time periods per year with which to evaluate the option, and
         num_trials, which is the number of trials to run when calculating the value of this option
         '''
         super().__init__(s, t, r, sigma, nper_per_year) #just rename mu as r 
         self.r = r #idk if this is right? 
         self.x = x
         self.num_trials = num_trials
         
         
    def __repr__(self): 
         
        '''returns a string representation of the MCstockoption'''
        string = f'MCStockOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string 
    
    
    def value(self):
        '''which will return the value of the option.  '''
        
        print('Base class MCStockOption has no concrete implementation of .value().')
        return 0
    
    
    
    def stderr(self):
        '''which will return the standard error of this option’s value. '''
        
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        
        return 0
        
                                         

class MCEuroCallOption(MCStockOption): 
    '''class definition for the class MCEuroCallOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCEuroCallOption'''
        string = f'MCEuroCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the call option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        call_euro = np.array([max((self.generate_simulated_stock_values()[-1] - self.x) , 0) * exp for x in range(self.num_trials)])
        
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
        



class MCEuroPutOption(MCStockOption): 
    '''class definition for the class MCEuroPutOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCEuroPutOption'''
        string = f'MCEuroPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the put option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        call_euro = np.array([max((self.x - self.generate_simulated_stock_values()[-1]) , 0) * exp for x in range(self.num_trials)])
        
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
        



class MCAsianCallOption(MCStockOption): 
    '''class definition for the class MCAsianCallOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCAsianCallOption'''
        string = f'MCAsianCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the call option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        #call_euro = np.array([max((np.mean(self.generate_simulated_stock_values()[-1]) - self.x) , 0) * exp for x in range(self.num_trials)])
        call_euro = np.array([max(np.mean(self.generate_simulated_stock_values()) - self.x , 0) * exp for x in range(self.num_trials)])
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
        
 

class MCAsianPutOption(MCStockOption): 
    '''class definition for the class MCAsianPutOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCAsianPutOption'''
        string = f'MCAsianPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the put option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        call_euro = np.array([max(self.x - np.mean(self.generate_simulated_stock_values()) , 0) * exp for x in range(self.num_trials)])
        
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
             
     


class MCLookbackCallOption(MCStockOption): 
    '''class definition for the class MCLookbackCallOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCLookbackCallOption'''
        
        string = f'MCLookbackCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the lookback call option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        #call_euro = np.array([max((np.mean(self.generate_simulated_stock_values()[-1]) - self.x) , 0) * exp for x in range(self.num_trials)])
        call_euro = np.array([max(max(self.generate_simulated_stock_values()) - self.x , 0) * exp for x in range(self.num_trials)])
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
        




class MCLookbackPutOption(MCStockOption): 
    '''class definition for the class MCLookbackPutOption which inherits from the base class MCStockOption'''
    
    
    
    def __repr__(self): 
         
        '''returns a string representation of the MCLookbackPutOption'''
        string = f'MCLookbackPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years),' #seems s=${self.s}, is throwing error?? 
        string += f' r={self.r:.2f}, sigma={self.sigma:.2f},'
        string += f' nper_per_year={self.nper_per_year}, num_trials={self.num_trials})'
        return string



    def value(self):
        '''which will return the value of the lookback put option.  '''
        
        #values =  self.generate_simulated_stock_values()[-1] # NEED TO CALL THIS EVERYTIME FOR EACH TRIAL 
        exp = math.e ** (-1 * self.r * self.t)
        #trials = self.num_trials
        call_euro = np.array([max(self.x - min(self.generate_simulated_stock_values()) , 0) * exp for x in range(self.num_trials)])
        
        #call_value = np.mean(call_euro)
        self.mean = np.mean(call_euro) 
        self.stdev = np.std(call_euro) #do we need this right now? oh for the stderr 

        return self.mean 
    

                                    
if __name__ == '__main__': 
    
    # option = MCStockOption(90, 100, 1.0, 0.1, 0.3, 250, 10)
    # print(option)
    # call = MCEuroCallOption(90, 100, 1, 0.1, 0.3, 100, 1000)
    # print(call) 
    # print(call.value())
    # print(call.stderr())
    
    
    # call = MCEuroCallOption(90, 100, 1, 0.1, 0.3, 100, 1000)
    # print(call)
    # print(call.value())
    # print(call.stderr())
    # call.num_trials = 100000
    # print(call.value())
    # print(call.stderr())
    # bs_call = BSEuroCallOption(90, 100, 1.0, 0.3, 0.10)
    # print(bs_call.value())
    # put = MCEuroPutOption(100, 100, 1.0, 0.1, 0.3, 100, 1000)
    # print(put)
    # print(put.value())
    # print(put.stderr())
    
    
    # acall = MCAsianCallOption(35, 30, 1.0, 0.05, 0.25, 100, 100000)
    # print(acall.value())
    # print(acall.stderr())
    
    # aput =  MCAsianPutOption(100, 100, 1, 0.05, 0.30, 100, 1000)
    # print(aput)
    # print(aput.value())
    # print(aput.stderr())
    
    
    
    lcall = MCLookbackCallOption(100, 100, 1, 0.05, 0.30, 100, 1000)
    print(lcall)
    print(lcall.value())
    print(lcall.stderr())
                                      
                