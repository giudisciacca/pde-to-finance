import numpy as np
import scipy.special
from  pricing.options_classes import Option, Asset

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

    def numerical_call(self):
        pass

def normal_cdf(x):
    return 0.5 * (1 + scipy.special.erf(x / np.sqrt(2)))    


def ddt_matrix(length, dt):
    id = np.identity(length);

    return 
def dds_matrix():
    pass

def d2ds2_matrix():
    pass


class solver:
    def __init__(self)
        return

    def crank_nicolson_solver(length, dt, ds, volatility, rate_of_interest, option):
        pass

    def runge_kutta_solver(length, dt, ds, volatility, rate_of_interest, option):
        pass

    def full_discretization_solver(length, dt, ds, volatility, rate_of_interest, option):
        # get ddt

        # get dds

        # get d2ds2

        # set up matrix A

        # set up matrix B

        # solve for V at each time step

        return
