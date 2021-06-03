'''
app.py is the entry point for all the applications

'''

import pathlib
home = pathlib.Path(__file__).parent.absolute() 
# This home is the absolute path to the root which is the folder where we have app.py file

from helpers.json_reader import get_json_file_data
from helpers.recommendation_engine import get_recommendation_engine_model, get_recommendation

# training the model only if trained model is not already present in helpers directory
from pathlib import Path
model_file = Path(str(home) + '/helpers/model.json')

if not model_file.exists():
    input_data = get_json_file_data(str(home) + '/helpers/linkedin_profile_data.json')
    try:
        model = get_recommendation_engine_model(input_data)
    except Exception as e:
        raise ValueError('Model traning failure and error is: ', e)
    
    print('Model training completed!!')
    # Since we know, here the model is dictionary data, we can store in json file
    # saving a json file 
    import json
    with open('model.json', 'w') as f:
        json.dump(model, f)
    print('Model saved successfully!!')
else:
    print('Model already available!!')
    model = get_json_file_data(str(home) + '/helpers/model.json')


job_title = input('What is the job title? ')
skills_number = input('How many skills to display? ')

try:
    skills_number = int(skills_number)
except ValueError():
    print('Number of skills to display should be an integer, displaying 10 skills')

print(get_recommendation(model, job_title, skills_number))