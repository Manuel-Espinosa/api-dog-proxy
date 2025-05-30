from src.proxy.dog_api_proxy import DogApiProxy

class DogUseCase:
    def __init__(self):
        self.proxy = DogApiProxy()

    def get_breeds(self, page=1):
        return self.proxy.fetch(f"/breeds?page[number]={page}&page[size]=10")

    def get_facts(self):
        return self.proxy.fetch("/facts")

    def get_groups(self):
        return self.proxy.fetch("/groups")

    def get_group(self, group_id):
        return self.proxy.fetch(f"/groups/{group_id}")

    def get_group_details(self, group_id):
        group = self.get_group(group_id)
        breeds = self.get_breeds()

        if 'data' in group and 'data' in breeds:
            group_breeds = [b for b in breeds['data'] if b['relationships']['group']['data']['id'] == group_id]
            return {"group": group['data'], "breeds": group_breeds}
        else:
            return {"error": "Failed to fetch group or breed data."}

    def get_group_breed(self, group_id, breed_id):
        group = self.get_group(group_id)
        breed = self.get_breed(breed_id)

        if 'data' in group and 'data' in breed:
            if breed['data']['relationships']['group']['data']['id'] == group_id:
                return {"group": group['data'], "breed": breed['data']}
            else:
                return {"error": "Breed does not belong to the group."}
        else:
            return {"error": "Failed to fetch group or breed data."}
