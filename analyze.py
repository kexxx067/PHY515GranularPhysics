import read_csv as rc
import potential as pe
import concatenate as concat

'''
file = rc.Reader("Results.csv")
file.read_raw_csv()
testdata = file.get_Xt()
testcenter = []
for i in range(len(testdata)):
    testcenter.append([200,-200])
p = pe.Potential(testdata, testcenter)
p.system_potential_t()
p.plot_potential()
'''

# Concatenate Xt1 and Xt2
file1 = rc.Reader("Xt1.csv")
file1.read_raw_csv()
Xt1 = file1.get_Xt()
file2 = rc.Reader("Xt2.csv")
file2.read_raw_csv()
Xt2 = file2.get_Xt()
file3 = rc.Reader("Xt3.csv")
file3.read_raw_csv()
Xt3 = file3.get_Xt()
myconcat = concat.Concatenate([Xt1,Xt2,Xt3], 5)
myconcat.concat_all()

# Read Xt csv
file_Xt = rc.Reader("concatenate.csv")
file_Xt.read_Xt_csv()
