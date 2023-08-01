import json
import csv
import requests

result_set = set()


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

with open('other.CRPC.json') as f:
    other_crpc = json.load(f)
# print(other_crpc)

other_crpc_hits = other_crpc['hits']
# print(other_crpc_hits)

crpc_hits += other_crpc_hits

for item in crpc_hits:
    id = item['id']
    print(id)

    protocol_section = item['study']['protocolSection']

    sponsor = protocol_section['sponsorCollaboratorsModule']['leadSponsor']['name']

    drug_list = []
    if 'armsInterventionsModule' in protocol_section:
        arms_interventions_module = protocol_section['armsInterventionsModule']
        if 'interventions' in arms_interventions_module:
            interventions = arms_interventions_module['interventions']
            for item in interventions:
                type = item['type']
                if type == 'DRUG':
                    drug_list.append(item['name'])
    drug_list_str = ','.join(drug_list)

    study_json = get_study_json_by_id(id)
    eligibility_module = study_json['study']['protocolSection']['eligibilityModule']
    eligibility_criteria = eligibility_module['eligibilityCriteria']
    # print(eligibility_criteria)

    if str(eligibility_criteria).find('enzalutamide') != -1 or str(eligibility_criteria).find('abiraterone') != -1:
        result_set.add((id, sponsor, drug_list_str))

with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['id', 'sponsor', 'drug'])
    write.writerows(result_set)
