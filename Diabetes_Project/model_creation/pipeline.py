from feature_engine.imputation import MeanMedianImputer
from feature_engine.transformation import LogTransformer
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.pipeline import Pipeline

from model_creation.config.core import config

outcome = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute numerical variables with the mean
        (
            "mean_imputation",
            MeanMedianImputer(
                imputation_method="mean",
                variables=config.model_config.numerical_vars_with_na,
            ),
        ),
        # ==== VARIABLE TRANSFORMATION =====
        # ("log", LogTransformer(variables=config.model_config.numericals_log_vars)),
        (
            "LogisticRegression",
            LogisticRegression(
                # alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
