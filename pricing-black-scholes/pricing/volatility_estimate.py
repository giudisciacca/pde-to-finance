import numpy as np

class VolatilityEstimate:
    def __init__(self, time, signal):
        self.time = time

        self.signal = signal
        self.dt = (self.time[-1] - self.time[0])/len(self.time)  # Calculate the time step
        self._returns = np.diff(self.signal, prepend=self.signal[0]) / self.signal  # Calculate returns

    def implied_volatility(self):
        """
        Calculate the implied volatility based on the time and signal.	
        """
        
        return (self.time, self.signal)

    def realized_volatility(self):	
        """
        Calculate the realized volatility based on the time and signal.
        """
        
        return (self.time, self.signal)
    
    def forward_volatility(self):
        """
        Calculate the forward volatility based on the time and signal.
        """
        
        return (self.time, self.signal) 
    
    def moving_average_volatility(self, window_size_s):
        """
        Calculate the moving average of returns over a specified window size.
        """
        #_returns = np.diff(np.log(self.signal),append=np.log(self.signal[-1]))
        
        # compute moving standard deviation
        window_size = int(window_size_s / self.dt)  # Convert seconds to number of samples
        if window_size <= 0:
            raise ValueError("Window size must be a positive integer.")
        if len(self._returns) <= window_size:
            print('Warning: Not enough data points to compute moving average volatility. Returning constant volatility.')
            return np.std(self._returns)*np.ones_like(self._returns)
          
        out = np.convolve(self._returns**2, np.ones(window_size)/window_size, mode='valid')
        # prepend with NaN values to match the length of the original signal
        out = np.concatenate((np.full(window_size - 1, np.nan), np.sqrt(out)))
        return out   
    
    def exponential_moving_average(self, alpha, method = 'riskmetric'):
        """
        Calculate the exponential moving average of the signal with a smoothing factor alpha.
        """
        if not (0 < alpha < 1):
            raise ValueError("Alpha must be between 0 and 1.")
        
        ema = np.zeros_like(self._returns)
        if method=='riskmetric':
            ema[0] = (1-alpha) * self._returns[0]**2
            for n in range(1, len(self._returns)):
                ema[n] = alpha * ema[n-1]+(1-alpha) * self._returns[n]**2
        else:
            for n in range(0, len(self._returns)):
                i = np.arange(0, n + 1)
                ema[n] = (1-alpha) * np.sum( (alpha**(n-i)) * self._returns[i]**2)
        return np.sqrt(ema)
    
    def garch_volatility(self, alpha_arch, alpha_exp, avg_volatility_sq = None ):
        """
        Calculate the GARCH (Generalized Autoregressive Conditional Heteroskedasticity) volatility estimate.
        This is a simplified version and may not be suitable for all use cases.
        """
        garch_volatility_sq = np.zeros_like(self._returns)
         
        if avg_volatility_sq is None:
            avg_volatility_sq = np.var(self._returns)
        for n in range(0, len(self._returns)):
            garch_volatility_sq[n] = alpha_arch*avg_volatility_sq+(1-alpha_arch)* (alpha_exp*garch_volatility_sq[n-1] + (1-alpha_exp)*self._returns[n]**2 )
        return np.sqrt(garch_volatility_sq)
    
    def arch_volatility(self, alpha = 0.05, avg_volatility_sq = None):
        """
        Calculate the ARCH (Autoregressive Conditional Heteroskedasticity) volatility estimate.
        This is a simplified version and may not be suitable for all use cases.
        """
        if len(self.signal) < 2:
            raise ValueError("Signal length must be greater than or equal to 2.")
        arch_volatility_sq = np.zeros_like(self._returns)  
        if avg_volatility_sq is None:
            avg_volatility_sq = np.var(self._returns)
        
        arch_volatility_sq[0] = avg_volatility_sq
        for i in range(1, len(self._returns)):
            arch_volatility_sq[i] = alpha * avg_volatility_sq + (1 - alpha) * np.var(self._returns[:i+1])

        return  np.sqrt(arch_volatility_sq)
    
    def future_ewma_volatility():
        pass
    def future_garch_volatilty():
        pass
    def future_close2close_volatility():
        pass
    def future_parkinson_volatility():
        pass
    def future_garman_and_klass_volatility():
        pass
    def future_rogers_and_satchell_volatility():
        pass

    
    def __repr__(self):
        return f"VolatilityEstimate(time={self.time}, signal={self.signal})"


