class ClsBaseAlgorithm:
    def __init__(self):
        self.problem_types = []
        self.is_supervised = []

    def check_problem(self, problem_info):
        return problem_info["type"] in self.problem_types and problem_info["is_supervised"] in self.is_supervised

    def echo(self):
        print(type(self).__name__)

    def name(self):
        return type(self).__name__

    def train(self, data):
        print("not implemented")

    def dumps(self):
        return bytes("dump", encoding="utf8")

    def save(self, file_name):
        f = open(file_name, "+wb")
        f.write(self.dumps())
        f.close()
