import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import plotly.express as px
import plotly.graph_objects as go



# Two alternatives for retrieving dataset:

# ALTERNATIVE 1 - ONLINE URL
# data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")


# ALTERNATIVE 2 - LOCAL CSV FILE
data = pd.read_csv("dataset/advertising.csv")

print("DATA RELATIONS:")
print(data.head())


# Check if the data in the csv has any null values
# print(data.isnull().sum())



def exportStaticOutput(figure, path):
    figure.write_html(f"output-current/html/{path}.html")
    figure.write_image(f"output-current/png/{path}.png")


##  GRAPH 1 - Visualize the relationship between the amount spent on advertising on TV and units sold  ##
def createGraph1():
    figure = px.scatter(data_frame = data, x="Sales",
                        y="TV", size="TV", trendline="ols")
    figure.show()
    exportStaticOutput(figure, "1-advertise-tv-units-sold")


def createGraph2():
    figure = px.scatter(data_frame = data, x="Sales",
                        y="Newspaper", size="Newspaper", trendline="ols")
    figure.show()

    exportStaticOutput(figure, "2-advertise-newspapers-units-sold")


def createGraph3():
    figure = px.scatter(data_frame = data, x="Sales",
                        y="Radio", size="Radio", trendline="ols")
    figure.show()

    exportStaticOutput(figure, "3-advertise-radio-units-sold")



###   GENERATE GRAPHS & OUTPUTS   ###

createGraph1()
createGraph2()
createGraph3()



# Out of all the amount spent on advertising on various platforms, I can see that the amount spent
# on advertising the product on TV results in more sales of the product. Now let’s have a look at the
# correlation of all the columns with the sales column:

correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False))