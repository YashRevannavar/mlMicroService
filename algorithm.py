import pickle
from webFunction import get_data_from_form

labels = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

def open_file():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_fucn():
    data = get_data_from_form()
    model = open_file()
    prediction = model.predict(data)
    print(f"no: {prediction}")
    if prediction == 0:
        return labels[0]
    elif prediction == 1:
        return labels[1]
    else:
        return labels[2]