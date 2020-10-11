import json
from flask import Flask
from flask import jsonify, make_response, request

app = Flask(__name__)
#app.config["DEBUG"] = True

# Get JSON Data
continentsFile = open ('geodata/continents.json', "r") 
continentsData = json.loads(continentsFile.read()) 
countriesFile = open ('geodata/countries.json', "r") 
countriesData = json.loads(countriesFile.read()) 

headers = {"Content-Type": "application/json"}

# Continents
@app.route('/api/continents', methods=['GET'])
def viewContinents():
  response = make_response(
    jsonify(
      continentsData
    ),
    200,
    headers
  )
  return response

# Countries
@app.route('/api/countries/<continentCode>', methods=['GET'])
def viewCountries(continentCode):
  results = [x for x in countriesData if x['continentCode'] == continentCode]  
  results_json = json.dumps(results)
  response = make_response(
    results_json,
    200,
    headers
  )
  return response

# Main
if __name__ == '__main__':
  app.run()