from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from knn_preprocessor import x, y
import files_functions as ff



def get_kAcc(startK, endK, x_train, y_train, x_test, y_test):
    try:
        if startK <= 0:
            return 'Invalid Input'
        bestK_acc = {'accuracy': 0.0,
                     'best_k': 0}
        for k in range(startK, endK + 1):
            print('Start checking KNN with K = %s' %k)
            scalar_x = StandardScaler()
            x_train = scalar_x.fit_transform(x_train)
            x_test = scalar_x.transform(x_test)

            classifier = KNeighborsClassifier(n_neighbors=k)
            classifier.fit(x_train, y_train)
            predict_y = classifier.predict(x_test)
            temp = accuracy_score(y_test, predict_y)
            if temp > bestK_acc['accuracy']:
                bestK_acc['accuracy'] = temp
                bestK_acc['best_k'] = k
            print('End checking KNN with K = %s' %k)
        ff.save_to_json(bestK_acc, 'bestK_acc')
        return bestK_acc
    except:
        return 'Error- could not get_kAcc'


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

get_kAcc(1, 20, x_train, y_train, x_test, y_test)

