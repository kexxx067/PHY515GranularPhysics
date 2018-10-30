import read_csv as rc
import potential as pe
import concatenate as concat

'''
file = rc.Load("Results.csv")
file.load()
testdata = file.get_Xt()
testcenter = []
for i in range(len(testdata)):
    testcenter.append([200,-200])
 p = pe.Potential(testdata, testcenter)
 p.system_potential_t()
 p.plot_potential()
'''

# Concatenate Xt1 and Xt2
file1 = rc.Load("Xt1.csv")
file1.load()
Xt1 = file1.get_Xt()
file2 = rc.Load("Xt2.csv")
file2.load()
Xt2 = file2.get_Xt()
file3 = rc.Load("Xt3.csv")
file3.load()
Xt3 = file3.get_Xt()
myconcat = concat.Concatenate([Xt1,Xt2,Xt3], 5)
myconcat.concat_all()
