def create_user(self, user_data):
    user = User(**user_data)
    self.user_repository.add(user)
    return user

def get_place(self, place_id):
    place = self.place_repository.get(place_id)
    if place:
        place.reviews = self.review_repository.get_by_attribute('place_id', place_id)
        return place

