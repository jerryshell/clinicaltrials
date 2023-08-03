from get_study_json_by_id import *
from get_study_hits_by_query import *
from write_to_csv import *

id_set = set()
result_set = set()

query = input('Enter query\n>>> ')
print('query:', query)

keywords = input(
    'Enter keywords, multiple keywords to use , split\n>>> '
)
keywords = keywords.split(',')
print('keywords:', keywords)

study_hits = get_study_hits_by_query(query)

for item in study_hits:
    id = item['id']
    print(id)

    if id in id_set:
        continue

    id_set.add(id)

    study_json = get_study_json_by_id(id)
    eligibility_module = study_json['study']['protocolSection']['eligibilityModule']
    if 'eligibilityCriteria' not in eligibility_module:
        continue
    eligibility_criteria = str(eligibility_module['eligibilityCriteria'])
    # print(eligibility_criteria)

    find_any_keywords = False
    for keyword in keywords:
        if eligibility_criteria.find(keyword) != -1:
            find_any_keywords = True
            break
    if not find_any_keywords:
        print('not find_any_keywords')
        continue

    protocol_section = item['study']['protocolSection']

    start_date = protocol_section['statusModule'].get(
        'startDateStruct', {'date': '-'}
    )['date']
    completion_date = protocol_section['statusModule'].get(
        'completionDateStruct', {'date': '-'}
    )['date']

    sponsor = protocol_section['sponsorCollaboratorsModule']['leadSponsor']['name']

    # overallStatus
    status = protocol_section['statusModule']['overallStatus']

    # phase
    phase = protocol_section['designModule'].get('phases', ['-'])[0]

    # conditions
    conditions = protocol_section['conditionsModule'].get('conditions', ['-'])
    conditions = ','.join(conditions)

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

    # add \t for stupid excel
    id = '\t' + id
    sponsor = '\t' + sponsor
    start_date = '\t' + start_date
    completion_date = '\t' + completion_date
    status = '\t' + status
    phase = '\t' + phase
    conditions = '\t' + conditions
    drug_list_str = '\t' + drug_list_str

    result_set.add((
        id,
        sponsor,
        start_date,
        completion_date,
        status,
        phase,
        conditions,
        drug_list_str,
    ))

print('write to csv ...')
write_to_csv(result_set)
