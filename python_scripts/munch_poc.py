from munch import Munch

response = Munch(ok=False, status=500)

if not response.ok:
    print(f'deu merda: {response.status}')
