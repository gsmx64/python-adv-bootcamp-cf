import requests

def unreleased() -> str:
    """Retorna los próximos talleres en CódigoFacilito.
    
    >>> type(unreleased()) == type(list())
    True
    
    >>> type(unreleased()) == type(dict())
    False
    """
    # La otra url no está operativa
    response = requests.get('https://codigofacilito.com/api/v2/workshops/')

    if response.status_code == 200:
        payload = response.json()
        #print(type(payload))
        return payload['data']
    
    #print(f'El valor de main para workshop es {__name__}')
