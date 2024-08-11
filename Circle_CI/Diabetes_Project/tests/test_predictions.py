import math

import numpy as np

from model_creation.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 1
    expected_no_predictions = 1

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    # print("predictions : " + str(predictions[0]))
    # assert isinstance(predictions, list)
    # assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
    # assert len(predictions) == expected_no_predictions
    # assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
    assert math.isclose(predictions[0], expected_first_prediction_value)
