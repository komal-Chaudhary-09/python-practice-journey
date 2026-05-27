class restaurant:
    def __init__(self,name,cuisine,ratings):
        self.name = name
        self.cuisine = cuisine
        self.ratings = ratings 
        
    def show_details(self):
        print("restaurant details")
        print("name:", self.name)
        print("cuisine",self.cuisine)
        print("ratings:",self.ratings)
    
    
    def order_food(self,item):
        print(item, "ordered from", self.name)
        
    def update_rating(self, new_rating):
        self.rating = new_rating
        
        print("ratings updated succesfully")
        
        
r1 = restaurant("pizza hub","italaian",4)
r2 = restaurant("spicy villa","indian",7)

r1.show_details()
r1.order_food("burger")
r1.update_rating(6)
r1.show_details()

r2.show_details()

r2.order_food("Paneer Pizza")