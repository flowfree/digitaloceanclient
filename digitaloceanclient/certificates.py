from .http_client import HttpClient
from .models import Certificate


class Certificates(HttpClient):
    model = Certificate

    def all(self):
        """
        List all certificates.

        Yields
        ------
        digitaloceanclient.models.Certificate

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().all()

    def create(self, type_, name, private_key, 
               leaf_certificate, certificate_chain=None):
        """
        Create new certificate.

        Parameters
        ----------
        type_ : {'custom', 'lets_encrypt'}
            The type of the certificate.
        name : str
            The name of the certificate.
        private_key : str
            The contents of a PEM-formatted private-key corresponding 
            to the SSL certificate.
        leaf_certificate : str
            The contents of a PEM-formatted public SSL certificate.
        certificate_chain : str, optional
            The full PEM-formatted trust chain between the certificate 
            authority's certificate and your domain's SSL certificate.

        Returns
        -------
        digitaloceanclient.models.Certificate

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {
            'type': type_,
            'name': name,
            'private_key': private_key,
            'leaf_certificate': leaf_certificate,
        }
        if certificate_chain:
            payload['certificate_chain'] = certificate_chain
        return super().create(payload=payload)

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
