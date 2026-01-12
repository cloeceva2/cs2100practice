"""
TODO: A very useful temperature-conversion app.
"""

THRESHOLD_TEMP_F == 68

def is_cold_f(temp_f: float)-> bool:
  """
   Determines if the suppiled
   temp in F is below out r agreeded upon temp 


   Parameters
   ==========
    temp_f : float 
        supplied temp in F 

   Returns 
   =========
    bool
        true means below the 
        agreeded upon threshold 
   """
   return temp_f < 68

#print("hello world!")


def greet_person() -> None:
 '''
 gets the name of the person 
 from the keyboard and greets them 
 '''
 your_name: str = input("what is your name")
 print(f"howdy, {your_name}")

def main() -> None:
    pass
 
if __name__ == "__main__":
    main()


