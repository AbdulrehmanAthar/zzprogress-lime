import docker
import psycopg2

client = docker.from_env()

def test_odoo_can_connect_to_postgres():
    # Start a new PostgreSQL container
    postgres_container = client.containers.run('postgres:latest', detach=True,
                                               environment={'POSTGRES_USER': 'odoo', 'POSTGRES_PASSWORD': 'odoo'})
    
    # Start a new Odoo container and link it to the PostgreSQL container
    odoo_container = client.containers.run('odoo:latest', detach=True,
                                           ports={'8069/tcp': 8069},
                                           links={postgres_container.name: 'db'})
    
    # Check that the Odoo container is running
    assert odoo_container.status == 'running'
    
    # Connect to the PostgreSQL container and check that the Odoo database exists
    conn = psycopg2.connect(host='localhost', port=postgres_container.ports['5432/tcp'][0]['HostPort'],
                            user='odoo', password='odoo', dbname='postgres')
    cur = conn.cursor()
    cur.execute("SELECT datname FROM pg_database WHERE datname='odoo';")
    result = cur.fetchone()
