import numpy as np
from river import stream
from statistics import mode
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def LCCDE(X_test, y_test, m1, m2, m3, model):
    yt, yp = [], []
    # Iterate over each sample in the test set
    for xi, yi in stream.iter_pandas(X_test, y_test):
        xi2 = np.array(list(xi.values()))
        # Predictions by each model
        y_pred1 = int(m1.predict(xi2.reshape(1, -1))[0])
        y_pred2 = int(m2.predict(xi2.reshape(1, -1))[0])
        y_pred3 = int(m3.predict(xi2.reshape(1, -1))[0])
        # Prediction probabilities
        p1, p2, p3 = m1.predict_proba(xi2.reshape(1, -1)), m2.predict_proba(xi2.reshape(1, -1)), m3.predict_proba(xi2.reshape(1, -1))
        y_pred_p1, y_pred_p2, y_pred_p3 = np.max(p1), np.max(p2), np.max(p3)

        # Decision logic
        if y_pred1 == y_pred2 == y_pred3:
            y_pred = y_pred1
        elif y_pred1 != y_pred2 != y_pred3:
            predictions = [(y_pred1, y_pred_p1, m1), (y_pred2, y_pred_p2, m2), (y_pred3, y_pred_p3, m3)]
            predictions = [pred for pred in predictions if model[pred[0]] == pred[2]]
            if len(predictions) == 1:
                y_pred = predictions[0][0]
            else:
                y_pred = max(predictions, key=lambda x: x[1])[0]
        else:
            # If two predictions are the same and the third is different
            n = mode([y_pred1, y_pred2, y_pred3])
            y_pred = int(model[n].predict(xi2.reshape(1, -1))[0])

        yt.append(yi)
        yp.append(y_pred)

    # Performance metrics
    accuracy = accuracy_score(yt, yp)
    precision = precision_score(yt, yp, average='weighted')
    recall = recall_score(yt, yp, average='weighted')
    f1 = f1_score(yt, yp, average='weighted')
    f1_each_attack = f1_score(yt, yp, average=None)

    # The performance of the proposed lCCDE model
    print("Accuracy of LCCDE: "+ str(accuracy))
    print("Precision of LCCDE: "+ str(precision))
    print("Recall of LCCDE: "+ str(recall))
    print("Average F1 of LCCDE: "+ str(f1))
    print("F1 of LCCDE for each type of attack: "+ str(f1_each_attack))

    return accuracy, precision, recall, f1, f1_each_attack

# This function could be called with the models and the model leaderboard
# accuracy, precision, recall, f1, f1_each_attack = LCCDE(X_test, y_test, m1, m2, m3, model)