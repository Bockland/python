from sklearn.datasets import load_iris

iris = load_iris()

nombreAtributos = iris.feature_names
nombreResultados = iris.target_names
print(iris.target_names)