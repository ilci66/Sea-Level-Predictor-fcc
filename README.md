# Sea Level Predictor - freeCodeCamp Challange

### Assignment

You will anaylize a dataset of the global average sea level change since 1880. You will use<br> the data to predict the sea level change through year <br> 2050.

Use the data to complete the following tasks:
* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO <br>
Adjusted Sea Level" column as the y-axix.
* Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line<br> 
of best fit.Plot the line of best fit over the top of the scatter plot. Make the line go through <br> 
the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in <br>
 the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if<br>
  the rate of rise continues asit has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)",and the title should be<br>
 "Rise in Sea Level".

Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the <br> "run" button and `main.py` will run.

### Testing 

Imported the tests from `test_module.py` to `main.py` for your convenience. <br>The tests will run automatically whenever you hit the "run" button.


### Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US  Environmental <br>Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise


### Challanges and Improvements
1.  Using pandas with matplotlib was a fun experience and it felt a lot easier to interact with than d3.js

