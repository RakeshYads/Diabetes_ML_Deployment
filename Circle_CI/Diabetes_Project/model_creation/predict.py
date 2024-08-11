import typing as t

import numpy as np
import pandas as pd

from model_creation import __version__ as _version
from model_creation.config.core import config
from model_creation.processing.data_managers import load_pipeline
from model_creation.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_diabtes_type = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _diabtes_type.predict(
            X=validated_data[config.model_config.features]
        )
        results = {
            "predictions": predictions,  # [np.exp(pred) for pred in predictions],   #type: ignore
            "version": _version,
            "errors": errors,
        }

    return results
