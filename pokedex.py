from flask import jsonify, session, abort
from flask  import Flask,request, render_template, url_for
import json,os

app = Flask(__name__)
port = int(os.getenv('PORT', 8000))

data = json.load(open('data.json'))

userDB = [
{
 'id':'1',
 'username':'buraksk',
 'password':'b3r4k'
},
{
 'id':'2',
 'username':'yusuf',
 'password':'123y'
}
]

@app.route('/', methods = ['GET'])
def hello():
   return "hello"

#handle login failed
@app.errorhandler(401)
def page_not_found(e):
    error = "you can not reach api without logging in"
    return  json.dumps({ "error": error },indent=2), 401 

@app.route("/pokedex/api/v1/get",methods = ['GET'])
def getV1():
    """if 'token' not  in session: #you can try this feature on browser
        return abort(401) """  
    type = request.args.get("type")
    return get(type) 

@app.route("/pokedex/api/v1/get/<type>",methods = ['GET'])
def getV2(type):
    #if 'token' not  in session: 
        #return abort(401)   
    return get(type) 

@app.route("/pokedex/api/v1/list",methods = ['GET'])
def list():
    #if 'token' not  in session: 
        #return abort(401)  
    type = request.args.get("type")
    sortby = request.args.get("sortby") #fetching paramaters

    size = len(data['pokemons'])
    pokemons = data['pokemons']
    response = []
    result = ""
    for i in range(size):
            item = {}
            nextEvolutions = [] # creating dictionary and list for storing reponse values 
            counter = 0
            if "Type I" in pokemons[i]:
                 tempType = pokemons[i]["Type I"]
		 tempTypeSize = len(tempType)

	         for j in range(tempTypeSize):
                     if tempType[j] == type:
                        counter = 1
                        break

  	         if (counter == 1):  #if the value matches the desired value, add new item in list 
                     item["Name"] = pokemons[i]["Name"] 
                     item["Weight"] = pokemons[i]["Weight"]
		     item["Height"] = pokemons[i]["Height"]  
                     item["BaseAttack"] = pokemons[i]["BaseAttack"]
 		     item["BaseDefense"] = pokemons[i]["BaseDefense"]
                     item["BaseStamina"] = pokemons[i]["BaseStamina"]
  		    
		     if "Next evolution(s)" in pokemons[i]:                
                         ne = pokemons[i]["Next evolution(s)"]
	                 neSize = len(pokemons[i]["Next evolution(s)"])

                         for k in range(neSize):                         
                              nextEvolutions.append(ne[k]["Name"])

                         item["Next evolutions"] = nextEvolutions
                               	
                     response.append(item)                         	  
    response = sorted(response, key=lambda k: k.get(sortby, 0), reverse=True) # sort by parameter
    # converting list to string
    for item in response:
        print item
        result += " " + str(item["Name"]) + ":\n"
        result += "\t" + "Weight: " + item["Weight"] + "\n"
        result += "\t" + "Height: " + item["Height"] + "\n"
        result += "\t" + "BaseAttack: " + str(item["BaseAttack"]) + "\n"
        result += "\t" + "BaseDefense: " + str(item["BaseDefense"]) + "\n"
        result += "\t" + "BaseStamina: " + str(item["BaseStamina"]) + "\n"
        if "Next evolutions" in item:
            result += "\t" +"Next evolutions:"+"\n"
            for ne in item["Next evolutions"]:
                result += 2*"\t" +ne+ "\n"
    return result  

def get(type):
    size = len(data['types'])

    response = ""
    for i in range(size):
        if (data["types"][i]["name"] == type):
            response += "Pekemon Type: " + type + "\n" 
            
	    response += "Effective Against:" +"\n"   
            listEA = data["types"][i]["effectiveAgainst"]
            for ea in listEA:
        	response += " -" +ea+ "\n"    
         
            response += "Weak Against:" +"\n" 
	    listWA = data["types"][i]["weakAgainst"]
	    for wa in listWA:
       		response += " -" +wa+ "\n"
           
            response += "Example Pokemons:" +"\n" 
	    listEXP = getExamplePokemons(type)
	    for exp in listEXP:
        	response += " -" +exp+ "\n"        
    return response

def getExamplePokemons(type):
    size = len(data['pokemons'])
    pokemons = data['pokemons']
    exPokemons = []
    counter = 0
    for i in range(size):         
            if "Type I" in pokemons[i]:
                 tempType = pokemons[i]["Type I"]
		 tempTypeSize = len(tempType)
	         for j in range(tempTypeSize):
                     if tempType[j] == type:
                        exPokemons.append(pokemons[i]["Name"])
 			counter = 1
                        break
            if counter != 1:
               if "Type II" in pokemons[i]:
                 tempType = pokemons[i]["Type I"]
		 tempTypeSize = len(tempType)
	         for j in range(tempTypeSize):
                     if tempType[j] == type:
                        exPokemons.append(pokemons[i]["Name"])
 			counter = 1
                        break
	    counter = 0
    return exPokemons


@app.route("/pokedex/api/v1/Authenticate",methods = ['GET']) #authentication for accessing 
def Authenticate():
    username = request.args.get('username')
    password = request.args.get('password')
    print username
    print password
    user = [usr for usr in userDB if (usr['username'] == username and usr['password'] == password)]
    print user
    if len(user) > 0:
         session['token'] = "success"
         return "Logged in succesfully"+"\n"
    else:
         return  "Username or Password is wrong"

if __name__ == "__main__":
   app.secret_key = 'cxyy4i3x2'
   app.debug = True
   app.run(host='0.0.0.0', port=port, debug=True)#app.run()


