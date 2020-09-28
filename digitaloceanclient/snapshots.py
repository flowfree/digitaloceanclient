from .http_client import HttpClient
from .models import Snapshot


class Snapshots(HttpClient):
    model = Snapshot
