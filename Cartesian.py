from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *

class Main:
    @staticmethod
    def plot_lines():
        cox1 = cox1_.get()
        cox2 = cox2_.get()
        coy1 = coy1_.get()
        coy2 = coy2_.get()
        con1 = con1_.get()
        con2 = con2_.get()

        def calculate_line_points(cox, coy, con, x_range):
            if coy != 0:
                y_start = -(cox * x_range[0] + con) / coy
                y_end = -(cox * x_range[1] + con) / coy
                return (x_range[0], y_start), (x_range[1], y_end)
            elif cox != 0:
                x_const = -con / cox
                return (x_const, x_range[0]), (x_const, x_range[1])
            else:
                return None, None

        first_point1, last_point1 = calculate_line_points(cox1, coy1, con1, (-1000, 1200))
        first_point2, last_point2 = calculate_line_points(cox2, coy2, con2, (-1000, 1200))

        if first_point1[0] is not None:
            print("First Point Line 1: ({}, {})".format(first_point1[0], first_point1[1]))
            print("Last Point Line 1: ({}, {})".format(last_point1[0], last_point1[1]))
        else:
            print("No points found on Line 1.")

        if first_point2[0] is not None:
            print("First Point Line 2: ({}, {})".format(first_point2[0], first_point2[1]))
            print("Last Point Line 2: ({}, {})".format(last_point2[0], last_point2[1]))
        else:
            print("No points found on Line 2.")

        # Create Matplotlib figure and plot
        fig = Figure(figsize=(5, 5), dpi=80)
        plot = fig.add_subplot(111)
        if first_point1[0] is not None:
            plot.plot([first_point1[0], last_point1[0]], [first_point1[1], last_point1[1]], color='r', linestyle='-', label=f'Line 1: {cox1}x + {coy1}y + {con1} = 0')
        if first_point2[0] is not None:
            plot.plot([first_point2[0], last_point2[0]], [first_point2[1], last_point2[1]], color='b', linestyle='-', label=f'Line 2: {cox2}x + {coy2}y + {con2} = 0')
        plot.grid(True)
        plot.set_title('Graph Plotter')
        plot.set_xlabel('X-axis')
        plot.set_ylabel('Y-axis')
        plot.legend()

        # Embed Matplotlib plot into Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, columnspan=2)

        # Add Matplotlib navigation toolbar
        toolbar_frame = Frame(window, bg='black')
        toolbar_frame.grid(row=10, column=0, columnspan=2)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()
        canvas.get_tk_widget().grid(row=9, column=0, columnspan=2)


if __name__ == '__main__':
    window = Tk()
    window.title("Graph Plotter")
    window.geometry('700x600')
    window.configure(bg='black')

    cox1_ = IntVar()
    cox2_ = IntVar()
    coy1_ = IntVar()
    coy2_ = IntVar()
    con1_ = IntVar()
    con2_ = IntVar()

    Label(window, text='Graph Plotter', font=('Arial', 30), bg='black', fg='white').grid(row=0, column=0, columnspan=2, pady=10, padx=220)

    Label(window, text='Enter the coefficient of x for Line 1:', bg='black', fg='white').grid(row=1, column=0, sticky=E)
    Entry(window, textvariable=cox1_).grid(row=1, column=1, sticky=W)

    Label(window, text='Enter the coefficient of y for Line 1:', bg='black', fg='white').grid(row=2, column=0, sticky=E)
    Entry(window, textvariable=coy1_).grid(row=2, column=1, sticky=W)

    Label(window, text='Enter the constant term for Line 1:', bg='black', fg='white').grid(row=3, column=0, sticky=E)
    Entry(window, textvariable=con1_).grid(row=3, column=1, sticky=W)

    Label(window, text='Enter the coefficient of x for Line 2:', bg='black', fg='white').grid(row=4, column=0, sticky=E)
    Entry(window, textvariable=cox2_).grid(row=4, column=1, sticky=W)

    Label(window, text='Enter the coefficient of y for Line 2:', bg='black', fg='white').grid(row=5, column=0, sticky=E)
    Entry(window, textvariable=coy2_).grid(row=5, column=1, sticky=W)

    Label(window, text='Enter the constant term for Line 2:', bg='black', fg='white').grid(row=6, column=0, sticky=E)
    Entry(window, textvariable=con2_).grid(row=6, column=1, sticky=W)

    Button(window, text="Plot Lines", command=Main.plot_lines, bg='white', fg='black').grid(row=7, column=0, columnspan=2, pady=10)

    window.mainloop()
