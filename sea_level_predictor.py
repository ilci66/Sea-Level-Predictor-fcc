import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  x = df["Year"]
  y = df["CSIRO Adjusted Sea Level"]

  # print(df)
    # Create scatter plot
  # plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
  # this one's for the legend
  fig, ax = plt.subplots() 
  plt.scatter(x, y)
  
    # Create first line of best fit
  res = linregress(x,y)
  # print(res)

  x_pre = pd.Series([i for i in range(1880, 2051)])
  # print(x_pre)
  # print(res.slope * x_pre)
  y_pre = res.slope * x_pre + res.intercept
  plt.plot(x_pre, y_pre, "r")

    # Create second line of best fit
  new_df = df.loc[df["Year"] >= 2000]
  new_x = new_df["Year"]
  new_y = new_df["CSIRO Adjusted Sea Level"]
  res_new = linregress(new_x, new_y)
  x_pre_new = pd.Series([i for i in range(2000, 2051)])
  y_pre_new = res_new.slope*x_pre_new + res_new.intercept
  plt.plot(x_pre_new, y_pre_new) 

    # Add labels and title
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
  ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()