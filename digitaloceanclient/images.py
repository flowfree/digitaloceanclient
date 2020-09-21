from .http_client import HttpClient
from .models import Image


class Images(HttpClient):
    model = Image

    def all(self, type_=None):
        if type_:
            if type_ in ['distribution', 'application']:
                params = {'type': type_}
            elif type_ == 'private':
                params = {'private': True}
            else:
                raise ValueError(f'Invalid type: {type_}')
        else:
            params = None

        return super().all(params)
