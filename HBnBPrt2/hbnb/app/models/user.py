from .base import BaseModel

class User(BaseModel):
    def __init__(self, email, password, first_name="", last_name=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return base_dict