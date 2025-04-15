from project.services.branches_services import Branche

def test_select_branche(mocker):

    fake_branch = mocker.Mock()
    fake_branch.as_dict.return_value = {
        'cnpj': '82110818000121',
        'name': 'ALFA TRANSPORTES LTDA',
        'city': 'CACADOR',
        'state': 'SC',
    }

    mock_query = mocker.patch("project.services.branches_services.db.session.query")
    mock_query.return_value.all.return_value = [fake_branch]


    Branche.select_branches()

    expected_data = [{
        'cnpj': "82110818000121",
        'name': "ALFA TRANSPORTES LTDA",
        'city': "CACADOR",
        'state': "SC"
    }]

    mock_query.assert_called_once()

    assert Branche.select_branches() == expected_data

def test_add_branche_calls_insert(mocker):

    test_params = [{
        'cnpj': "82110818000121",
        'name': "ALFA TRANSPORTES LTDA",
        'city': "CACADOR",
        'state': "SC",
    }]

    cnpj = ["82110818000121"]

    mocker.patch("project.services.branches_services.BranchesAlfa.collect_branches_data", return_value=test_params)
    mock_add = mocker.patch("project.services.branches_services.db.session.add")
    mock_commit = mocker.patch("project.services.branches_services.db.session.commit")

    Branche.insert_branches(cnpj)

    expected_data = {
        'cnpj': "82110818000121",
        'name': "ALFA TRANSPORTES LTDA",
        'city': "CACADOR",
        'state': "SC"
    }
    
    mock_add.assert_called_once()
    mock_commit.assert_called_once()

    """Essa parte basicamente foi feita para acessar o que tem dentro do objeto Branches,
     as partes que precisamos para o teste. Se não, o teste falha porque o sqlalchemy está
     gerando um id aleaório sempre que usamos o insert."""

    args, _ = mock_add.call_args
    added_obj = args[0]

    assert added_obj.tbb_s_cnpj == expected_data['cnpj']
    assert added_obj.tbb_s_name == expected_data['name']
    assert added_obj.tbb_s_city == expected_data['city']
    assert added_obj.tbb_s_state == expected_data['state']

    