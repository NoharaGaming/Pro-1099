import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("Project.csv")
list= df["math score"].to_list()
fig = ff.create_distplot([list],["Math Score"])
fig.show()
mean = statistics.mean(list)
print(mean)
mode = statistics.mode(list)
print(mode)
median = statistics.median(list)
print(median)
print("mean",statistics.mean(list))
print("mode",statistics.mode(list))
print("median",statistics.median(list))
std = statistics.stdev(list)
print(std)
print(mean-std)
print(mean+std)
print("second standard deviation")
print(mean-(2*std))
print(mean+(2*std))
print("third standarad diviation")
print(mean-(3*std))
print(mean+(2*std))