import matplotlib.pyplot as plt
from astropy.utils import iers

table = iers.IERS_Auto.open() # table containing all parameters
px = table['PM_x']
py = table['PM_y']
mjd = table['MJD']
tcorr = table['UT1_UTC_A']

plt.figure(figsize=(9,4))
plt.subplot(1,2,1)
plt.plot(px, py)
plt.xlabel("polar motion X ({})".format(px.unit.to_string('latex')))
plt.ylabel("polar motion Y ({})".format(py.unit.to_string('latex')))

plt.subplot(1,2,2)
plt.plot(mjd, tcorr)
plt.xlabel("MJD")
plt.ylabel("UT to UTC time correction")
plt.tight_layout()