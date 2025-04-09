def test_app_is_created(app):
    assert app.name == "project"

def test_config_is_loaded(config):
    assert config["DEBUG"] is False

def test_request_home_returns_201(client):
    assert client.get("/").status_code == 201

def test_request_branches_add_success_returns_201(client):
    # Usar mock para simular o request dessa rota
    assert client.get("/filiais").status_code == 201

def test_request_branches_already_exists_returns_409(client):
    assert client.get("/filiais").status_code == 409