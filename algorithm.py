import pickle
from webFunction import get_data_from_form

labels = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

def open_file():
    """
    Load a machine learning model from a pickle file.
    Returns:
    - model: A trained machine learning model object.
    """
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


def predict_fucn():
    """
    Uses the input data to predict the Iris species using the saved model.
    Returns:
    -------
    prediction: str
    A string representing the predicted Iris species.
    """
    data = get_data_from_form()
    model = open_file()
    prediction = model.predict(data)
    if prediction == 0:
        return labels[0]
    elif prediction == 1:
        return labels[1]
    else:
        return labels[2]
