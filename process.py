import algorithm


def train_algs(train_data, problem_info):
    algs = algorithm.algChoose(problem_info)
    for alg in algs:
        alg.train(train_data)
    return algs


if __name__ == '__main__':
    from sklearn.datasets import load_iris
    algs = train_algs(load_iris(), {"type": "classification", "is_supervised": True})
    for alg in algs:
        alg.save("iris[" + alg.name() + "].txt")
