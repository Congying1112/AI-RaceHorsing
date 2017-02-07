from .cls_base_algorithm import ClsBaseAlgorithm
from sklearn import tree
import pickle


class cls_decision_tree(ClsBaseAlgorithm):
    def __init__(self):
        ClsBaseAlgorithm.__init__(self)
        self.model = None
        self.problem_types = ["classification", "regression"]
        self.is_supervised = [True]

    def train(self, data):
        self.model = tree.DecisionTreeClassifier().fit(data["data"], data["target"])

    def dumps(self):
        return pickle.dumps(self.model)
