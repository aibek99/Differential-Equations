from bokeh.io import show
from bokeh.models import ColumnDataSource, CheckboxGroup, Panel, Tabs, Button, CustomJS, TextInput
from bokeh.plotting import figure, curdoc
from bokeh.layouts import layout, column
from ExactSolution import *
from EulerMethod import *
from ImprovedEulerMethod import *
from RungeKuttaMethod import *


init_x = 2
init_y = 1
init_X = 10
init_n0 = 1
init_N = 10

exact = ExactSolution(float(init_x), float(init_y), float(init_X), int(init_N))
euler = Euler(float(init_x), float(init_y), float(init_X), int(init_N))
improved_euler = ImprovedEuler(float(init_x), float(init_y), float(init_X), int(init_N))
runge_kutta = RungeKutta(float(init_x), float(init_y), float(init_X), int(init_N))

data = {'x_values': exact.array_x, 'y_exact': exact.array_y,
        'y_euler': euler.array_y, 'y_improved': improved_euler.array_y,
        'y_runge': runge_kutta.array_y}
init = {'init_x': [1], 'init_y': [1], 'init_X': [10], 'init_n0': [1], 'init_N': [10]}

source = ColumnDataSource(data=data)
initials = ColumnDataSource(data=init)

button = Button(label="Plot", button_type="success")
x0 = TextInput(title="x0 : ", value=str(init_x))
y0 = TextInput(title="y0 : ", value=str(init_y))
X = TextInput(title="X : ", value=str(init_X))
n0 = TextInput(title="n0 : ", value=str(init_n0))
N = TextInput(title="N : ", value=str(init_N))

def Click():
    exact = ExactSolution(initials.data['init_x'], initials.data['init_y'], initials.data['init_X'], initials.data['init_N'])
    euler = Euler(initials.data['init_x'], initials.data['init_y'], initials.data['init_X'], initials.data['init_N'])
    improved_euler = ImprovedEuler(initials.data['init_x'], initials.data['init_y'], initials.data['init_X'], initials.data['init_N'])
    runge_kutta = RungeKutta(initials.data['init_x'], initials.data['init_y'], initials.data['init_X'], initials.data['init_N'])

    print(exact.array_y)

    data = {'x_values': exact.array_x, 'y_exact': exact.array_y,
            'y_euler': euler.array_y, 'y_improved': improved_euler.array_y,
            'y_runge': runge_kutta.array_y}

    source.data = data

def fig4(title, dataset):
    p = figure(title=title, x_axis_label="x-axis", y_axis_label="y-axis")
    p.line('x_values', 'y_exact', source=dataset, legend_label="Exact Solution", line_color="blue", line_width=2)
    p.line('x_values', 'y_euler', source=dataset, legend_label="Euler Method", line_color="green", line_width=2)
    p.line('x_values', 'y_improved', source=dataset,
           legend_label="Improved Euler Method",
           line_color="yellow", line_width=2)
    p.line('x_values', 'y_runge', source=dataset, legend_label="Runge Kutta Method", line_color="red", line_width=2)
    return p


def fig3(title, dataset):
    d = figure(title=title, x_axis_label="x-axis", y_axis_label="y-axis")
    d.line('x_values', 'y_euler', source=dataset, legend_label="Euler Method", line_color="green", line_width=2)
    d.line('x_values', 'y_improved', source=dataset,
           legend_label="Improved Euler Method",
           line_color="yellow", line_width=2)
    d.line('x_values', 'y_runge', source=dataset, legend_label="Runge Kutta Method", line_color="red", line_width=2)
    return d


def update_x0(attr, old, new):
    initials.data['init_x'] = new


def update_y0(attr, old, new):
    initials.data['init_y'] = new


def update_xx(attr, old, new):
    initials.data['init_X'] = new


def update_n0(attr, old, new):
    initials.data['init_n0'] = new


def update_nn(attr, old, new):
    initials.data['init_N'] = new
    print(initials.data['init_x'] + " " + initials.data['init_y'] + " " + initials.data['init_X'] + " " + initials.data['init_n0'] + " " + initials.data['init_N'])


x0.on_change('value', update_x0) #init_x
y0.on_change('value', update_y0) #init_y
X.on_change('value', update_xx) #init_X
n0.on_change('value', update_n0) #init_n0
N.on_change('value', update_nn) #init_N

p1 = fig4("Exact Solution", source)
p2 = fig3("LTE", source)
p3 = fig3("GTE", source)

button.on_click(Click)

l1 = layout([[p1, p2, column(x0, y0, X, n0, N, button)]])
l2 = layout([[p3, column(x0, y0, X, n0, N, button)]])

tab1 = Panel(child=l1, title="Exact Solution and LTE")
tab2 = Panel(child=l2, title="GTE")

#curdoc().add_root(Tabs(tabs=[tab1, tab2]))

show(Tabs(tabs=[tab1, tab2]))
