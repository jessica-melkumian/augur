import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import annotate

def create_insight_metrics(metrics):

    database = metrics.db

