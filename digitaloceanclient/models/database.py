from . import Model


class Database(Model):
    """
    Represents a Database in DigitalOcean's managed database service.

    Attributes
    ----------
    id : str
        Unique identifier for the database cluster
    name : str
        A Unique human-readable name 
    engine : str
        Slug representing the database engine used for the cluster
    version : str
        Version of the database cluster
    connection : Database.Connection
        Information about how to connect to the database
    private_connection : Database.Connection
        Information about how to connect to the database via the private network
    users : list
        An array containing objects describing the database's users
    db_names : list
        An array of strings containing the names of databases created 
        in the database cluster
    num_nodes : int
        The number of nodes in the database cluster
    size : str
        Slug representing the size of the nodes
    region : str
        Slug for the region where the database is located
    status : str
        Current status of the database cluster
        Possible values: creating, online, resizing, migrating
    maintenance_window : Database.MaintenanceWindow
        An object containing information about any pending maintenance for 
        the database cluster and when it will occur
    created_at : str
        When the database cluster was created
    tags : list
        Array of tags for this database cluster
    private_network_uuid : str
        string specifying the UUID of the VPC to which the database 
        cluster is assigned
    """

    ENGINE_POSTGRESQL = 'pg'
    ENGINE_MYSQL = 'mysql'
    ENGINE_REDIS = 'redis'

    STATUS_CREATING = 'creating'
    STATUS_ONLINE = 'online'
    STATUS_RESIZING = 'resizing'
    STATUS_MIGRATING = 'migrating'

    id = ''
    name = ''
    engine = ''
    version = ''
    connection = None
    private_connection = None
    users = []
    db_names = []
    num_nodes = 0
    size = ''
    region = ''
    status = ''
    maintenance_window = None 
    created_at = ''
    tags = []
    private_network_uuid = ''


    class Connection(Model):
        """
        Describes how to connect to a database.

        Attributes
        ----------
        uri : str
            A connection string in the format accepted by the psql command
        database : str
            The name of the default database
        host : str
            The FQDN pointing to the database cluster's current primary node
        port : int
            The port on which the database cluster is listening
        user : str
            The default user for the database
        password : str
            The randomly generated password for the default user
        ssl : bool
            Whether the connection should be made over SSL
        """

        uri = ''
        database = ''
        host = ''
        port = 0
        user = ''
        password = ''
        ssl = True


    class User(Model):
        """
        Describes a user for the database.

        Attributes
        ----------
        name : str
            The name of the database user
        role : str
            A string representing the database user's role
            The value will be either "primary" or "normal".
        password : str
            Randomly generated password for the database user
        """

        ROLE_PRIMARY = 'primary'
        ROLE_NORMAL = 'normal'

        name = ''
        role = ''
        password = ''


    class MainTenanceWindow(Model):
        """
        Describes information about any pending maintenance for the 
        database cluster and when it will occur.

        Attributes
        ----------
        day : str
            The day of the week on which to apply maintenance updates
        hour : str
            The hour in UTC at which maintenance updates will be applied 
            in 24 hour format
        pending : bool
            Whether any maintenance is scheduled to be performed 
            in the next window
        description : list
            A list of strings, each containing information about a pending 
            maintenance update
        """

        day = ''
        hour = ''
        pending = False
        description = []


    def __init__(self, data):
        super().__init__(data)
        try:
            self.connection = Database.Connection(data['connection'])
        except KeyError:
            pass
        try:
            self.private_connection = Database.Connection(data['private_connection'])
        except KeyError:
            pass
        try:
            self.users = [Database.User(u) for u in data['users']]
        except KeyError:
            pass
        try:
            self.maintenance_window = Database.MainTenanceWindow(data['maintenance_window'])
        except KeyError:
            pass
