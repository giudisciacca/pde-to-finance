import matplotlib.pyplot as plt
import matplotlib


def plot_signal(time, value, **kwargs):
    plt.figure()
    if type(value) is not list:
        plt.plot(time, value, label='Signal' if 'label' not in kwargs else kwargs['label'])
    else:
        for i, v in enumerate(value):
            plt.plot(time, v, label=f'Signal {i+1}' if 'label' not in kwargs else kwargs['label'][i])
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time [s]' if 'xlabel' not in kwargs else kwargs['xlabel'])
    plt.ylabel('Value' if 'ylabel' not in kwargs else kwargs['ylabel'])
    plt.title('Signal Plot' if 'title' not in kwargs else kwargs['title'])
    plt.show(block=False)
    


