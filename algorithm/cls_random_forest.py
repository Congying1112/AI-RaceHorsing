from .cls_base_algorithm import ClsBaseAlgorithm
from sklearn.ensemble import RandomForestClassifier
import pickle


class cls_random_forest(ClsBaseAlgorithm):
    def __init__(self):
        ClsBaseAlgorithm.__init__(self)
        self.model = None
        self.problem_types = ["classification", "regression"]
        self.is_supervised = [True]

    def train(self, data):
        clf = RandomForestClassifier(n_estimators=100)
        self.model = clf.fit(data["data"], data["target"])

    def dumps(self):
        return pickle.dumps(self.model)
