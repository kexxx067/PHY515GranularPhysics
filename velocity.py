import numpy as np
class Velocity:
    def __init__(self, Xt, pixel_scale, t_step):
        self.t_step = t_step
        self.Xt = pixel_scale*Xt
        self.nballs = len(Xt[0])
        self.time_len = len(Xt)
        self.pixel_width = 1
        # VXt has the same information as Xt but in different shape
        # VXt is in shape of (self.nballs, 2(x or y), self.time_len)
        self.VXt = self.Xt.reshape((self.time_len, self.nballs*2))
        self.VXt = self.VXt.T.reshape((self.nballs, 2, self.time_len))
        self.Vt = np.zeros((self.nballs, 2, self.time_len-1))
        
    def get_velocity(self):
        for ball in range(self.nballs):
            for axis in range(2):
                for t in range(self.time_len-1):
                    self.Vt[ball][axis][t] = \
                    (self.VXt[ball][axis][t+1] - self.VXt[ball][axis][t])/self.t_step
        return self.Vt
