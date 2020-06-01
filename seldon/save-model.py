#!/usr/bin/env python

import mlflow, mlflow.sklearn
import sys
import os

def main():
    # https://mlflow-user1.apps.ocp.ltsai.com
    # run id 241d39225722466f8cf770bb91f04513

    print('MLFLOW_TRACKING_URI: ' + os.environ['MLFLOW_TRACKING_URI'])
    print('MLFLOW RUN ID: ' + os.environ['MLFLOW_RUN_ID'])
    mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])
    
    #run = mlflow.get_run(os.environ['MLFLOW_RUN_ID'])    
    #print('Git Commit: {}'.format(run.data.tags['mlflow.source.git.commit'] ))
    sk_model = mlflow.sklearn.load_model("runs:/{}/model".format(os.environ['MLFLOW_RUN_ID']))

    model_path = os.environ['HOME'] + '/model'
    print('Saving model to ' + model_path)
    mlflow.sklearn.save_model(sk_model, model_path,
        serialization_format=mlflow.sklearn.SERIALIZATION_FORMAT_CLOUDPICKLE)

if __name__ == '__main__':
    main()
