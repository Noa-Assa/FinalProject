from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from data_analysis.knn_preprocessor import preprocessing
from utilities import files_functions as ff
from datetime import datetime


def get_kAcc(startK, endK, x_train, y_train, x_test, y_test):
    try:
        if startK <= 0:
            return 'Invalid Input: Start K must be bigger than 0.'
        # bestK_acc = {'accuracy': 0.0,
        #              'best_k': 0}
        for k in range(startK, endK + 1):
            start_time = datetime.now()
            print('Start checking KNN with K = %s' %k)
            print('at: ', start_time)
            scalar_x = StandardScaler()
            x_train = scalar_x.fit_transform(x_train)
            x_test = scalar_x.transform(x_test)
            classifier = KNeighborsClassifier(n_neighbors=k)
            classifier.fit(x_train, y_train)
            predict_y = classifier.predict(x_test)
            temp = accuracy_score(y_test, predict_y)
            iteration_length = datetime.now() - start_time
            allK_acc = {'accuracy': temp,
                         'best_k': k,
                         'iteration_length': iteration_length}
            ff.save_to_json(allK_acc, 'allK_acc')
            # if temp > bestK_acc['accuracy']:
            #     bestK_acc['accuracy'] = temp
            #     bestK_acc['best_k'] = k
            print('End checking KNN with K = %s' %k)
            print('Iteration length: ', iteration_length, '\n')
#        return bestK_acc
        return
    except:
        return 'Error- could not get_kAcc'


def knn():
    x, y = preprocessing()
    test_size = float(input("how much percentage of the data would you like to use for training?\n for example: if you " 
                            "want to use 21% please enter: 0.21\n"))
    if (test_size >= 1) or (test_size <= 0):
        raise Exception('Invalid Input: Test size must be a decimal fraction between 0-100.')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    startK = int(input("Which K would like to check?\nfirst K: "))
    endK = int(input("last K: "))
    if startK > endK:
        raise Exception('Invalid Input: last K can be bigger or equal to first one, but not smaller.')
    get_kAcc(startK, endK, x_train, y_train, x_test, y_test)


