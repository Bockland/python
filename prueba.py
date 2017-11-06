from sklearn import tree

datos = [[140,1],[130,1],[150,0],[160,0]]
resultados = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(datos, resultados)

print(clf.predict([[135,1]]))
