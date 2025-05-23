from pricing import visual
from pricing import market_data

if __name__ == "__main__":
    # Ticker	Nome
    # run simulation of stock price with given volatilty and drift
    input_kwargs = {"volatility": 0.001,
                    "drift" : 0.001,
                    "S0" : 100,
                    "t0" : 0,
                    "T" : 3600*24,
                    "dt" : 60}
    
    sim = market_data.simulation(**input_kwargs)
    visual.plot_signal(*sim.forward())
    # compute BS price of option

    # Implement delta hedging and test that gains/losses are zero
    
    
    tickers_collection = ['AAPL','MSFT','NVDA',	'AMD','TSLA','META','SPY']
    for ticker_name in tickers_collection:
        # download

        # get options 

        # estimate price with different volatilities

        # estimate the actual volatility

        # compare BS price w.r.t. real 

        # payoff graph over time

        # Implement delta hedging

        # Compute losses/gains 

        # Implement gamma, vega, rho

        # compute losses/gains
        pass

        