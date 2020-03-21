class FITNESS_FUNCTION:

    def __init__(self):

        self.terms = {}

        cols = np.random.randint(1,500)
        rows = np.random.randint(1,500)
        self.terms['s'] = sensorData = np.random.random([cols,rows]) * 2 - 1 

    def Print(self):

        print(self.terms)
