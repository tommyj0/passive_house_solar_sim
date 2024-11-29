import numpy
import pvlib
import matplotlib.pyplot as plt
from pvlib.modelchain import ModelChain
from pvlib.location import Location
from pvlib.pvsystem import PVSystem
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
import pandas as pd

location = Location(latitude=56.074 , longitude=-3.189, tz = 'Europe/London', altitude=0, name="Passive House")

sandia_modules = pvlib.pvsystem.retrieve_sam('sandiamod')
cec_inverters = pvlib.pvsystem.retrieve_sam('CECInverter')
module = sandia_modules['Canadian_Solar_CS6X_300M__2013_']
inverter = cec_inverters['ABB__PVI_3_0_OUTD_S_US__208V_']

temp_params  = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

system = PVSystem(surface_tilt=20,surface_azimuth=180, module_parameters=module, inverter_parameters=inverter, temperature_model_parameters=temp_params, modules_per_string= 6, strings_per_inverter=2)
modelchain = ModelChain(system, location)

# times = pd.date_range(start="2021-07-01", end="2021-07-07", freq='1min', tz=location.tz)
# clear_sky = location.get_clearsky(times)
# clear_sky.plot()
# plt.show()
tmy = pd.read_csv("pvlib_tutorial/pvlib_kinghorn.csv", index_col=0)
tmy.index = pd.to_datetime(tmy.index)

modelchain.run_model(tmy)

# modelchain.results.ac.plot()
# plt.show()
(modelchain.results.ac.resample("M").sum()/1e3).plot()
plt.title("Monthly PV Generation")
plt.ylabel("Generation (kWh)")

plt.grid(True,color = 'green', linestyle = '--', linewidth = 0.5)
plt.savefig("pvlib_tutorial/PV_gen.svg", format="svg")
plt.show()
(modelchain.results.ac.resample("M").sum()/1e3).to_csv("pvlib_tutorial/results.csv")