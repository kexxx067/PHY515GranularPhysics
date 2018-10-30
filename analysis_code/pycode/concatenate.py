import csv
import numpy as np

class Concatenate:
    # Parameter:
    # 1. overlap: number of rows overlapped between 2 Xt.
    #             need to be the same for all Xt in Xt_lst
    # 2. Xt_lst: a list of Xt that will be concatenated
    #            need to be in order of Xt1, Xt2...
    #            Xt_lst[Xt_i][time][ball][ball_x/y]
    def __init__(self, Xt_lst, overlap):
        self.overlap_rows = overlap
        # list of projection dict [{i:j, ..},{},...] track i in previous Xt
        # correspond to track j in next Xt
        self.projection = []
        self.Xt_lst = Xt_lst
        self.nballs = len(Xt_lst[0][0])
        self.nXt = len(Xt_lst) # Number of Xt
        self.Xt = np.array([]) # Stores combined Xt

    # Concat all Xt into a single Xt
    def concat_all(self):
        for i in range(self.nXt-1):
            self.concat_two(i, i+1)
        print("Concat dictionary is:")
        print(self.projection)
        self.output()
        return self.Xt

    # Concatenate Xt_lst[index_i] and Xt_lst[index_j]
    def concat_two(self, index_i, index_j):
        Xt1 = self.Xt_lst[index_i]
        Xt2 = self.Xt_lst[index_j]
        Xt1_tail = Xt1[-self.overlap_rows: ]
        Xt2_head = Xt2[ :self.overlap_rows]
        self.projection.append({})
        for i in range(self.nballs):
            for j in range(self.nballs):
                if self.same_position(Xt1_tail[0][i],Xt2_head[0][j]):
                    self.projection[index_i][i] = j
        if not self.concat_is_correct(Xt1_tail, Xt2_head, index_i):
            print("Failed concatenating. Force to exit.")
        # The following is for human check
        #else:
        #    self.humancheck(Xt1_tail, Xt2_head, index_i)
        #    print("Concatenation is good")
                    
    # Check if the projection provided by concatenate is correct
    # Parameter:
    # index: self.projection[i] is the dictionary used for checking
    #        concatenation of 2 Xt.
    def concat_is_correct(self, Xt1_tail, Xt2_head, index):
        # check if projection is 1 to 1
        value_set = set()
        for i in range(self.nballs):
            # Exception handling in case dict is not compelete.(Missing key)
            try:
                value_set.add(self.projection[index][i])
            except KeyError as error:
                print("Concatenation failed. Please check input csv file.")
        if len(value_set) != self.nballs:
            return False
        # Use data from 2nd rows to verify projection
        for i in range(self.nballs):
            if not self.same_position(Xt1_tail[1][i],
                                      Xt2_head[1][self.projection[index][i]]):
                return False
        return True
    
    # Compare 2 coordinates. A helper function
    def same_position(self, x1, x2):
        for i in range(len(x1)):
            if x2[i]+0.001 < x1[i] or x1[i] < x2[i]-0.001: # if x1[i] != x2[i]
                return False
        return True
    
    # Output the concatenated part for human checking 
    def humancheck(self, Xt1_tail, Xt2_head, index_i):
        for i in range(self.overlap_rows):
            for j in range(self.nballs):
                print(Xt1_tail[i][j],Xt2_head[i][self.projection[index_i][j]])
            print("")

    # Output the concatenated csv file
    def output(self):
        self.Xt = np.array(self.Xt_lst[self.nXt-1])
        # Pass Xt_lst[0] because of the line above
        # for i in range(5,0,-1) print i # Prints 5 4 3 2 1
        # for i in range(5,-1,-1) print i # Prints 5 4 3 2 1 0
        for i in range(self.nXt-2,-1,-1):
            temp = np.zeros_like(self.Xt)
            for j in range(self.nballs):
                temp[:,j] = self.Xt[:,self.projection[i][j]]
            self.Xt = np.vstack((np.array(self.Xt_lst[i]),temp[self.overlap_rows:]))

        #for i in range(self.nballs):
        #    print(self.Xt[:,i]) # ball_i's [t][x,y]

        # Output to file
        with open('concatenate.csv', mode='w') as concat_file:
            concat_writer = csv.writer(concat_file, delimiter=',')
            row_header = [] # csv header
            for i in range(self.nballs):
                row_header.append("x"+str(i+1))
                row_header.append("y"+str(i+1))
            concat_writer.writerow(row_header)
            for i in range(len(self.Xt)):
                concat_writer.writerow(self.Xt[i].reshape(self.nballs*2,))
