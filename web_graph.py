import plotly.graph_objects as go
from plotly.subplots import make_subplots

figure = make_subplots(
    rows = 2,
    cols = 3,
    subplot_titles = ("Scatter", "Bar", "Pie", "Scatter", "Bar", "Empty"),
    specs = [
        [{"type" : "xy"}, {"type" : "xy"}, {"type" : "domain"}],
        [{"type" : "xy"}, {"type" : "xy"}, {"type" : "xy"}]
    ]
)

sdatax = [1234, 1927, 1987, 1821, 7212, 6363]
sdatay = [7348,7238, 1029, 1278,8373, 9327]
figure.add_trace(go.Scatter(x = sdatax, y = sdatay, mode = "lines+markers"), row = 1, col = 1)

bdatax = ["a", "b", "c", 'd', "e"]
bdatay = [1, 3, 2, 6, 3]

#bar_chart = go.Bar(bdatax, bdatay)
figure.add_trace(go.Bar(x = bdatax, y = bdatay), row = 1, col = 2)


pdatax = ["Bro", "Dude", "Sup", "Hello", "Hi"]
pdatay = [12, 15, 19, 13, 16]

pie_chart = go.Pie(labels = pdatax, values = pdatay)
figure.add_trace(pie_chart, row = 1, col = 3)


scdatax = [23, 45, 54, 13, 27, 35]
scdatay = [70, 78, 69, 82, 75, 68]

scatter_plot = go.Scatter(x = scdatax, y = scdatay)
figure.add_trace(scatter_plot, row = 2, col = 1)

b2datax = ["L", "M", "N", "O", "P"]
b2datay = [12, 13, 14, 15, 10]

bar_chart = go.Bar(x = b2datax, y = b2datay)
figure.add_trace(bar_chart, row = 2, col = 2)



figure.update_layout(title = "Multiple Subplot Example", width = 1000, height = 1000)
figure.write_html("MSE.html", auto_open = True)
