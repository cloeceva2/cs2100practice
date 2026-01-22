"""
Practice with classes/ objects
"""


class CoffeeBag:
    """
    Data type for bags of coffee
    """


    def __init__(self,coffee_name:str, roast_level: str, grams: int) -> None:
        """ Initalize the bag"""
        self.coffee_name: str = coffee_name
        self.roast_level: str = roast_level
        self.grams = grams

    def __str__(self) -> str:
        """Nice readable version of the bag"""
        return f"Your bag is {self.coffee_name} it is a {self.roast_level} roast with {self.grams} grams left"
    
    def brew(self, how_many_grams: int)-> None:
        """ 
       Reduces available coffee in the bag based on brew amount

       Parameters 
       ==========
       how_many_grams: int 
            indicates how much to reduce 
            the overall grams in bag by  
        """

        if how_many_grams > self.grams:
            print(f"sorry not enough {self.coffee_name} for brew: :(")
        else:
        # longer version ---> self.grams = self.grams - how_many_grams
            self.grams -= how_many_grams

    
def main()-> None:
    """
    Running our coffee app
    """
    # current bag and fave bag 
    # are objects(or intastance) of 
    # the class CoffeeBag
    current_bag: CoffeeBag = CoffeeBag("Etheopia Bochesa Natural", "medium", 284) # self is current_bag 
    fave_bag: CoffeeBag = CoffeeBag("Weed Coffee", "light", 150) # self is fave_bag

    print(f"Current Bag: {current_bag}")
    #{current_bag.roast_level} {current_bag.grams}")
    print(f"Favorite Bag: {fave_bag}")
    #{fave_bag.roast_level} {fave_bag.grams}")
    
    print("Brew a Cup")
    current_bag.brew(15)
    print(f"Current Bag: {current_bag}")

    print("Brew a Cup")
    fave_bag.brew(1500)
    print(f"Fave Bag: {fave_bag}")

if __name__ == "__main__":
    main()