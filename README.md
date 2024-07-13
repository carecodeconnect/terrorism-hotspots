# Terrorism Hotspots

Interactive data visualisation app mapping and visualising terrorist incidents from the [Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/).

[terrorism-hotspots.webm](https://github.com/user-attachments/assets/22cf7f97-cc3a-48ed-8301-18df3c3fffac)

## Data

The GTD is an open-source database including information on terrorist attacks around the world from 1970 through 2017. It includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 180,000 attacks. 

## Tools

The app was built using:

* [PyGWalker](https://github.com/Kanaries/pygwalker) Python library, which allows you to explore a pandas `DataFrame` 
with interactive Tableau-style data visualisations.

* [Streamlit](https://streamlit.io/) to build the web data app.

* [Python](https://www.python.org/) version 3.10.

## Usage

To use the app, click [here](https://terrorism-hotspots.streamlit.app/).

To select a dashboard, click **Visualization**, then select the dashboard you want: a **Map** of terrorism incidents, **Year vs Region (Bar Plot)**, or **Year vs Region (Faceted)** showing incidents by year.

To customise the plots yourself, you can drag and drop fields and measurements from the left-hand columns to explore the dataset, or click **+ New** to create your own dashboard.

## Development

To develop with this project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/carecodeconnect/terrorism-hotspots
   ```

2. Navigate to the project directory:

   ```
   cd terrorism-hotspots
   ```

3. Setup your environment and required dependencies:

   ```
   conda create -n terrorism-hotspots python=3.10
   pip install -r requirements.txt
   ```

4. Run the Streamlit app locally:

   ```
   streamlit run terrorism-hotspots.py
   ```

## Project Structure

Below is the tree structure of the project for quick reference:

```
├── data/                   # Folder containing data file
├── LICENCE                 # MIT licence
├── README.md               # Project overview and setup instructions
├── requirements.txt        # List of dependencies to install
└── terrorism-hotspots.py   # Main Streamlit application script
```
