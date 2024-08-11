import json
from typing import Any
import pandas as pd
import numpy as np

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from model_creation import __version__ as model_version
from model_creation.predict import make_prediction

from app import __version__, schemas
from app.config import settings


api_router = APIRouter()

@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    health = schemas.Health(
        #name='API TEST', api_version='0.0.1', model_version='0.0.1'
         name = settings.PROJECT_NAME, api_version = __version__, model_version = model_version
    )
    return health.dict()

@api_router.post("/predict", response_model= schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleDiabetesInputs) -> Any:
      """
      Make prediction with tid diabetes model
      """
      input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

      logger.info(f"Making prediction on inputs: {input_data.inputs}")

      results = make_prediction(input_data = input_df.replace({np.nan: None}))
      #results['predictions'] = results['predictions'].tolist()
      results['predictions'] = list(results['predictions'])

      if results["errors"] is not None:
          logger.warning(f"Prediction Validation Errors: {results.get('errros')}")
          raise HTTPException(status_code=400, detail = json.loads(results["errors"]))

      logger.info(f"Prediction Results : {results.get('predictions')}")
      logger.info(f"Check Results : {type(results.get('predictions'))}")

      return results

