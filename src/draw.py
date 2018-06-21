import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Range1d, LabelSet, Label

from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

# debug_palette = Spectral8
# debug_palette += ('#ff0000', '#0080ff') #debug_palette.append('#ff0000')


plot = figure(title='PythonBokeh Graph Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=25, fill_color='color') #radius also works / **kwargs

# This is drawing the edges from start to end
start_indexes = []
end_indexes = []

for start_index, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        end_indexes.append(graph_data.vertexes.index(e.destination))

# TODO: Change how this works
graph.edge_renderer.data_source.data = dict(
    start=start_indexes, # This is a list of vertex indexes to start edges from
    end=end_indexes) # This is a list of vertex indexes to start edges at

### start of layout code
# this is setting the positions of the vertexes
# circ = [i*2*math.pi/N for i in node_indices] #divided circumference by node count

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

#creating dictionary using dict()
graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

#create a new dict to use as a data source, with three lists in it, ordrered in the same way as vertexes
# list of x values
# list of y values
# list of labels
value = [v.value for v in graph_data.vertexes]
label_source = ColumnDataSource(data=dict(x=x, y=y, v=value))

labels = LabelSet(x='x', y='y', text='v', level='glyph',
              source=label_source, text_align='center', text_baseline='middle', render_mode='canvas')

plot.add_layout(labels)

output_file('graph.html')
show(plot)