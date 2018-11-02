import read_csv as rc
import potential as pe
import concatenate as concat
import velocity as v
import kinetic_energy as ke
import matplotlib.pyplot as plt
import numpy as np

'''
file = rc.Reader("Results.csv")
testdata = file.read_raw_csv()
testcenter = []
for i in range(len(testdata)):
    testcenter.append([200,-200])
p = pe.Potential(testdata, testcenter)
p.system_potential_t()
p.plot_potential()
'''

# Concatenate Xt1 and Xt2
file1 = rc.Reader("Xt1.csv")
Xt1 = file1.read_raw_csv()
file2 = rc.Reader("Xt2.csv")
Xt2 = file2.read_raw_csv()
file3 = rc.Reader("Xt3.csv")
Xt3 = file3.read_raw_csv()
myconcat = concat.Concatenate([Xt1,Xt2,Xt3], 5)
myconcat.concat_all()

# Read Xt csv
#file_Xt = rc.Reader("concatenate.csv")
#XtV = file_Xt.read_Xt_csv()

file_Xt1 = rc.Reader("1-25000.csv")
XtV1 = file_Xt1.read_raw_csv()

file_Xt2 = rc.Reader("25001-50000.csv")
XtV2 = file_Xt2.read_raw_csv()

file_Xt3 = rc.Reader("50001-100000.csv")
XtV3 = file_Xt3.read_raw_csv()

file_Xt4 = rc.Reader("100001-143920.csv")
XtV4 = file_Xt4.read_raw_csv()

myv1 = v.Velocity(XtV1, 1, 1./209.78)
Vt1 = myv1.get_velocity()

myv2 = v.Velocity(XtV2, 1, 1./209.78)
Vt2 = myv2.get_velocity()

myv3 = v.Velocity(XtV3, 1, 1./209.78)
Vt3 = myv3.get_velocity()

myv4 = v.Velocity(XtV4, 1, 1./209.78)
Vt4 = myv4.get_velocity()

myke1 = ke.Kinetic_energy(Vt1, 1)
myke1.get_kinetic_energy()

myke2 = ke.Kinetic_energy(Vt2, 1)
myke2.get_kinetic_energy()

myke3 = ke.Kinetic_energy(Vt3, 1)
myke3.get_kinetic_energy()

myke4 = ke.Kinetic_energy(Vt4, 1)
myke4.get_kinetic_energy()

avg_len = 100

ke1 = myke1.avg_kinetic_energy(avg_len)
ke2 = myke2.avg_kinetic_energy(avg_len)
ke3 = myke3.avg_kinetic_energy(avg_len)
ke4 = myke4.avg_kinetic_energy(avg_len)

kef = np.concatenate([ke1, ke2, ke3, ke4])
time = np.arange(len(kef))*avg_len
plt.scatter(time, kef, marker = ".")
plt.show()
