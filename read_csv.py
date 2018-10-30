import csv
class Load:
    def __init__(self, filename):
        self.filename = filename
        self.Xt = []

    def load(self):
        trajectory = [] # Store the 1st column in csv file
        frame = [] # Store the 2nd column in csv file
        x = [] # Store the 3rd column in csv file
        y = [] # Store 4th column in csv file
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    trajectory.append(int(row[0]))
                    frame.append(int(row[1]))
                    x.append(float(row[3])) # Reverse because of Image J output format
                    y.append(-float(row[2])) # Same reason as above
                    line_count += 1
        # Determine number of balls
        nballs = trajectory[len(trajectory) - 1]
        # Determine total time length
        time_len = int(len(trajectory)/nballs)
        # Xt
        for t in range(time_len):
            temp_lst = []
            for ball in range(nballs):
                temp_lst.append([x[t + ball*time_len], y[t + ball*time_len]])
            self.Xt.append(temp_lst)
            
    # Return balls' coordinate
    def get_Xt(self):
        return self.Xt
