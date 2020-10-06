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

    def create(self, type_, name, private_key=None, leaf_certificate=None, 
              certificate_chain=None, dns_names=None):
        """
        Create new certificate.

        Parameters
        ----------
        type_ : {'custom', 'lets_encrypt'}
            The type of the certificate.
        name : str
            The name of the certificate.
        private_key : str, optional
            The contents of a PEM-formatted private-key corresponding 
            to the SSL certificate. Required if type_=custom.
        leaf_certificate : str, optional
            The contents of a PEM-formatted public SSL certificate.
            Required if type_=custom.
        certificate_chain : str, optional
            The full PEM-formatted trust chain between the certificate 
            authority's certificate and your domain's SSL certificate.
        dns_names : list, optional
            An array of fully qualified domain names (FQDNs) for which 
            the certificate will be issued. The domains must be managed 
            using DigitalOcean's DNS. Required if type_=lets_encrypt.

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
        }
        if type_ == 'custom':
            if private_key is None or leaf_certificate is None:
                raise ValueError('private_key and leaf_certificate are '
                                 'required for custom certificate.')
            payload['private_key'] = private_key
            payload['leaf_certificate'] = leaf_certificate
            if certificate_chain:
                payload['certificate_chain'] = certificate_chain
        elif type_ == 'lets_encrypt':
            if dns_names is None:
                raise ValueError("dns_names is required for "
                                 "Let's Encrypt certificate")
            payload['dns_names'] = dns_names

        return super().create(payload=payload)

    def get(self, certificate_id):
        """
        Retrieve existing certificate.

        Parameters
        ----------
        certificate_id : str
            The ID of the specified certificate.

        Returns
        -------
        digitaloceanclient.models.Certificate

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        return super().get(resource_id=certificate_id)

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError
