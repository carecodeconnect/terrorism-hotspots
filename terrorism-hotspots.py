import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

# Set width of Streamlit app
st.set_page_config(
    page_title="Mapping Terrorism Hotspots",
    layout="wide"
)

# Add title
st.title("Mapping Terrorism Hotspots")

# Subtitle/Description
st.write(
    """
    This app maps terrorist incidents from the [Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/) - an open-source database including information on terrorist attacks around the world from 1970 through 2017.
    
    The GTD includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 180,000 attacks. 
    
    This Streamlit app uses the free and open source [PyGWalker](https://github.com/Kanaries/pygwalker) Python library, which allows you to explore a pandas `DataFrame` 
    with interactive Tableau-style data visualisations.

    To select a dashboard, click **Visualization**, then select the dashboard you want: a **Map** of terrorism incidents, or a **Time** bar chart showing incidents by year.

    To customise the plots yourself, you can drag and drop fields and measurements from the left-hand columns to explore the dataset, or click **+ New** to create your own dashboard.

    """
)

# Cache pygwalker renderer
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    # Import data from compressed CSV file
    df = pd.read_csv("./data/globalterrorismdb_0718dist.tar.bz2", compression="bz2")
    # Load pygwalker configuration
    return StreamlitRenderer(df, spec="./pygwalker_spec.json", spec_io_mode="rw")

renderer = get_pyg_renderer()
renderer.explorer()

# Visualise with PygWalker with duckdb
#pyg.walk(df, kernel_computation=True)