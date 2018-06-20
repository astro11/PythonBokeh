import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
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
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# This is drawing the edges from start to end
# TODO: Change how this works
graph.edge_renderer.data_source.data = dict(
    start=[0]*N, # This is a list that has something to do with starting points | Why does it work?
    end=node_indices) # This is a list that has something to do with ending points | Why does it work?

### start of layout code
# this is setting the positions of the vertexes
# circ = [i*2*math.pi/N for i in node_indices] #divided circumference by node count

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]


graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)