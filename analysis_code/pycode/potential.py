import matplotlib.pyplot as plt
import math
# Calculate potential and make a plot
class Potential:
    # Xt is in the form of[[ball_1_postion_t,ball_2_position_t],[ball_1_postion_t+1,ball_2_position_t+1]] 
    def __init__(self, Xt, ring_center_t):
        self.Xt = Xt
        self.time_len = len(Xt)
        self.ring_center_t = ring_center_t
        self.nballs = len(Xt[0])
        self.potential_time_series = []
        self.time = []
        for t in range(self.time_len):
            self.time.append(t)

    # Calculate distance between 2 points
    def two_point_distance(self, x1, x2):
        square_sum = 0
        for i in range(len(x1)):
            square_sum += (x1[i] - x2[i])**2
        r = math.sqrt(square_sum)
        return r

    # Calculate potential energy between 2 ball
    def two_ball_potential(self, ball1, ball2, t):
        r = self.two_point_distance(self.Xt[t][ball1], self.Xt[t][ball2])
        ball_PE = 1./r**4
        return ball_PE

    # Calculate potential energy between ring and ball
    def ball_in_ring_potential(self, ball, t):
        r = self.two_point_distance(self.Xt[t][ball], self.ring_center_t[t])
        ring_PE = r**2
        return ring_PE

    def ball_balls_total_potential(self, ball, t):
        total_potential = 0
        for other_ball in range(self.nballs):
            if ball == other_ball:
                continue
            else:
                total_potential += self.two_ball_potential(other_ball, ball, t)
        return total_potential

    # Calculate potential of whole system at time step t
    def system_potential(self, t):
        total_potential = 0
        for ball in range(self.nballs):
            total_potential += self.ball_balls_total_potential(ball, t)
        total_potential /= 2. # Get rid of double counting
        for ball in range(self.nballs):
            total_potential += self.ball_in_ring_potential(ball,t)
        return total_potential

    # Calculate potential of whole system across all time
    def system_potential_t(self):
        self.potential_time_series = []
        for t in range(self.time_len):
            self.potential_time_series.append(self.system_potential(t))

    # Plot potential energy of system vs. time
    def plot_potential(self):
        if len(self.potential_time_series) < 1:
            print("Haven't calculate potential_time_series yet")
            return
        else:
            plt.scatter(self.time, self.potential_time_series)
            plt.show()
            print("Done plotting")
