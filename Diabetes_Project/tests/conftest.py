import pytest

from model_creation.config.core import config
from model_creation.processing.data_managers import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(filename=config.app_config.test_data_file)
