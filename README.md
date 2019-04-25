# Advanced-Data-Storage-Retrieval-SQLAlchemy-ORM

This program was written by Radha Mahalingam on 4-20-19

This project analyses the climate of Honolulu, Hawaii, where I plan to go on a long holiday vacation.  Using Python and SQLAlchemy, I did basic climate analysis and data exploration using the climate database. Using SQLAlchemy ORM queries, Pandas, Matplotlib and Jupyter notebook.

## Step 1 - Climate Analysis and Exploration

* Used the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to do the climate analysis and data exploration.

* Chosen a start date and end date of my trip i.e. 2017-06-01','2017-06-15'

* Used SQLAlchemy `create_engine` to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect my tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis process

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Ploted the results using the DataFrame `plot` method and saved it as a .png file in the Images directory (precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

* Designed a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filtered by the station with the highest number of observations.

  * Ploted the results as a histogram with `bins=12` and and saved it as a .png file in the Images directory (station_histogram.png)

## Step 2 - Climate App

After completing the above initial analysis, designed a Flask API based on the queries that I have developed.

### Optional: Other Recommended Analyses

* In addition, designed the following additional challenge queries. 

### Daily Rainfall Average.

* Calculated the rainfall per weather station using the previous year's matching dates.

* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

* With the function provided called `daily_normals` that will calculate the daily normals for a specific date.   Created a list of dates for your trip in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date. Used Pandas to plot an area plot (`stacked=False`) for the daily normals. Saved in the Image folder.