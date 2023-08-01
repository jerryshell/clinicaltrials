import json
import csv
import requests

id_set = set()
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


with open('cond.Castration_Resistant_Prostate_Cancer.json') as f:
    study = json.load(f)
# print(study)

study_hits = study['hits']
# print(study_hits)

with open('term.Castration_Resistant_Prostate_Cancer.json') as f:
    other_study = json.load(f)
# print(other_study)

other_study_hits = other_study['hits']
# print(other_study_hits)

study_hits += other_study_hits

# i = 100
for item in study_hits:
    # i -= 1
    # if i <= 0:
    #     break

    id = item['id']
    print(id)

    if id in id_set:
        continue

    id_set.add(id)

    study_json = get_study_json_by_id(id)
    eligibility_module = study_json['study']['protocolSection']['eligibilityModule']
    if 'eligibilityCriteria' not in eligibility_module:
        continue
    eligibility_criteria = eligibility_module['eligibilityCriteria']
    # print(eligibility_criteria)

    if str(eligibility_criteria).find('enzalutamide') == -1 and str(eligibility_criteria).find('abiraterone') == -1:
        continue

    protocol_section = item['study']['protocolSection']

    start_date = protocol_section['statusModule'].get(
        'startDateStruct', {'date': '-'}
    )['date']
    completion_date = protocol_section['statusModule'].get(
        'completionDateStruct', {'date': '-'}
    )['date']

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

    result_set.add((
        id,
        sponsor,
        start_date,
        completion_date,
        drug_list_str
    ))

with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow([
        'id',
        'sponsor',
        'start_date',
        'completion_date',
        'drug'
    ])
    write.writerows(result_set)
