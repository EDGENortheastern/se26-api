import streamlit as st #creates web apps 
import requests #fetches API data 
import pandas as pd #processes data 
import plotly.express as px #creates interactive charts 

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson" 

with open("style.css") as f: #loads the css file
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🌍 Top 10 Earthquakes 🌋")

st.markdown("""
<div class="info">
⚡ <b>What is magnitude?</b> Magnitude measures how much energy an earthquake releases.
Each step up the scale is about 32 times more energy, so a 6.0 is far stronger than a 5.0.
</div>
<div class="warning">
⚠️ Quakes of 4.5 and above can be felt over a wide area, and 6.0 or more can cause serious damage.
</div>
""", unsafe_allow_html=True)

data = requests.get(url, timeout=20).json()

quake_data = pd.json_normalize(data["features"])
quake_data = quake_data.nlargest(10, "properties.mag")
colors = [ 

    "#f58552", "#e46225", "#d74b19", 

    "#fec54c", "#fdb737", "#e2a854", 

    "#62b6d0", "#2d7496", "#0d3353", 

    "#609f80", "#045944", "#1b4538" 

] 

 

fig = px.bar( 

    quake_data, 

    x="properties.mag", 

    y="properties.place", 

    orientation="h", 

    labels={ 

        "properties.mag": "Magnitude", 

        "properties.place": "Earthquake location" 

    } 

) 

  

fig.update_traces(marker_color=colors) 

fig.update_yaxes(autorange="reversed") 

st.plotly_chart(fig) 

 
