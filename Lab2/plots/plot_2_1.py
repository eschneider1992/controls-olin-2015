import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Time (s),C1 (V),C2 (V)
    filename = "part2_q1_"
    voltages = ['6V', '9V', '10V', '11V', '12V']
    colors = ['b', 'g', 'r', 'c', 'm']
    filetype = ".csv"

    # for i in range(len(colors)):
    for i in [0, 4]:
        time, current_V, voltage = \
            get_double_column_data(filename + voltages[i] + filetype)

        current = calculate_current_from_voltage(current_V)
        filtered_current = moving_average(current, 3)

        if i == 0:
            plt.subplot(2, 2, 1)
            plt.title('Motor Voltage Driven in 6V Square Wave')
        else:
            plt.subplot(2, 2, 3)
            plt.title('Motor Voltage Driven in 12V Square Wave')

        plt.plot(time, voltage, color=colors[i], linewidth=1)
        plt.plot([time[0], time[1]],
                 [voltage[0], voltage[1]],
                 color=colors[i], label=voltages[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Motor Voltage (V)')

        if i == 0:
            plt.subplot(2, 2, 2)
            plt.title('Current, Motor Driven in 6V Square Wave')
        else:
            plt.subplot(2, 2, 4)
            plt.title('Current, Motor Driven in 12V Square Wave')
        plt.plot(time, filtered_current, color=colors[i], linewidth=1)
        plt.plot([time[0], time[1]],
                 [filtered_current[0], filtered_current[1]],
                 color=colors[i], label=voltages[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A)')
    plt.show()


if __name__ == '__main__':
    main()
