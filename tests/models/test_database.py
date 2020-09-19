from digitaloceanclient.models import Database


def test_load_from_json():
    data = {
        "id": "9cc10173-e9ea-4176-9dbc-a4cee4c4ff30",
        "name": "backend",
        "engine": "pg",
        "version": "10",
        "connection": {
            "uri": "postgres://doadmin:wv78n3zpz42xezdk@backend-do-user-19081923-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require",
            "database": "",
            "host": "backend-do-user-19081923-0.db.ondigitalocean.com",
            "port": 25060,
            "user": "doadmin",
            "password": "wv78n3zpz42xezdk",
            "ssl": True
        },
        "private_connection": {
            "uri": "postgres://doadmin:wv78n3zpz42xezdk@private-backend-do-user-19081923-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require",
            "database": "",
            "host": "private-backend-do-user-19081923-0.db.ondigitalocean.com",
            "port": 25060,
            "user": "doadmin",
            "password": "wv78n3zpz42xezdk",
            "ssl": True
        },
        "users": [{
            "name": "doadmin",
            "role": "primary",
            "password": "wv78n3zpz42xezdk"
        }],
        "db_names": ["defaultdb"],
        "num_nodes": 1,
        "region": "nyc3",
        "status": "online",
        "created_at": "2019-01-11T18:37:36Z",
        "maintenance_window": {
            "day": "saturday",
            "hour": "08:45:12",
            "pending": True,
            "description": [
                "Update TimescaleDB to version 1.2.1",
                "Upgrade to PostgreSQL 11.2 and 10.7 bugfix releases"
            ]
        },
        "size": "db-s-2vcpu-4gb",
        "tags": ["production"],
        "private_network_uuid": "d455e75d-4858-4eec-8c95-da2f0a5f93a7"
    }

    database = Database(data)
 
    assert database.id == '9cc10173-e9ea-4176-9dbc-a4cee4c4ff30'
    assert database.name == 'backend'
    assert database.engine == Database.ENGINE_POSTGRESQL
    assert database.version == '10'
    assert database.connection.uri == 'postgres://doadmin:wv78n3zpz42xezdk@backend-do-user-19081923-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
    assert database.connection.database == ''
    assert database.connection.host == 'backend-do-user-19081923-0.db.ondigitalocean.com'
    assert database.connection.port == 25060
    assert database.connection.user == 'doadmin'
    assert database.connection.password == 'wv78n3zpz42xezdk'
    assert database.connection.ssl == True
    assert database.private_connection.uri == 'postgres://doadmin:wv78n3zpz42xezdk@private-backend-do-user-19081923-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
    assert database.private_connection.database == ''
    assert database.private_connection.host == 'private-backend-do-user-19081923-0.db.ondigitalocean.com'
    assert database.private_connection.port == 25060
    assert database.private_connection.user == 'doadmin'
    assert database.private_connection.password == 'wv78n3zpz42xezdk'
    assert database.private_connection.ssl == True
    assert database.users[0].name == 'doadmin'
    assert database.users[0].role == Database.User.ROLE_PRIMARY
    assert database.users[0].password == 'wv78n3zpz42xezdk'
    assert database.db_names == ["defaultdb"]
    assert database.num_nodes == 1
    assert database.region == 'nyc3'
    assert database.status == Database.STATUS_ONLINE
    assert database.created_at == '2019-01-11T18:37:36Z'
    assert database.maintenance_window.day == 'saturday'
    assert database.maintenance_window.hour == '08:45:12'
    assert database.maintenance_window.pending == True
    assert database.maintenance_window.description == [
        "Update TimescaleDB to version 1.2.1",
        "Upgrade to PostgreSQL 11.2 and 10.7 bugfix releases"
    ]
    assert database.size == 'db-s-2vcpu-4gb'
    assert database.tags == ["production"]
    assert database.private_network_uuid == 'd455e75d-4858-4eec-8c95-da2f0a5f93a7'
