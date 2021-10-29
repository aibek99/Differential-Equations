from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import CheckboxGroup
from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns = ['a', 'b', 'c', 'd'])
source = ColumnDataSource(df)


def checkbox_click_handler(selected_checkboxes):
    visible_glyphs = lay.children
    for index, glyph in enumerate(glyph_list):
        print(index)
        print(glyph)
        if index in selected_checkboxes:
            if glyph not in visible_glyphs:
                lay.children.append(glyph)
        else:
            if glyph in visible_glyphs:
                lay.children.remove(glyph)


checkbox_group = CheckboxGroup(labels=list(df.columns.values), active=[0, 1, 2, 3])
checkbox_group.on_click(checkbox_click_handler)

print(checkbox_group.labels)

lay = column()
lay.children.append(checkbox_group)

glyph_list = []
for index, letter in enumerate(df.columns.values):
    glyph = figure(plot_width = 800, plot_height = 240, title = letter, name = letter)
    glyph.circle(source = source, x = 'a', y = letter)
    glyph_list.append(glyph)
    lay.children.append(glyph)

curdoc().add_root(lay)
