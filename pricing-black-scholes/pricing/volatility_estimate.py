import numpy as np

class VolatilityEstimate:
    def __init__(self, time, signal):
        self.time = time

        self.signal = signal
        self.dt = (self.time[-1] - self.time[0])/len(self.time)  # Calculate the time step

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
        _returns = np.diff(self.signal, append=self.signal[-1]) / self.signal  # Calculate returns
        
        # compute moving standard deviation
        window_size = int(window_size_s / self.dt)  # Convert seconds to number of samples
        if window_size <= 0:
            raise ValueError("Window size must be a positive integer.")
        if len(_returns) <= window_size:
            print('Warning: Not enough data points to compute moving average volatility. Returning constant volatility.')
            return np.std(_returns)*np.ones_like(_returns)
          
        out = np.convolve(_returns**2, np.ones(window_size)/window_size, mode='valid')
        # prepend with NaN values to match the length of the original signal
        out = np.concatenate((np.full(window_size - 1, np.nan), np.sqrt(out)))
        return out   
    def exponential_moving_average(self, alpha):
        """
        Calculate the exponential moving average of the signal with a smoothing factor alpha.
        """
        if not (0 < alpha < 1):
            raise ValueError("Alpha must be between 0 and 1.")
        
        ema = np.zeros_like(self.signal)
        ema[0] = self.signal[0]
        
        for i in range(1, len(self.signal)):
            ema[i] = alpha * self.signal[i] + (1 - alpha) * ema[i - 1]
        
        return ema
    
    def garch(self, window_size):
        """
        Calculate the GARCH (Generalized Autoregressive Conditional Heteroskedasticity) volatility estimate.
        This is a simplified version and may not be suitable for all use cases.
        """
        if window_size <= 0:
            raise ValueError("Window size must be a positive integer.")
        
        if len(self.signal) < window_size:
            raise ValueError("Signal length must be greater than or equal to window size.")
        
        garch_volatility = np.zeros_like(self.signal)
        for i in range(window_size, len(self.signal)):
            garch_volatility[i] = np.std(self.signal[i-window_size:i])
        
        return garch_volatility[window_size:]



    def __repr__(self):
        return f"VolatilityEstimate(time={self.time}, signal={self.signal})"


