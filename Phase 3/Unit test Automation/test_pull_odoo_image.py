import docker

def test_pull_odoo_image():
    client = docker.from_env()
    try:
        client.images.pull('odoo')
        assert True
    except docker.errors.ImageNotFound:
        assert False, "Odoo image not found"
    except Exception as e:
        assert False, str(e)
