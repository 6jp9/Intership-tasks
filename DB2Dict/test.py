import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.json())



def create_resource():
    new_data = {
        'name':'sunny',
        'address':'mumbai',
    }
    resp = requests.post(BASE_URL+END_POINT,data=json.dumps(new_data))

    print(resp.json())
# create_resource()


def update_resource(id):
    data = {
        'id':id,
        'name':'pj',
        'address':'goa'
    }
    resp = requests.put(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.json())
#update_resource(2)


def delete_resource(id):
    data={
        'id':id
    }
    resp = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.json())
delete_resource(5)




get_resource()
