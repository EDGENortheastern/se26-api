# ⛰︎ se26-api: Top 10 Earthquakes ϟ ϟ

A Streamlit web app that shows the 10 strongest earthquakes (magnitude 4.5+) recorded around the world in the past 7 days, using live data from the USGS earthquake API.

---

## ᨒ User documentation

### Hover for details
Move your mouse over any bar in the chart to see the earthquake's location and exact magnitude.

### Refresh for new data
Refresh the page (`Cmd + R` on Mac, `Ctrl + R` or `F5` on Windows) to load the latest earthquakes.

---

## ⚙︎ Technical documentation

### Requirements
- Python 3.9 or newer
- The libraries listed in [requirements.txt](requirements.txt): `streamlit`, `requests`, `pandas`, `plotly`

### 1. Create a virtual environment
A virtual environment keeps this project's libraries separate from the rest of your computer. Run this in the project folder:

```bash
python3 -m venv .venv
```

### 2. Activate the virtual environment
Mac / Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

When it's active, you'll see `(.venv)` at the start of your terminal line.

### 3. Install the requirements
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app opens in your browser at http://localhost:8501. To stop it, press `Ctrl + C` in the terminal.

### 5. Deactivate the virtual environment
When you're finished:
```bash
deactivate
```

### How it works
1. `requests` fetches earthquake data from the [USGS GeoJSON feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson).
2. `pandas` turns the data into a table and picks the 10 largest magnitudes.
3. `plotly` draws the bar chart.
4. `streamlit` displays everything as a web page.

### ⚠︎ Useful links
- [Requests documentation](https://requests.readthedocs.io/en/latest/)
- [Streamlit documentation](https://docs.streamlit.io/)
- [USGS earthquake feeds](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
