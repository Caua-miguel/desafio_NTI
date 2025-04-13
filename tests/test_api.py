from project.services.api_services import BranchesAlfa

def test_get_data_branches_retunrs_correct_json(mocker):
    
    test_params = {
        'cnpj': "82.110.818/0001-21",
        'nome': "ALFA TRANSPORTES LTDA",
        'municipio': "CACADOR",
        'uf': "SC",
    }

    cnpj = ["82110818000121"]
    
    alfa = BranchesAlfa(cnpjs=cnpj)

    mock_requests = mocker.patch("project.services.api_services.requests.get")
    mock_requests.return_value = mocker.Mock(**{"status_code": 200, 
                                                "json.return_value": test_params})
    

    assert alfa.get_data_branches(cnpj[0]) == test_params
    
