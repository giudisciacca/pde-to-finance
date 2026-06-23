import pricing.market_data as md
import numpy as np

class Option:
    def __init__(self, strike_price, current_time, time_to_maturity, asset, quality='call'):
        self.strike_price = strike_price;
        self.current_time = current_time;
        self.time_to_maturity = time_to_maturity;
        self.underlying_asset = asset;
        self.quality = quality;

    def payoff(self, underlying_price):
        if self.quality == 'call':
            return np.maximum(underlying_price - self.strike_price, 0)
        elif self.quality == 'put':
            return np.maximum(self.strike_price - underlying_price, 0)
        else:
            raise ValueError("Invalid option quality. Must be 'call' or 'put'.")


class Asset:
    def __init__(self, price, drift, volatility, rate_of_interest):
        self.price = price;
        self.drift = drift;
        self.volatility = volatility;
        self.rate_of_interest = rate_of_interest;
        self.time = None;
        self.signal = None;

    def assign_signal(self, time, signal):
        self.time = time;
        self.signal = signal;

    def simulate_price_path(self, time):
        self.time = time;
        input_kwargs = {"volatility": self.volatility,
                "drift" : self.drift,
                "S0" : self.price,
                "t0" : self.time[0],
                "T" : self.time[-1],
                "dt" : (self.time[1] - self.time[0])/len(self.time)}

        sim = md.simulation(**input_kwargs)
        _, self.signal = sim.forward()

if __name__ == "__main__":
    asset = Asset(price=100, drift=0.05, volatility=0.2, rate_of_interest=0.01)
    option = Option(strike_price=110, current_time=0, time_to_maturity=1, asset=asset, quality='call')
    print(option.payoff(120))  # Should print 10
    print(option.payoff(90))   # Should print 0




