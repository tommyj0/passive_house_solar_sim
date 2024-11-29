import pandas as pd
import matplotlib.pyplot as plt


tmy = pd.read_csv("pvlib_tutorial/kinghorn_tmy.csv", skiprows=16, nrows=8760, 
                  usecols=["time(UTC)", "T2m", "G(h)", "Gb(n)", "Gd(h)", "WS10m"],
                  index_col=0)
# tmy.index = pd.to_datetime(tmy.index, format="%Y%m%d:%H%M")
tmy.index = pd.date_range(start="2022-01-01-00:00", end="2022-12-31-23:00", freq="h")
print(tmy)

tmy.columns = ["temp_air", "ghi", "dni", "dhi", "wind_speed"]

tmy.plot()
tmy.to_csv("pvlib_tutorial/pvlib_kinghorn.csv")
plt.show()