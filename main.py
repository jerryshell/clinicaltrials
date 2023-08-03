from get_study_json_by_id import *
from get_study_hits_by_query import *
from write_to_csv import *

query = input('---\nEnter query\n>>> ')
print('query:', query)

keywords = input(
    '---\nEnter keywords, multiple keywords to use , split\n>>> '
)
keywords = keywords.split(',')
print('keywords:', keywords)

keywords_in_inclusion = input(
    '---\nkeywords in Inclusion Criteria? (yes/no)\n>>> '
)
keywords_in_inclusion = keywords_in_inclusion.lower() == 'yes'
print('keywords_in_inclusion:', keywords_in_inclusion)

keywords_in_exclusion = input(
    '---\nkeywords in Exclusion Criteria? (yes/no)\n>>> '
)
keywords_in_exclusion = keywords_in_exclusion.lower() == 'yes'
print('keywords_in_exclusion:', keywords_in_exclusion)

keywords_in_conditions = input(
    '---\nkeywords in Conditions? (yes/no)\n>>> '
)
keywords_in_conditions = keywords_in_conditions.lower() == 'yes'
print('keywords_in_conditions:', keywords_in_conditions)

print('searching ...')
study_hits = get_study_hits_by_query(query)

id_set = set()
result_set = set()

for item in study_hits:
    add_to_result_set_flag = False

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

    eligibility_criteria_split = eligibility_criteria.split(
        'Exclusion Criteria:'
    )
    if len(eligibility_criteria_split) == 2:
        inclusion_criteria = eligibility_criteria_split[0]
        exclusion_criteria = eligibility_criteria_split[1]
    else:
        inclusion_criteria = eligibility_criteria
        exclusion_criteria = ''

    if keywords_in_inclusion:
        match_any_keywords = any(
            [inclusion_criteria.find(keyword) != -1 for keyword in keywords]
        )
        add_to_result_set_flag = add_to_result_set_flag or match_any_keywords

    if keywords_in_exclusion:
        match_any_keywords = any(
            [exclusion_criteria.find(keyword) != -1 for keyword in keywords]
        )
        add_to_result_set_flag = add_to_result_set_flag or match_any_keywords

    protocol_section = study_json['study']['protocolSection']

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
    if keywords_in_conditions:
        match_any_keywords = any(
            [conditions.find(keyword) != -1 for keyword in keywords]
        )
        add_to_result_set_flag = add_to_result_set_flag or match_any_keywords

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

    print('match: ', add_to_result_set_flag)
    if add_to_result_set_flag:
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
