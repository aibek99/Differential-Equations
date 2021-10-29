from bokeh.models import ColumnDataSource, Panel, Tabs, Button, TextInput, CheckboxGroup
from bokeh.plotting import figure, curdoc
from bokeh.layouts import layout, column, row
from ExactSolution import *
from Dependencies import *


init_x = 2.0
init_y = 1.0
init_X = 10
init_n0 = 1
init_N = 10
source = ColumnDataSource()
depend = ColumnDataSource()

button_size = int(285)

x0 = TextInput(title="x0 : ", value="2", width=button_size)
y0 = TextInput(title="y0 : ", value="1", width=button_size)
X = TextInput(title="X : ", value="10" , width=button_size)
n0 = TextInput(title="n0 : ", value="1", width=button_size)
N = TextInput(title="N : ", value="10", width=button_size)
button = Button(label="Plot", button_type="success", width=button_size)
list_methods = ['Exact Solution', 'Euler Method', 'Improved Euler Method', 'Runge Kutta Method']


def update_x0(attr, old, new):
    global init_x
    init_x = float(x0.value)


def update_y0(attr, old, new):
    global init_y
    init_y = float(y0.value)


def update_xx(attr, old, new):
    global init_X
    init_X = float(X.value)


def update_n0(attr, old, new):
    global init_n0
    init_n0 = int(n0.value)


def update_nn(attr, old, new):
    global init_N
    init_N = int(N.value)


def update():
    global init_x, init_y, init_X, init_n0, init_N
    exact = ExactSolution(init_x, init_y, init_X, init_N)
    euler = Euler(init_x, init_y, init_X, init_N)
    improved_euler = ImprovedEuler(init_x, init_y, init_X, init_N)
    runge_kutta = RungeKutta(init_x, init_y, init_X, init_N)
    dependency = Dependencies(init_x, init_y, init_X, init_N, init_n0)

    _data = {'x_values': exact.array_x, 'y_exact': exact.array_y, 'y_euler': euler.array_y,
             'y_improved': improved_euler.array_y, 'y_runge': runge_kutta.array_y,
             'y_euler_lte': euler.lte, 'y_euler_gte': euler.gte,
             'y_improved_lte': improved_euler.lte, 'y_improved_gte': improved_euler.gte,
             'y_runge_lte': runge_kutta.lte, 'y_runge_gte': runge_kutta.gte}

    d = {'x_values': dependency.len, 'y_legte': dependency.legte, 'y_ligte': dependency.ligte, 'y_lrgte': dependency.lrgte,
         'y_lelte': dependency.lelte,  'y_lilte': dependency.lilte, 'y_lrlte': dependency.lrlte}

    source.data = _data
    depend.data = d


update()

p1 = figure(title="Exact Solution", x_axis_label="x-axis", y_axis_label="y-axis", width=500, height=300)
p1.line('x_values', 'y_exact', source=source, legend_label="Exact Solution", line_color="blue", line_width=2)
p1.line('x_values', 'y_euler', source=source, legend_label="Euler Method", line_color="green", line_width=2)
p1.line('x_values', 'y_improved', source=source, legend_label="Improved Euler Method", line_color="yellow", line_width=2)
p1.line('x_values', 'y_runge', source=source, legend_label="Runge Kutta Method", line_color="red", line_width=2)
p1.legend.click_policy = "hide"


def fig3(title, i: int, res):
    yyy = ['y_euler', 'y_improved', 'y_runge', 'y_euler_lte', 'y_improved_lte', 'y_runge_lte', 'y_euler_gte',
           'y_improved_gte', 'y_runge_gte', 'y_legte', 'y_ligte', 'y_lrgte', 'y_lelte', 'y_lilte', 'y_lrlte',
           'y_legte', 'y_ligte', 'y_lrgte', 'y_lelte', 'y_lilte', 'y_lrlte']
    p = figure(title=title, x_axis_label="x-axis", y_axis_label="y-axis", width=500, height=300)
    p.line("x_values", yyy[i * 3 - 3], source=res, legend_label="Euler Method", line_color="green", line_width=2)
    p.line("x_values", yyy[i * 3 - 2], source=res, legend_label="Improved Euler Method", line_color="yellow", line_width=2)
    p.line("x_values", yyy[i * 3 - 1], source=res, legend_label="Runge Kutta Method", line_color="red", line_width=2)
    p.legend.click_policy = "hide"
    return p


p2 = fig3("LTE", 2, source)
p3 = fig3("GTE", 3, source)
p4 = fig3("LTE Dependency", 5, depend)
p5 = fig3("GTE Dependency", 4, depend)
glyph_list = [p1, p2, p3, p4, p5]

x0.on_change('value', update_x0)
y0.on_change('value', update_y0)
X.on_change('value', update_xx)
n0.on_change('value', update_n0)
N.on_change('value', update_nn)
button.on_click(update)

l1 = layout([[column(row(p1, p2, p3), row(x0, y0, X, N, button))]])
l2 = layout([[column(row(p4, p5), column(n0, N, button))]])

tab1 = Panel(child=l1, title="Exact Solution, LTE, GTE")
tab2 = Panel(child=l2, title="LTE, GTE Dependency")

curdoc().add_root(Tabs(tabs=[tab1, tab2]))
