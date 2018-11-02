import numpy as np
import matplotlib.pyplot as plt

class Kinetic_energy:
    def __init__(self, Vt, ball_m):
        self.Vt = Vt
        self.KE = np.array([])
        self.ball_m = ball_m
        self.KE_tot = np.array([])
        self.KE_avg = np.array([])
        self.nframes = 0
        
    def get_kinetic_energy(self):
        self.KE = 0.5*self.ball_m*np.multiply(self.Vt,self.Vt)
        self.KE = self.KE.sum(axis = 1)
        self.KE_tot = self.KE.sum(axis = 0)

    # nstep is the number of frames you want to average on.
    def avg_kinetic_energy(self,nframes):
        self.nframes = nframes
        if len(self.KE_tot)%nframes != 0:
            self.KE_avg = self.KE_tot[:-(len(self.KE_tot)%nframes)].reshape(-1,nframes)
        else:
            self.KE_avg = self.KE_tot.reshape(-1,nframes)
        self.KE_avg = self.KE_avg.sum(axis = 1)/nframes
        return self.KE_avg
        
    def plot(self):
        # Still plotting KE in correct frames.
        time = np.arange(len(self.KE_avg))*self.nframes
        plt.scatter(time, self.KE_avg, marker = ".")
        plt.show()
