from typing import Any, List, Optional

from pydantic import BaseModel
from model_creation.processing.validation import DiabetesInputSchema
import numpy as np
#from pydantic_numpy import np_array_pydantic_annotated_typing

class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]
    #predictions: np_array_pydantic_annotated_typing(data_type=np.float32)
    #predictions: np.ndarray

class MultipleDiabetesInputs(BaseModel):
    inputs: List[DiabetesInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Pregnancies": 6,
                        "Glucose": 148,
                        "BloodPressure": 72,
                        "SkinThickness": 35,
                        "Insulin": 0,
                        "BMI": 33.6,
                        "DiabetesPedigreeFunction": 0.627,
                        "Age": 50
                    }
                ]
            }
        }