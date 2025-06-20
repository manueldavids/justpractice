from .base import BaseModel

class Place(BaseModel):
    def __init__(self, name, description="", price=0, user_id=""):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'user_id': self.user_id
        })
        return base_dict