import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

train = pd.read_csv("iris.csv")
test = pd.read_csv("iris2.csv")
# train,test = train_test_split(train, train_size=0.5)


clf = DecisionTreeClassifier(max_depth=4)
clf.fit(train.drop("class",axis=1), train["class"])
y_hat = clf.predict(test.drop("class",axis=1))
print((y_hat == test["class"]).sum()/len(test))
# submit =pd.DataFrame(y_hat, columns =["gender"], index = train["user"])
# submit.to_csv("submit.csv") 