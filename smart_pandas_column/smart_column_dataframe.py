import pandas as pd
import logging
from .utils import get_closest_match

class SmartColumnDataFrame(pd.DataFrame):
    maximum_allowed_wrong_characters = 3
    def __getitem__(self, key):
        try:
            super(self.__class__, self).__getitem__(key)
        except KeyError as e:
            new_key, dist = get_closest_match(key, self.columns)
            if (dist <= SmartColumnDataFrame.maximum_allowed_wrong_characters):
                logging.warn(f" Unable to find column '{key}'. Maybe you meant '{new_key}' ? Returning '{new_key}' for now but please correct it")
                return super(self.__class__, self).__getitem__(new_key)
            else:
                raise e


def read_csv(*args, **kwargs):
    return SmartColumnDataFrame(pd.read_csv(args, kwargs))