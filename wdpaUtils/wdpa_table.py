from .viewer import show

class ProtectedAreas:
    """
    This class represents the current WDPA table pulled from Protected Planet.

    Add the parameters you can pass
    name:str
        Vizzuality name
    role: str
        Vizzuality role
    """
    def __init__(self, name=None, role='No role'):
        if not name: print('No name provided :(')
        if not role: print('No role provided :(')

        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} is a string"

    def __repr__(self):
        return self.__str__()

    # def change_role(self,new_role):
