
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{

            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age":33,
            "lucky_numbers":[7,13,22]
        },
        {

            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age":35,
            "lucky_numbers":[10,14,3]
        },

        {

            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age":5,
            "lucky_numbers":[1]
        }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, first_name,age,lucky_numbers):
    
        new_member = {
            "first_name": first_name,
            "last_name": self.last_name,
            "age":age,
            "lucky_numbers":lucky_numbers,
            "id": self._generateId()
        }

        self._members.append(new_member)


        return "member added"
        

    def delete_member(self, id):
      
        self._members = list(filter(lambda item: item['id'] != id , self._members))
        
        return "done"

    def get_member(self, id):
    
        member = list(filter(lambda item: item['id'] == id , self._members))
        return member


    def get_all_members(self): 
        return list(map(lambda item: [item["first_name"],item["id"]], self._members))
