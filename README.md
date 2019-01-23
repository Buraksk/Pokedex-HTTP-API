# Pokedex API

Everyone knows Pokémon. So far 7 generations of pokémon released in last 20 years. In pokémon universe there are 18 types of these pocket monsters. 
The types are normal, fight, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, steel, fire, water, grass, electric, psychc, ice, dragon, dark, and, fairy. Each one of them has advanteges and disadvantes to others. For example; a **fire** type pokémon hits 2x to a **grass** type but hits 0.5x to a **rock** pokémon.

In this task i am going to create a Http api named **pokedex**. Data is provided by the data.json file in the same directory

### Data Format

The given json data has the following structure.

    {
        "types": [...],
        "pokemons": [...],
        "moves": [...]
    }
    
### Enter the following command at the command prompt to start pokedex api 
```
$ python pokedex.py
```

### HTTP API
  
**Get Api**

Lists the given type of pokémons. A sample output is given below. 

Output:

   ![GetTypeByID](screenshots/getType_v1.png?raw=true)
   
   
**List Api**

List by Pokémon type

Output:

   ![ListByType](screenshots/listv1.png?raw=true)
   
Sort by BaseAttack

Output:

   ![ListByType](screenshots/listv1.png?raw=true)


You can get more information about pokemonlar from http://www.pokemongodb.net/.








