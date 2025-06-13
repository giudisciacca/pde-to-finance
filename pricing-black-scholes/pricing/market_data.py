import yfinance as yf

import numpy as np

class simulation:
    def __init__(self, volatility = 0, drift = 0, dt = 60, S0=1, t0= 0, T=3600):
        
        if volatility == 'heston':
            raise NotImplementedError("Heston model simulation is not implemented yet.")
        self.volatility = volatility
        
        self.drift = drift
        self.dt = dt
        self.S0 = S0
        self.t0 = t0
        self.T = T
    def forward_euler(self):
        # dS = drift * S * dt + volatility * dX
        time = np.arange(self.t0, self.T, self.dt, dtype=np.float64) 
        if np.isscalar(self.volatility):
            self.volatility = np.ones_like(time)*self.volatility    
        sqrt_dt = np.sqrt(self.dt)
        out_value = np.zeros_like(time)
        out_value[0] = self.S0
        normal_set = np.random.randn(len(time))
        for i in range(1,len(time)):
            out_value[i] =  out_value[i-1]*(1+self.drift*self.dt + self.volatility[i-1]*normal_set[i-1]*sqrt_dt)
        return time, out_value
    def forward(self):
        # dS = drift * S * dt + volatility * dX
        time = np.arange(self.t0, self.T, self.dt, dtype=np.float64) 
        if np.isscalar(self.volatility):
            self.volatility = np.ones_like(time)*self.volatility    
        sqrt_dt = np.sqrt(self.dt)
        out_value = np.zeros_like(time)
        out_value[0] = self.S0
        normal_set = np.random.randn(len(time))
        for i in range(1, len(time)):
            dt = self.dt
            drift_term = (self.drift - 0.5 * self.volatility[i-1] ** 2) * dt
            diffusion_term = self.volatility[i-1] * normal_set[i-1] * sqrt_dt
            out_value[i] = out_value[i-1] * np.exp(drift_term + diffusion_term)
        return time, out_value

class bs_analytical:
    def __init__(self):
        return
    def put_option(self):
        pass
    def call_option(self):
        pass
    def digital_call_option(self):
        pass
    def digital_put_option(self):
        pass
    