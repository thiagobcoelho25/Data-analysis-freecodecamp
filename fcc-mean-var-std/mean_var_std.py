import numpy as np

def calculate(list):
  calculations = {}
  
  
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  matrix = np.array(list).reshape(3,3)
  
  calculations["mean"] = [matrix.mean(0).tolist(),matrix.mean(1).tolist(),matrix.mean()]

  calculations["variance"] = [np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix)]

  calculations["standard deviation"] = [np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix)]

  calculations["max"] = [np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix)]

  calculations["min"] = [np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix)]

  calculations["sum"] = [np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(matrix)]



  return calculations