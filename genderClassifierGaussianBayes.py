from sklearn import naive_bayes

gnb = naive_bayes.GaussianNB()

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [181, 85, 43], [174, 75, 42], [190, 90, 47], [186, 62, 34], [199, 93, 50], [160, 85, 34]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female']


gnb.fit(X,Y)

prediction = gnb.predict([[190, 70, 43]])

print(prediction)