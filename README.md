☀️ Weather Analysis and Visualisation Application (Weather Analyzer)
This project is an interactive application written in Python that retrieves real-time weather data and multi-day forecasts 
from an external API. It then processes this data using the Pandas library and visualises temperature trends using Matplotlib.

Features 🚀
-> Data Retrieval: Connects to the OpenWeatherMap API (API key required).
-> Dynamic Input: Allows the user to check the weather for any city.
-> Data Analysis: Uses the Pandas library to structure raw JSON data.
-> Visualisation: Generates graphs using Matplotlib (e.g. 5-day linear trend forecast).
-> Archiving: Saves forecast data to a CSV file.
-> Error Handling: Correctly informs the user in case of a connection error or if the city cannot be found.

Requirements and Installation ⚙️
To run this project, you need Python 3 installed and the following libraries:

Clone the repository:
Bash:
-> git clone [your repository link]

Create and activate a virtual environment (RECOMMENDED):
Bash:
-> python -m venv venv
-> source venv/bin/activate  # macOS/Linux
-> venv\Scripts\activate     # Windows

Install the required packages:
Bash:
-> pip install requests pandas matplotlib

API Key Configuration 🔑
The project requires an API key from OpenWeatherMap.
1. Register on OpenWeatherMap and generate an API key.
2. In the pogoda.py file, find the API_KEY variable and replace the text YOUR_API_KEY with your unique key.
   -> API_KEY = "YOUR_API_KEY"

How to Use ▶️
Run the script directly in the terminal
Bash: 
-> python pogoda.py
The application will ask you to enter the name of the city for which you want to check the forecast.

Project Structure
-> pogoda.py: The main application file, containing all the logic for downloading, processing, and visualising data.
-> pogoda_[city_name].csv: An automatically generated file containing historical data.
