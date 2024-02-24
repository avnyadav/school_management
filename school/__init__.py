from typing import List


class Room:
    doors:int=2
    window:int=4
    bench:20
    bench_seating_capacity:2


#HAS a relation because floor has a room
class Floor: #Composition
    room = Room()
    def __init__(self,n_room,floor_no) -> None:
        self.n_room=n_room
        self.floor_no=floor_no

    def ___repr__(self):
        return f"(n_room={self.n_room},floor_no={self.floor_no})"
    
    def __str__(self):
        return f"(n_room={self.n_room},floor_no={self.floor_no})"


    
#HAS a relation because Building has a floor
class Building:
    owner:str = "Ashish Yadav"
    location:str = "Malad East"
    floors:List[Floor] = [Floor(n_room=10,floor_no="Ground Floor"),
                          Floor(n_room=11,floor_no="1st Floor"),
                          Floor(n_room=8,floor_no="2nd Floor"),
                          
                          ]
    rent:float=1000000
    
    
    def __repr__(self) -> str:

        representation = ""
        for floor in Building.floors[::-1]:
            representation=f"{representation}{floor}\n"
        return representation

    def __str__(self) -> str:
        self.__repr__()
    
#IS a Relation because School is a building 
class School(Building): #Inheritance Reusability
    name:str = "Shivaji Vidya Mandir High School"
    def __repr__(self) -> str:
        return f"(Name={self.name}\nlocation={self.location})"
    



    