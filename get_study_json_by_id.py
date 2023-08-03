import requests
import json


def get_study_json_by_id(id: str):
    url = 'https://www.clinicaltrials.gov/api/int/studies/' + id
    # print(url)

    response = requests.get(url)
    response_text = response.text
    # print(response_text)

    study_json = json.loads(response_text)
    # print(study_json)

    return study_json
