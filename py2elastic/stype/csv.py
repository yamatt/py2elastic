import logging
import csv
from os.path import basename

class Input(object):
    OPEN_TYPE="r"
    @classmethod
    def from_args(cls, args):
        return cls.from_path(
            args.source[0]
        )
        
    @classmethod
    def from_path(cls, path):
        return cls(
            open(path, cls.OPEN_TYPE)
        )
        
    def __init__(self, f):
        self.f = f
        self._data = None
        
    @property
    def data(self):
        if self._data is None:
            self._data = csv.DictReader(self.f)
        return self._data

    @staticmethod
    def add_args(parser):
        parser.add_argument(
            'source',
            nargs=1,
            help='Path to CSV file'
        )
    

        
        


