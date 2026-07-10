import numpy as np
import scipy.special
from  pricing.options_classes import Option, Asset
import pricing.market_data as market_data


class BlackScholes:
    """
    A class to represent the Black-Scholes model for option pricing.
    """

    def __init__(self, option):
        """
        Initialises the Black-Scholes model with the given option.
        Solves the Black-Scholes partial differential equation to find the option price:
            d/dt V + 0.5* volatility^2 * S^2 * d^2/dS^2 V + r * S * d/dS V - r * V = 0
        where V is the option price, S is the underlying asset price, r is the risk-free interest rate, 
        and volatility is the volatility of the underlying asset.
        """


        self.option = option;   



    def analytical_put(self):

        d1 = (np.log(self.option.underlying_asset.price / self.option.strike_price) + 
              (self.option.underlying_asset.rate_of_interest + 0.5 * self.option.underlying_asset.volatility ** 2) * self.option.time_to_maturity) / (self.option.underlying_asset.volatility * np.sqrt(self.option.time_to_maturity))
        d2 = d1 - self.option.underlying_asset.volatility * np.sqrt(self.option.time_to_maturity)
        put_price = -(self.option.underlying_asset.price * normal_cdf(-d1) + self.option.strike_price * np.exp(-self.option.underlying_asset.rate_of_interest * self.option.time_to_maturity) * normal_cdf(-d2))
        return put_price

    def analytical_call(self):
        d1 = (np.log(self.option.underlying_asset.price / self.option.strike_price) + 
              (self.option.underlying_asset.rate_of_interest + 0.5 * self.option.underlying_asset.volatility ** 2) * self.option.time_to_maturity) / (self.option.underlying_asset.volatility * np.sqrt(self.option.time_to_maturity))
        d2 = d1 - self.option.underlying_asset.volatility * np.sqrt(self.option.time_to_maturity)
        call_price = (self.option.underlying_asset.price * normal_cdf(d1) - self.option.strike_price * np.exp(-self.option.underlying_asset.rate_of_interest * self.option.time_to_maturity) * normal_cdf(d2))
        return call_price

    def numerical_put(self):
        pass
        #eturn solver.full_discretization_solver(time_length, length, dt, ds, volatility, rate_of_interest, self.option, theta = 0.5   )

    def numerical_call(self):
        pass

def normal_cdf(x):
       return 0.5 * (1 + scipy.special.erf(x / np.sqrt(2)))    


def ddt_matrix(length, dt):
    id = np.identity(length);

    return 
def dds_matrix(length, ds, mode = 'forward'):
    if mode == 'forward':
        dds = np.diag(-np.ones(length-1), 0) + np.diag(np.ones(length-1), 1)
        dds = dds / ds
    else: 
        NotImplementedError("Only forward mode is implemented for d/dS operator.")
    return  dds
    
def d2ds2_matrix(length, ds):
    d2ds2 = np.diag(np.ones(1), -1) + np.diag(-2*np.ones(1), 0) + np.diag(np.ones(1), 1)
    d2ds2 = d2ds2 / (ds**2)
    return d2ds2
    

class solver:
    def __init__(self):
        return




    def full_discretization_solver(time_length, length, dt, ds, volatility, rate_of_interest, option, theta = 0.5   ):
        # d/dt V + 0.5* volatility^2 * S^2 * d^2/dS^2 V + r * S * d/dS V - r * V = 0

        if volatility.size == 1:
            volatility = np.ones(length) * volatility

        # S vector
        S = np.linspace(option.underlying_asset.price * 0.1, option.underlying_asset.price * 10, length)

        V = np.zeros((time_length, length))

        for i in range(length):
            V[i, -1] = option.payoff(S[i]);

        I = np.identity(length)
        for it in range(time_length - 2, -1, -1):
            A = 0.5 * volatility[it] ** 2 * S ** 2 * d2ds2_matrix(length, ds) + rate_of_interest * S * dds_matrix(length, ds) - rate_of_interest 
            V[it, :] = V[it + 1, :] + dt*(theta *  A @ V[it + 1, :] + (1 - theta) * np.linalg.inv(I -dt*A) @ V[it, :] )
            
        return V

    def montecarlo(self, time_length, length, dt, ds, volatility, rate_of_interest, option, theta = 0.5   ):

        input_kwargs = {"volatility": 0.005,
                "drift" : 0.000002,
                "S0" : 100,
                "t0" : 0,
                "T" : 3600*24,
                "dt" : 60}

        sim = market_data.simulation(**input_kwargs)
        t,val = sim.forward()
        visual.plot_signal(t,val)
        avg_val = np.zeros_like(val)
        M = 100
        for i in range(M):
            t,val = sim.forward()
            avg_val += val/M
        return