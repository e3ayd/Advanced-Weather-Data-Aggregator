# Advanced Weather Data Aggregator

This project is a Python-based weather data aggregator that fetches and combines weather data from multiple APIs (OpenWeatherMap and Weatherbit) to provide a comprehensive weather report. The project demonstrates advanced API usage, data aggregation, and handling multiple sources of information.

## Features

- Fetches weather data from OpenWeatherMap and Weatherbit APIs.
- Aggregates temperature and humidity data from both sources.
- Provides detailed weather descriptions from both APIs.

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries using pip:

```bash
pip install requests
```

## Usage

```To run the project, use the following command:

python weather_aggregator.py
```

After running the script, you'll be prompted to enter a city name. If you press Enter without typing anything, it will use the default city (London). The script will then fetch data from multiple APIs, aggregate the information, and display a comprehensive weather report.

## Example Output

```Here's what the output might look like:

Enter city name (default is London): New York
Weather report for New York:
Temperature: 21.5°C
Humidity: 55%
OpenWeatherMap description: scattered clouds
Weatherbit description: broken clouds
```

## Explanation

- Multiple APIs: This project uses data from two different weather APIs to provide more reliable and aggregated information.
- Data Aggregation: It combines data from both sources to give a better average for temperature and humidity.
- API Handling: Demonstrates how to work with different APIs, handle API keys, and manage JSON responses.

## Contribution

To contribute, please submit a pull request. We welcome all suggestions and improvements!



