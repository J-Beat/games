from random import choice, uniform
import json

class River:
    def __init__(self):
        with open("D:/Python/games/text_adventure/cell_type.json", "rb") as read_file:
            data = json.load(read_file)
        self.cell_type = data['river']
        self.orientation = choice([0, 1])
        self.def_type = choice([self.create_S_type, self.create_U_type])


    def create_U_type(self):
        base = 0.5
        coeff = choice([-1, 1])
        # print(coeff)
        rndBx = uniform(0.0, 0.4)
        rndBy = uniform(0.0, 0.3)
        rndAx = uniform(-0.4, rndBx-0.1)
        rndCx = uniform(-0.4, rndBx-0.1)
        B = [base+rndBx*coeff, base+rndBy*coeff]
        A = [base+rndAx*coeff, 0]
        C = [base+rndCx*coeff, 1]
        rndABx = (A[0] + B[0])/2+uniform(-0.05, 0.05)
        rndABy = (0 + B[1])/2+uniform(-0.05, 0.05)
        AB = [rndABx, rndABy]
        rndBCx = (C[0] + B[0])/2+uniform(-0.05, 0.05)
        rndBCy = (1 + B[1])/2+uniform(-0.05, 0.05)
        BC = [rndBCx, rndBCy]
        A1 = [A[0], AB[1]]
        B1 = [B[0], AB[1]]
        B2 = [B[0], BC[1]]
        C1 = [C[0], BC[1]]
        result = [[A, A1, AB], [AB, B1, B], [B, B2, BC], [BC, C1, C]]
        return result


    def create_S_type(self):
        base = 0.5
        A = [base+uniform(-0.4, 0.4), 0]
        C = [base+uniform(-0.4, 0.4), 1]
        rndABx = (A[0] + C[0])/2
        rndABy = base+uniform(-0.1, 0.1)
        B = [rndABx, rndABy]
        # print(A, B, C)
        A1 = [A[0], B[1]]
        C1 = [C[0], B[1]]
        result = [[A, A1, B], [B, C1, C]]
        # print(result)
        return result
    
    