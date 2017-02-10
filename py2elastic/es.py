import logging
from urllib.parse import urlparse
from json import dumps as jsondumps
from uuid import uuid4

from elasticsearch import Elasticsearch

def random_uuid():
    return uuid4().hex

class Output(object):
    
    @classmethod
    def from_args(cls, args):
        doc_type = args.doctype
        if args.doctype is None:
            doc_type = args.source
        return cls.from_url(
            url=args.esurl,
            doc_type=doc_type
        )
    
    @classmethod
    def from_url(cls, url, *args, **kwargs):
        url_parts = urlparse(url)
        return cls(
            [url_parts.netloc],
            index=url_parts.path[1:],
            *args, **kwargs
        )
        
    def __init__(self, *args, **kwargs):
        self.index = kwargs['index']
        self.args = args
        self.kwargs = kwargs
        self._es = None
        
    @property
    def es(self):
        if self._es is None:
            self._es = Elasticsearch(*self.args, **self.kwargs)
            logging.debug("Setup ElasticSearch connection")
            
        return self._es

    def run(self, ds):
        while True:
            logging.info("Started iterating through dataset")
            
            try:
                datum = next(ds)
                logging.debug("Processing new datum")
                
                self.es.create(
                    index=self.kwargs['index'],
                    body=jsondumps(datum),
                    id=random_uuid(),
                    doc_type=self.kwargs['doc_type']
                )
            except StopIteration as i:
                logging.info("Stopped iterating through dataset")
                break
                
    @staticmethod
    def add_args(parser):
        parser.add_argument(
            '--esurl',
            default="es://localhost:9200/es_index",
            required=False,
            help='URL to Elastic Search Instance'
        )
        parser.add_argument(
            '--doctype',
            required=False,
            help='doc_type to use for elastic search. Defaults to ' \
            'filename in source argument.'
        )
            
