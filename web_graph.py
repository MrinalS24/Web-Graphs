import plotly.graph_objects as go
from plotly.subplots import make_subplots

figure = make_subplots(
    rows = 3,
    cols = 2,
    subplot_titles = ("Scatter", "Bar", "Pie", "Scatter", "Bar", "Empty"),
    specs = [
        [{"type" : "xy"}, {"type" : "xy"}, {"type" : "xy"}],
        [{"type" : "xy"}, {"type" : "xy"}, {"type" : "xy"}]
    ]
)

datax = [1234, 1927, 1987, 1821, 7212, 6363]
datay = [7348,7238, 1029, 1278,8373, 9327]
figure.add_trace(go.Scatter(x = datax, y = datay, mode = "lines+markers"), row = 1, col = 1)





figure.update_layout(title = "Multiple Subplot Example", width = 1000, height = 1000)
figure.write_html("MSE.html", auto_open = True)