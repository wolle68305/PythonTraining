
import matplotlib.pyplot as plt

def create_Plot(**plot_params):
    print(plot_params)
    plt.plot([1,2,3], [5,6,5], **plot_params)
    plt.show()

create_Plot(color="r", linewidth=10, linestyle="dashed")