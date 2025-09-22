import yfinance as yf
import numpy as np
import scipy.sparse as sp

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
        dt = self.dt
        time = np.arange(self.t0, self.T, dt, dtype=np.float64) 
        if np.isscalar(self.volatility):
            self.volatility = np.ones_like(time)*self.volatility    
        sqrt_dt = np.sqrt(self.dt)
        out_value = np.zeros_like(time)
        out_value[0] = self.S0
        normal_set = np.random.randn(len(time))
        for i in range(1, len(time)):
            
            drift_term = (self.drift - 0.5 * self.volatility[i-1] ** 2) * dt
            diffusion_term = self.volatility[i-1] * normal_set[i-1] * sqrt_dt
            out_value[i] = out_value[i-1] * np.exp(drift_term + diffusion_term)
        return time, out_value
    def forward_vectorised(self):
        dt = self.dt
        time = np.arange(self.t0, self.T, self.dt, dtype=np.float64) 
        D = self._time_derivative_operator(dt,len(time))
        if np.isscalar(self.volatility):
            self.volatility = np.ones_like(time)*self.volatility    
        sqrt_dt = np.sqrt(self.dt)
        normal_set = np.random.randn(len(time))
        drift_term = (self.drift - self.volatility**2) 
        diffusion = self.volatility * normal_set * sqrt_dt/dt
        M = D - sp.eye(len(time))*(drift_term+diffusion) 
        M[0,0] = 1
        b = np.zeros(len(time))
        b[0] = self.S0
        out_value = sp.linalg.spsolve(M, b)
        
        return time, out_value
    def _time_derivative_operator(self, dt, numel):
        D = sp.eye(numel) - sp.diags(np.ones(numel-1), -1)/dt
        return sp.csr_matrix(D)


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
    