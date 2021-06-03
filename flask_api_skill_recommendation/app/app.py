# This application is relatively straight forward, if you have completed the first part 
# skill_recommendation_for_job_title is the pre-requisite

import pathlib
home = pathlib.Path(__file__).parent.absolute() 

from flask import Flask, jsonify, request
import os

app = Flask(__name__)

from helpers.skill_recommendor import get_skills_for_a_jobtitle
@app.route('/skill_recommendation/', methods=['GET', 'POST'])
def recommendation():
    output_list = []
    try:
        if request.method in ['GET', 'POST']:
            input_json = request.get_json()
            if input_json:
                job_title = input_json.get("job_title")
                count = input_json.get("count")
                if job_title:
                    job_title = job_title.lower()
                    output_list = get_skills_for_a_jobtitle(job_title, count)
                    return jsonify({"recommendations": output_list}), 200

    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = '5020', debug = True, threaded = True)
