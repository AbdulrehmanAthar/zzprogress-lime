import docker

def test_start_odoo_container():
    client = docker.from_env()
    try:
        container = client.containers.run('odoo', detach=True, ports={'8069/tcp': 8069})
        assert container.status == 'running'
        assert b'Odoo' in container.logs()
    except Exception as e:
        assert False, str(e)
    finally:
        container.stop()
