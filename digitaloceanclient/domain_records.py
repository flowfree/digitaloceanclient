from .http_client import HttpClient
from .models import DomainRecord


class DomainRecords(HttpClient):
    """
    Retrieve, create, update, and delete domain records.
    """

    model = DomainRecord

    def all(self, for_domain, name=None, type_=None):
        """
        List all domain records.

        Parameters
        ----------
        for_domain : str
            Get the records for the specified domain.
        name : str, optional
            The host name, alias, or service being defined by the record.
        type_ : str, optional
            The type of the DNS record.

        Yields
        ------
        digitaloceanclient.models.DomainRecord

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'domains/{for_domain}/records'
        params = {}
        if name:
            params['name'] = name
        if type_:
            params['type'] = type_
        return super().all(path=path, params=params, json_key='domain_records')

    def create(self, for_domain, type_, name=None, data=None, priority=None,
               port=None, ttl=None, weight=None, flags=None, tag=None):
        """
        Create a new record for a domain.

        Parameters
        ----------
        for_domain : str
            The domain for the record to be added to.
        type_ : str
            The record type.
        name : str, optional
            The host name, alias, or service being defined by the record.
            Required for: A, AAAA, CAA, CNAME, TXT, SRV
        data: str, optional
            The data for the domain record.
            Required for: A, AAAA, CAA, CNAME, MX, TXT, SRV, NS
        priority : int, optional
            The priority of the host.
            Required for: MX, SRV
        port : int, optional
            The port that the service is accessible on.
            Required for: SRV
        ttl: int, optional
            This value is the time to live for the record, in seconds.
            Required for: SOA
        weight: int, optional
            The weight of records with the same priority.
            Required for: SRV
        flags: int, optional
            An unsigned integer between 0-255 used for CAA records.
        tag: {"issue", "issuewild", "iodef"}, optional
            The parameter tag for CAA records.

        Returns
        -------
        digitaloceanclient.models.DomainRecord

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'domains/{for_domain}/records'
        payload = {'type': type_}
        if name:
            payload['name'] = name
        if data:
            payload['data'] = data
        if priority:
            payload['priority'] = priority
        if port:
            payload['port'] = port
        if ttl:
            payload['ttl'] = ttl
        if weight:
            payload['weight'] = weight
        if flags:
            payload['flags'] = flags
        if tag:
            payload['tag'] = tag
        return super().create(path=path, payload=payload)

    def get(self, for_domain, id_):
        """
        Retrieve an existing domain record.

        Parameters
        ----------
        for_domain : str
            The domain name where this record exist.
        id_ : str
            The identifier for the domain record.

        Returns
        -------
        digitaloceanclient.models.DomainRecord

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'domains/{for_domain}/records'
        return super().get(path=path, resource_id=id_)

    def update(self, for_domain, id_, type_=None, name=None, data=None, 
               priority=None, port=None, ttl=None, weight=None, flags=None,
               tag=None):
        """
        Update existing domain record.

        Parameters
        ----------
        for_domain : str
            The domain where the record exist.
        type_ : str, optional
            The record type.
        name : str, optional
            The host name, alias, or service being defined by the record.
            Available for: A, AAAA, CAA, CNAME, TXT, SRV
        data: str, optional
            The data for the domain record.
            Available for: A, AAAA, CAA, CNAME, MX, TXT, SRV, NS
        priority : int, optional
            The priority of the host.
            Available for: MX, SRV
        port : int, optional
            The port that the service is accessible on.
            Available for: SRV
        ttl: int, optional
            This value is the time to live for the record, in seconds.
            Available for: SOA
        weight: int, optional
            The weight of records with the same priority.
            Available for: SRV
        flags: int, optional
            An unsigned integer between 0-255 used for CAA records.
        tag: {"issue", "issuewild", "iodef"}, optional
            The parameter tag for CAA records.

        Returns
        -------
        digitaloceanclient.models.DomainRecord

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        payload = {} 
        if name:
            payload['name'] = name
        if data:
            payload['data'] = data
        if priority:
            payload['priority'] = priority
        if port:
            payload['port'] = port
        if ttl:
            payload['ttl'] = ttl
        if weight:
            payload['weight'] = weight
        if flags:
            payload['flags'] = flags
        if tag:
            payload['tag'] = tag
        
        path = f'domains/{for_domain}/records'
        return super().update(resource_id=id_, payload=payload, path=path)

    def delete(self, for_domain, id_):
        """
        Delete a domain record.

        Parameters
        ----------
        for_domain : str
            The domain name where this record exist.
        id_ : str
            The identifier for the domain record.

        Raises
        ------
        digitaloceanclient.exceptions.APIError
        """

        path = f'domains/{for_domain}/records'
        return super().delete(resource_id=id_, path=path)
