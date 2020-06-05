class Room():
    def __init__(self, name, description, item_array = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item_array = item_array
    #def __str__(self):
     #   return
# Implement a class to hold room information. This should have name and
# description attributes.

    def roomItem(self, original_item):
        return f"{self.original_item}"
  
  
  
  
  
  
  
  
    def addItem(self,itemToAdd):
        self.item_array.append(itemToAdd)
        
    def __str__(self):
        return f"{self.name},{self.description},{self.item_array}"