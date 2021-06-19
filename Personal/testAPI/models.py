# utils
from utils import get
from utils import post

# typing
from typing import List

# The pandas library was added to speed up the search for the most frequent breed and the most frequent name
import pandas as pd

class Dog(object):
    """
    Dog object that is composed of the id, name and breed of the dog

    To initialize:
    :param id: dog id
    :param name: dog name
    :param breed: dog breed id

    USAGE:
        >>> dog = Dog(id=1, name='Bobby', breed=1)
    """
    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed


class Breed(object):
    """
    Breed object that is composed of the id and the name of the breed.

    To initialize:
    :param id: breed id
    :param name: breed name

    Also, breed has a list of dogs for development purposes
    :field dogs: breed dog list

    USAGE:
        >>> breed = Breed(id=1, name='Kiltro')
        >>> dog = Dog(id=1, name='Cachupin', breed=breed.id)
        >>> breed.add_dog(dog)
        >>> breed.dogs_count()
        1
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []
        self.breeds: List[Breed] = []
    
    #Method that allows adding an object of class dog
    def add_dog(self, dog: Dog):
        self.dogs.append(dog)
    
    #Method showing the total number of dogs
    def dogs_count(self) -> int:
        return len(self.dogs)
    
    #Method showing number of breeds
    def breeds_count(self) -> int:
        return len(self.breeds)
    


class DogHouse(object):
    """
    Doghouse object that manipulates information on breeds and dogs.
    We expect you implement all the methods that are not implemented
    so that the flow works correctly


    DogHouse has a list of breeds and a list of dogs.
    :field breeds: breed list
    :field dogs: dog list

    USAGE:
        >>> dog_house = DogHouse()
        >>> dog_house.get_data(token='some_token')
        >>> total_dogs = dog_house.get_total_dogs()
        >>> common_breed = dog_house.get_common_breed()
        >>> common_dog_name = dog_house.get_common_dog_name()
        >>> total_breeds = dog_house.get_total_breeds()
        >>> data = {  # add some data
        ...     'total_dogs': total_dogs,
        ...     'total_breeds': total_breeds,
        ...     'common_breed': common_breed.name,
        ...     'common_dog_name': common_dog_name,
        ... }
        >>> token = 'some token'
        >>> dog_house.send_data(data=data, token=token)
    """
    def __init__(self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

    
    def get_data(self, token: str):
        """
        You must get breeds and dogs data from our API: http://dogs.magnet.cl

        We recommend using the Dog and Breed classes to store
        the information, also consider the dogs and breeds fields
        of the DogHouse class to perform data manipulation.
        
        """
        ##URLS extracted from Dogs API (v1) reference.
        urlAPI = ['http://dogs.magnet.cl/api/v1/dogs/','http://dogs.magnet.cl/api/v1/breeds/']

        for data in urlAPI: 
            
            response = get(data,token)

            infoDogs = response['results']

            #This loop extends the data of infoDogs with the parameter 'next' ,also is contained in the references of the API for the booth url.
            while response['next']:

                response = get(response['next'],token)
                infoDogs.extend(response["results"])

            #if statement adds all the dogs elements from the list results to the list dogs initializated in the class DogHouse.
            if (urlAPI[0] == data):

                for elemento in infoDogs:

                    self.dogs.append(elemento)

            #elif statement adds all the breeds elements from the list results to the list breeds initializated in the class DogHouse. 
            elif (urlAPI[1] == data): 

                for elemento in infoDogs:
                    self.breeds.append(elemento)
                
        
        

    #Create the breeds_count method of the Breed class using the values of the dogHouse class
    def get_total_breeds(self) -> int:
        """
        Returns the amount of different breeds in the doghouse
        """
        return Breed.breeds_count(self)


    #Using the dogs_count method of the Breed class using the values of the dogHouse class
    def get_total_dogs(self) -> int:
        """
        Returns the amount of dogs in the doghouse
        """
        return Breed.dogs_count(self)


    def get_common_breed(self) -> Breed:
        """
        Returns the most common breed in the doghouse
        """
        #dog information stored in list self.dogs
        df = pd.DataFrame(self.dogs)

        #Get the most frequent breed thanks to the pandas library
        commonBread = df['breed'].value_counts().idxmax()

        #Comparison of elements in the self.breeds list with the most frequent element
        for elemento in self.breeds:

            if(elemento['id'] == commonBread):

                return  Breed(elemento.get('id'),elemento.get('name'))
    
        
    def get_common_dog_name(self) -> str:
        """
        Returns the most common dog name in the doghouse
        """
        #The information contained in the self.dogs list is sorted with the sorted function, alphabetically a ..... z
        sortedNames = sorted(self.dogs, key = lambda i: i['name'], reverse=False)

        # The ordered information is obtained and assigned to the variable df
        df = pd.DataFrame(sortedNames)

        # With the pandas library you get the most repeated name
        return df['name'].value_counts().idxmax()


    def send_data(self, data: dict, token: str):
        """
        You must send the answers obtained from the implemented
        methods, the parameters are defined in the documentation.

        Important!! We don't tell you if the answer is correct
        """
        #Send the data to the server with post method
        post('http://dogs.magnet.cl/api/v1/answer/',data,token)