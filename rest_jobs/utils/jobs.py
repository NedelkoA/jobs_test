from .data_api import get_job


class JobItem:
    def __init__(self, title):
        self._data = get_job(title)
        for key, value in self._data.items():
            setattr(self, key, value)
