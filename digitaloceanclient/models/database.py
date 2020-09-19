from . import Model


class Database(Model):
    ENGINE_POSTGRESQL = 'pg'
    ENGINE_MYSQL = 'mysql'
    ENGINE_REDIS = 'redis'

    STATUS_CREATING = 'creating'
    STATUS_ONLINE = 'online'
    STATUS_RESIZING = 'resizing'
    STATUS_MIGRATING = 'migrating'

    # Unique identifier for the database cluster
    id = ''

    # A Unique human-readable name 
    name = ''

    # Slug representing the database engine used for the cluster
    engine = ''

    # Version of the database cluster
    version = ''

    # An object containing the information required to connect to the database
    connection = None

    # An object containing the information required to connect to the database 
    # via the private network
    private_connection = None

    # An array containing objects describing the database's users
    users = []

    # An array of strings containing the names of databases created 
    # in the database cluster
    db_names = []

    # The number of nodes in the database cluster
    num_nodes = 0

    # Slug representing the size of the nodes
    size = ''

    # Slug for the region where the database is located
    region = ''

    # Current status of the database cluster
    # Possible values: creating, online, resizing, migrating
    status = ''

    # An object containing information about any pending maintenance for 
    # the database cluster and when it will occur
    maintenance_window = None 

    # When the database cluster was created
    created_at = ''

    # Array of tags for this database cluster
    tags = []

    # string specifying the UUID of the VPC to which the database 
    # cluster is assigned
    private_network_uuid = ''


    class Connection(Model):
        # A connection string in the format accepted by the psql command
        uri = ''

        # The name of the default database
        database = ''

        # The FQDN pointing to the database cluster's current primary node
        host = ''

        # The port on which the database cluster is listening
        port = 0

        # The default user for the database
        user = ''

        # The randomly generated password for the default user
        password = ''

        # Whether the connection should be made over SSL
        ssl = True


    class User(Model):
        ROLE_PRIMARY = 'primary'
        ROLE_NORMAL = 'normal'

        # The name of the database user
        name = ''

        # A string representing the database user's role
        # The value will be either "primary" or "normal".
        role = ''

        # Randomly generated password for the database user
        password = ''


    class MainTenanceWindow(Model):
        # The day of the week on which to apply maintenance updates
        day = ''

        # The hour in UTC at which maintenance updates will be applied 
        # in 24 hour format
        hour = ''

        # Whether any maintenance is scheduled to be performed 
        # in the next window
        pending = False

        # A list of strings, each containing information about a pending 
        # maintenance update
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
