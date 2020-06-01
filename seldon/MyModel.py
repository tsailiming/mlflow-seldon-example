import mlflow.sklearn
import os

class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """
    
    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")

        model_path = os.environ['HOME'] + '/model'
        self.sk_model = mlflow.sklearn.load_model(model_path)

    def predict(self,X,features_names):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")
        return self.sk_model.predict(X)
