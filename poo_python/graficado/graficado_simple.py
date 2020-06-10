from bokeh.plotting import figure, output_file, show
import random


if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    type(fig)

    total_vals = int(input('Cuantos valores quieres graficar? '))

    x_vals = list(range(total_vals))
    y_vals = [random.randint(0, 100) for i in range(total_vals)]

#    for x in x_vals:
#        val = int(input(f'Valor y para {x}: '))
#        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
