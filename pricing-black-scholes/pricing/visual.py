import matplotlib.pyplot as plt
import matplotlib


def plot_signal(time, value):
    plt.figure()
    plt.plot(time, value)
    plt.grid(True)
    plt.show(block=False)
    


