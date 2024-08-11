import numpy as np
from config.core import config
from pipeline import outcome
from processing.data_managers import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split


def run_training() -> None:
    """Model Training"""

    """Loading Dataset"""
    data = load_dataset(filename=config.app_config.training_data_file)

    """Splitting Dataset Into Train and Test"""
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],  # Predictors
        data[config.model_config.target],  # Target
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
        # stratify = config.model_config.stratify,
    )

    # fit model
    outcome.fit(X_train, y_train)

    # persist training model
    save_pipeline(pipeline_to_persist=outcome)


if __name__ == "__main__":
    run_training()
