from __future__ import generators
import json

__version__ = '1.0.0'
__all__ = ["cls_base_algorithm", "cls_decision_tree", "cls_random_forest"]
__author__ = 'Congying <congying1112@gmail.com>'

from .cls_base_algorithm import ClsBaseAlgorithm
from .cls_decision_tree import cls_decision_tree
from .cls_random_forest import cls_random_forest


def algChoose(prob_info):
    algs = []
    for alg in json.load(open("algorithm/algorithm_config.json", 'r')):
        alg_cls_name = "cls_" + "_".join(list(map(lambda x: x.lower(), alg["name"].split(" "))))
        alg = eval(alg_cls_name)()
        if alg.check_problem(prob_info):
            algs.append(alg)
    return algs


if __name__ == '__main__':
    algs = algChoose({"type": "classification"})
    for alg in algs:
        alg.echo()
