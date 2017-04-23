real_distance=[
    [0,11,0,0,0,0,0,0,0,0,0,0,0,0],
    [11,0,9,0,0,0,0,0,11,4,0,0,0,0],
    [0,9,0,7,0,0,0,0,10,0,0,0,19,0],
    [0,0,7,0,14,0,0,15,0,0,0,0,12,0],
    [0,0,0,14,0,3,2,33,0,0,0,0,0,0], #5
    [0,0,0,0,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,15,33,0,0,0,10,0,0,7,0,0],
    [0,11,10,0,0,0,0,10,0,0,14,0,0,0],
    [0,4,0,0,0,0,0,0,0,0,0,0,0,0], #10
    [0,0,0,0,0,0,0,0,14,0,0,0,0,0],
    [0,0,0,0,0,0,0,7,0,0,0,0,0,0],
    [0,0,19,12,0,0,0,0,0,0,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,5,0]
]

distance_in_line=[
    [0,11,20,27,40,43,39,28,18,10,18,30,30,32],
    [11,0,9,16,29,32,28,19,11,4,17,23,21,24],
    [20,9,0,7,20,22,19,15,10,11,21,21,12,18],
    [27,16,7,0,13,16,12,13,13,18,26,21,11,17],
    [40,29,20,13,0,3,2,21,25,31,38,27,16,20],
    [43,32,22,16,3,0,4,23,28,33,41,30,17,20],
    [39,28,19,12,2,4,0,22,25,29,38,28,13,17],
    [28,19,15,13,21,23,22,0,9,22,18,7,25,30],
    [18,11,10,13,25,28,25,9,0,13,12,12,23,28],
    [10,4,11,18,31,33,29,22,13,0,20,27,20,23],
    [18,17,21,26,38,41,38,18,12,20,0,15,35,39],
    [30,23,21,21,27,30,28,7,12,27,15,0,31,37],
    [30,21,13,11,16,17,13,25,23,20,35,31,0,5],
    [32,24,18,17,20,20,17,30,28,23,39,37,5,0]
]

blue = [0, 1, 2, 3, 4]
yellow = [9, 1, 8, 7, 4, 6]
red = [10, 8, 2, 13]
green =[11, 7, 3, 12,13]

lines=[blue, yellow, red, green]

class PathItem:
    """ """
    def __init__(self, station, parent=None):
        self.station=station
        self.velocity =30 #km/h
        self.parent = parent
        self.cost_f=0
        self.line = -1
        if parent != None:
            for i, line in enumerate(lines):
                if self.station in line and self.parent.station in line:
                    self.line = i

    def __lt__(self, other):
        return self.cost_f < other.cost_f

    def equals(self, other):
        pass

    def calculate_equals(self, target):
       pass

    def calc_G(self):
        current = self
        current_parent = self.parent
        cost =0
        while current_parent != None:
            d = real_distance[current_parent.station][current.station]
            cost = cost + (d / current.velocity * 60)
            if current_parent.line != -1 and current.line != current_parent.line:
                cost = cost +5
     
            current = current_parent
            current_parent = current_parent.parent
        return cost

    def calc_H(self, target):
        """
        custo em minutos
        """
        return distance_in_line[self.station][target.station] / self.velocity * 60

    def recalculate_cost(self, target):
        self.cost_f = self.calculate_cost(target)

    def calculate_cost(self, target):
        '''
        F = G + H
        '''
        return self.calc_G() + self.calc_H(target)
    
    
    def swap_zero(self, zero_row, zero_col, row, col):
        passs

    def get_adjacent(self):
        adjacents = []

        for i, distance in enumerate(real_distance[self.station]):
            if distance != 0:
                adjacents.append(PathItem(i,self))

        return adjacents
