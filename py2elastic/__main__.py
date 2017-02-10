import logging
import argparse
from datetime import datetime

from .stype.csv import Input
from .es import Output

## collate args
def collate_args():
    parser = argparse.ArgumentParser(
        description='Turn CSV in to ElasticSearch documents.'
    )
    parser.add_argument(
        '--log',
        default="INFO",
        required=False,
        help='Log level: INFO, DEBUG, WARN, etc.'
    )
    Input.add_args(parser)
    Output.add_args(parser)
    return parser.parse_args()
    
args = collate_args()

## sort out logging

logging.basicConfig(
    level=getattr(logging, args.log.upper())
)

## setup inputs and outputs

input_proc = Input.from_args(args)
output_proc = Output.from_args(args)

## process
now = datetime.now()
logging.info("Started at {0}".format(now.strftime("%c")))

output_proc.run(input_proc.data)

later = datetime.now()
delta = later-now
logging.info("Finished at {0}. Took {1}s".format(
    later.strftime("%c"),
    delta.total_seconds()
))
