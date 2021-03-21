# SQL-Alchemy-Challenge

I use the provided starter notebook and hawaii.sqlite files to do Hawaii climate analysis and data exploration. I use use Python and SQLAlchemy for the analysis and data exploration purpose. 

## Precipitation Analysis
- I retrieve the data from the last 12 months using Pandas and plot the date and precipitation on a graph. From this data I was able to produce the graph below that shows Precipitation in Hawaii from 08/23/2016- 08/23/2017.
![precipitation](Images/precipitation.png)

## Station Analysis
- I design a query to calculate the total number of stations, the most active stations, and the last 12 months of temperature observation data (TOBS) from the most active station.
![station-histogram](Images/temperature_vs_frequency.png)


## Climate App
- As part of the project, I also created a Flask API based on the queries that I developed from the climate and precipitation analysis
Here are the routes on my flask: 

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * This route queries the dates and temperature observations of the most active station for the last year of data. It will return the data in JSON list.


* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * This route will return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


