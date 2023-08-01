import json
import requests


def get_study_json_by_id(id: str):
    url = 'https://www.clinicaltrials.gov/api/int/studies/' + id
    # print(url)

    response = requests.get(url)
    response_text = response.text
    # print(response_text)

    study_json = json.loads(response_text)
    # print(study_json)

    return study_json


with open('CRPC.json') as f:
    crpc = json.load(f)
# print(crpc)

crpc_hits = crpc['hits']
# print(crpc_hits)

for item in crpc_hits:
    id = item['id']
    # print(id)

    study_json = get_study_json_by_id(id)
    eligibility_module = study_json['study']['protocolSection']['eligibilityModule']
    eligibility_criteria = eligibility_module['eligibilityCriteria']
    # print(eligibility_criteria)

    if str(eligibility_criteria).find('enzalutamide') != -1 or str(eligibility_criteria).find('abiraterone') != -1:
        print(id)
