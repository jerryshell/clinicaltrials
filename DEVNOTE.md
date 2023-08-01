```
https://www.clinicaltrials.gov/api/int/studies?query.cond=CRPC&agg.synonyms=true&aggFilters=&checkSpell=true&from=0&limit=500&fields=OverallStatus%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true
```

```
https://www.clinicaltrials.gov/api/int/studies?query.term=CRPC&agg.synonyms=true&aggFilters=&checkSpell=true&from=0&limit=1000&fields=OverallStatus%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true
```

```
https://www.clinicaltrials.gov/api/int/studies?query.cond=Castration%20Resistant%20Prostate%20Cancer&agg.synonyms=true&aggFilters=&checkSpell=true&from=0&limit=2000&fields=OverallStatus%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true
```

```
https://www.clinicaltrials.gov/api/int/studies?query.term=Castration%20Resistant%20Prostate%20Cancer&agg.synonyms=true&aggFilters=&checkSpell=true&from=0&limit=2000&fields=OverallStatus%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true
```

```bash
curl 'https://www.clinicaltrials.gov/api/int/studies/NCT03690141?query.cond=CRPC&history=true' \
  -H 'authority: www.clinicaltrials.gov' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'dnt: 1' \
  -H 'if-none-match: "bfbfda5/0.22.3/lkmygwxt-gzip"' \
  -H 'referer: https://www.clinicaltrials.gov/study/NCT03690141?cond=CRPC&rank=1' \
  -H 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
  --compressed
```

```json
{
    "study": {
        "protocolSection": {
            "identificationModule": {
                "nctId": "NCT03690141",
                "orgStudyIdInfo": {
                    "id": "eFT508-0009"
                },
                "organization": {
                    "fullName": "Effector Therapeutics",
                    "class": "INDUSTRY"
                },
                "briefTitle": "An Open-label Study Examining the Effect of Tomivosertib (eFT508) in Patients With Advanced Castrate-resistant Prostate Cancer (<mark class=\"hl-term\">CRPC</mark>)",
                "officialTitle": "A Phase 2 Non-randomized Open-label Study Examining the Effect of Tomivosertib (eFT508) in Patients With Advanced Castrate-resistant Prostate Cancer (<mark class=\"hl-term\">CRPC</mark>)"
            },
            "statusModule": {
                "statusVerifiedDate": "2020-04",
                "overallStatus": "COMPLETED",
                "expandedAccessInfo": {
                    "hasExpandedAccess": false
                },
                "startDateStruct": {
                    "date": "2018-10-12",
                    "type": "ACTUAL"
                },
                "primaryCompletionDateStruct": {
                    "date": "2020-04-27",
                    "type": "ACTUAL"
                },
                "completionDateStruct": {
                    "date": "2020-04-27",
                    "type": "ACTUAL"
                },
                "studyFirstSubmitDate": "2018-09-10",
                "studyFirstSubmitQcDate": "2018-09-27",
                "studyFirstPostDateStruct": {
                    "date": "2018-10-01",
                    "type": "ACTUAL"
                },
                "lastUpdateSubmitDate": "2020-04-27",
                "lastUpdatePostDateStruct": {
                    "date": "2020-04-28",
                    "type": "ACTUAL"
                }
            },
            "sponsorCollaboratorsModule": {
                "responsibleParty": {
                    "type": "SPONSOR"
                },
                "leadSponsor": {
                    "name": "Effector Therapeutics",
                    "class": "INDUSTRY"
                }
            },
            "oversightModule": {
                "oversightHasDmc": true,
                "isFdaRegulatedDrug": true,
                "isFdaRegulatedDevice": false
            },
            "descriptionModule": {
                "briefSummary": "<p>This Phase 2 Open-label Study examines the efficacy, safety, tolerability, and pharmacokinetics (PK) of tomivosertib (eFT508) in Patients with advanced CRPC.</p><p>An Open-label Study Examining the Effect of tomivosertib (eFT508) in Patients with Advanced Castrate-resistant Prostate Cancer (CRPC)</p>",
                "detailedDescription": "This Phase 2 study examines the efficacy, safety, tolerability, and pharmacokinetics (PK) of tomivosertib (eFT508) in advanced CRPC patients who have documented PSA progression on treatment with apalutamide and&#x2F;or abiraterone and&#x2F;or enzalutamide and for whom no suitable curative therapy exists."
            },
            "conditionsModule": {
                "conditions": [
                    "Castrate-resistant Prostate Cancer (<mark class=\"hl-term\">CRPC</mark>)"
                ],
                "keywords": [
                    "Prostate Cancer",
                    "Castrate-resistant Prostate Cancer",
                    "<mark class=\"hl-term\">CRPC</mark>",
                    "eFT508",
                    "eFT508-0009",
                    "tomivosertib"
                ]
            },
            "designModule": {
                "studyType": "INTERVENTIONAL",
                "phases": [
                    "PHASE2"
                ],
                "designInfo": {
                    "allocation": "NA",
                    "interventionModel": "SINGLE_GROUP",
                    "interventionModelDescription": "tomivosertib (eFT508) will be supplied as 100-mg capsules by the Sponsor.\nCapsules are packaged in 200-cc high-density polyethylene wide-mouth, round, white bottles, at either 100 or 150 units per bottle, induction sealed and capped with a 38-mm child-resistant closure.",
                    "primaryPurpose": "TREATMENT",
                    "maskingInfo": {
                        "masking": "NONE"
                    }
                },
                "enrollmentInfo": {
                    "count": 16,
                    "type": "ACTUAL"
                }
            },
            "armsInterventionsModule": {
                "armGroups": [
                    {
                        "label": "tomivosertib (eFT508)",
                        "type": "EXPERIMENTAL",
                        "description": "Tomivosertib (eFT508) is a novel small-molecule, investigational drug being developed by eFFECTOR Therapeutics, Inc. as an anticancer therapy.\nTomivosertib (eFT508) down regulates AR and acts by inhibiting mitogen-activated protein kinase-interacting serine&#x2F;threonine kinase-1 (MNK1) and MNK2.",
                        "interventionNames": [
                            "Drug: tomivosertib (eFT508)"
                        ]
                    }
                ],
                "interventions": [
                    {
                        "type": "DRUG",
                        "name": "tomivosertib (eFT508)",
                        "description": "This Phase 2 study examines the efficacy, safety, tolerability, and PK of tomivosertib (eFT508) in advanced CRPC patients who have documented PSA progression on treatment with apalutamide and&#x2F;or abiraterone and&#x2F;or enzalutamide and for whom no suitable curative therapy exists.",
                        "armGroupLabels": [
                            "tomivosertib (eFT508)"
                        ]
                    }
                ]
            },
            "outcomesModule": {
                "primaryOutcomes": [
                    {
                        "measure": "Anti-tumor response as defined by a patient achieving either of the following outcomes:",
                        "description": "<ul><li>A ≥50% PSA decline from baseline at any time point after therapy and maintained for ≥4 weeks</li><li>Objective response according to iRECIST 1.1</li></ul>",
                        "timeFrame": "52 weeks"
                    }
                ],
                "secondaryOutcomes": [
                    {
                        "measure": "PSA progression-free survival from start of study therapy until the date PSA progression is first observed.",
                        "description": "PSA progression is defined as a ≥25% increase in PSA from nadir or baseline (and by ≥2 ng&#x2F;mL) and requires confirmation ≥3 weeks later.",
                        "timeFrame": "52 weeks"
                    }
                ]
            },
            "eligibilityModule": {
                "eligibilityCriteria": "<p>Inclusion Criteria:</p><ul><li>Men ≥18 years.</li><li>Eastern Cooperative Oncology Group (ECOG) performance status of 0, 1, or 2.</li><li>Histologically or cytologically confirmed (by clinical site) adenocarcinoma of the prostate without neuroendocrine differentiation or small cell features.</li><li>Ongoing androgen deprivation therapy with a GnRH analog or bilateral orchiectomy (surgical or medical castration).</li><li>Serum testosterone ≤1.73 nmol&#x2F;L (50 ng&#x2F;dL) at screening.</li><li><p>PSA progression on treatment with abiraterone and&#x2F;or enzalutamide and&#x2F;or apalutamide.\nPSA progression is defined by a minimum of 2 rising PSA levels with an interval of ≥1 week between each determination.\nPSA value at the screening visit should be ≥2 ng&#x2F;mL.\nPatients may also have:</p><ul><li>Soft tissue disease progression defined by iRECIST&#x2F;RECIST 1.1</li><li>Bone disease</li></ul></li><li>Patients receiving bisphosphonate&#x2F;receptor activator of nuclear factor kappa-Β ligand (RANKL) therapy must have been on stable doses for ≥ 4 weeks before the start of study therapy.</li><li>Completion of all previous therapy for the treatment of cancer ≥4 weeks before the start of study therapy.</li><li>All acute toxic effects of any prior anti-tumor therapy resolved to Grade ≤1 before the start of study therapy (with the exception of alopecia [Grade 1 or 2 permitted], neurotoxicity [Grade 1 or 2 permitted], or bone marrow parameters [Grade 1 or 2 permitted with exceptions as noted below]).</li><li><p>Adequate bone marrow function:</p><ul><li>Absolute neutrophil count (ANC) ≥1.0 x 109&#x2F;L</li><li>Platelet count ≥75 x 109&#x2F;L</li><li>Hemoglobin ≥80 g&#x2F;L (8.0 g&#x2F;dL or 4.9 mmol&#x2F;L)</li></ul></li><li><p>Adequate hepatic function:</p><ul><li>Serum alanine aminotransferase (ALT) ≤3 x upper limit of normal (ULN), ≤ 5 x ULN in the presence of liver metastases</li><li>Serum aspartate aminotransferase (AST) ≤3 x ULN, ≤5 x ULN in presence of liver metastases</li><li>Serum bilirubin ≤1.5 x ULN (unless due to Gilbert&#x27;s syndrome or hemolysis ≤3 x ULN)</li></ul></li><li><p>Adequate renal function:</p><p>-Serum creatinine ≤1.5 mg&#x2F;dL and&#x2F;or creatinine clearance ≥30 mL&#x2F;min using Cockcroft Gault equation (Appendix 13.4)</p></li><li>For male patients who can father a child and are having intercourse with females of childbearing potential, willingness to use a protocol-recommended method of contraception from the start of study therapy and for ≥30 days following the last dose of study medication or to abstain from sexual intercourse for at least this period of time, and willingness to refrain from sperm donation from the start of study therapy to ≥90 days following the last dose of study drug.</li><li>Estimated life expectancy &gt;12 weeks.</li><li>Willingness to comply with scheduled visits, drug administration plan, protocol-specified laboratory tests and biopsies, other study procedures, and study restrictions.\nNote: Psychological, social, familial, or geographical factors that might preclude adequate study participation should be considered.</li><li>Evidence of a personally signed informed consent indicating that the patient is aware of the neoplastic nature of the disease and has been informed of the procedures to be followed, the experimental nature of the therapy, alternatives, potential benefits, possible side effects, potential risks and discomforts, and other pertinent aspects of study participation.</li></ul><p>Exclusion Criteria:</p><ul><li>History of another malignancy except for the following: adequately treated local basal cell or squamous cell carcinoma of the skin; adequately treated, papillary, noninvasive bladder cancer; other adequately treated Stage 1 or 2 cancers currently in complete remission, or any other cancer that has been in complete remission for ≥2 years.</li><li>Rapidly progressive, clinically unstable central nervous system malignancy.\nNote: Central nervous system imaging is only required in patients with known or suspected central nervous system malignancy.</li><li>Significant cardiovascular disease, including myocardial infarction, arterial thromboembolism, or cerebrovascular thromboembolism within 6 months before the start of study therapy; symptomatic dysrhythmias or unstable dysrhythmias requiring medical therapy; unstable angina; symptomatic peripheral vascular disease; New York Heart Association Class 3 or 4 congestive heart failure; Grade ≥3 hypertension (diastolic blood pressure ≥100 mmHg or systolic blood pressure ≥160 mmHg), or history of congenital prolonged QT syndrome.</li><li>Significant screening electrocardiogram (ECG) abnormalities, including unstable cardiac arrhythmia requiring medication, left bundle-branch block, 2nd-degree atrioventricular (AV) block type II, 3rd-degree AV block, Grade ≥2 bradycardia, or QTcF ≥470 msec.</li><li>Symptomatic or impending cord compression unless appropriately treated beforehand and clinically stable.</li><li>Patients with gastrointestinal disorders likely to interfere with absorption of study medication.</li><li>Major surgery within 4 weeks before the start of study therapy.</li><li>Prior treatment with chemotherapy within 3 weeks or at least 4 half-lives, whichever is longer, before the start of study therapy.</li><li>Prior therapy with any known inhibitor of MNK-1 or MNK-2.</li><li>Treatment with 5-alpha reductase inhibitors within 4 weeks of enrollment.</li><li>Prior flutamide treatment within 4 weeks before the start of study therapy and evidence of withdrawal response.</li><li>Bicalutamide or nilutamide within 6 weeks before the start of study therapy and evidence of withdrawal response.</li><li><p>Enzalutamide or abiraterone or apalutamid within 4 weeks before the start of study therapy.</p><p>a. Steroids given in conjunction with abiraterone must be washed out for at least 2 weeks prior to Cycle 1 Day 1 unless the investigator chooses to maintain at a dose of ≤10 mg&#x2F;day prednisone or equivalent.</p></li><li>Use of herbal products that may have hormonal anti-prostate cancer activity and&#x2F;or are known to decrease PSA levels (eg, saw palmetto).</li><li><p>Current use of immunosuppressive medication at the time of randomization, EXCEPT for the following:</p><ol><li>intranasal, inhaled, topical steroids, or local steroid injection (eg, intra-articular injection);</li><li>Systemic corticosteroids at physiologic doses ≤10 mg&#x2F;day of prednisone or equivalent;</li><li>Steroids as premedication for hypersensitivity reactions (eg, computed tomography [CT] scan premedication).</li></ol></li><li>Use of a potent inhibitor or inducer of cytochrome P450 (CYP) 3A4 within 7 days before the start of study therapy or expected requirement for use of a CYP3A4 inhibitor or inducer during study therapy (Appendix 13.5).</li><li>Concurrent participation in another therapeutic clinical trial.</li><li>Any illness, medical condition, organ system dysfunction, or social situation, including mental illness or substance abuse, deemed by the investigator to be likely to interfere with a patient&#x27;s ability to sign informed consent, adversely affect the patient&#x27;s ability to cooperate and participate in the study, or compromise the interpretation of study results.</li></ul>",
                "healthyVolunteers": false,
                "sex": "MALE",
                "genderBased": true,
                "minimumAge": "18 Years",
                "stdAges": [
                    "ADULT",
                    "OLDER_ADULT"
                ]
            },
            "contactsLocationsModule": {
                "overallOfficials": [
                    {
                        "name": "Lyon Gliech, MD",
                        "affiliation": "Medpace, Inc.",
                        "role": "STUDY_DIRECTOR"
                    }
                ],
                "locations": [
                    {
                        "facility": "Yale Cancer Center",
                        "city": "New Haven",
                        "state": "Connecticut",
                        "zip": "06510",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 41.30815,
                            "lon": -72.92816
                        }
                    },
                    {
                        "facility": "Northwestern University",
                        "city": "Chicago",
                        "state": "Illinois",
                        "zip": "60611",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 41.85003,
                            "lon": -87.65005
                        }
                    },
                    {
                        "facility": "Kimmel Center at Johns Hopkins",
                        "city": "Baltimore",
                        "state": "Maryland",
                        "zip": "21205",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 39.29038,
                            "lon": -76.61219
                        }
                    },
                    {
                        "facility": "Karmanos Cancer Institute",
                        "city": "Detroit",
                        "state": "Michigan",
                        "zip": "48201",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 42.33143,
                            "lon": -83.04575
                        }
                    },
                    {
                        "facility": "Washington University",
                        "city": "Saint Louis",
                        "state": "Missouri",
                        "zip": "63110",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 38.62727,
                            "lon": -90.19789
                        }
                    },
                    {
                        "facility": "Comprehensive Cancer Centers of Nevada",
                        "city": "Las Vegas",
                        "state": "Nevada",
                        "zip": "89169",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 36.17497,
                            "lon": -115.13722
                        }
                    },
                    {
                        "facility": "The Urology Group",
                        "city": "Cincinnati",
                        "state": "Ohio",
                        "zip": "45212",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 39.12713,
                            "lon": -84.51435
                        }
                    },
                    {
                        "facility": "Lancaster Urology",
                        "city": "Lancaster",
                        "state": "Pennsylvania",
                        "zip": "17604",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 40.03788,
                            "lon": -76.30551
                        }
                    },
                    {
                        "facility": "Carolina Urologic Research Center",
                        "city": "Myrtle Beach",
                        "state": "South Carolina",
                        "zip": "29572",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 33.68906,
                            "lon": -78.88669
                        }
                    },
                    {
                        "facility": "University of Washington",
                        "city": "Seattle",
                        "state": "Washington",
                        "zip": "89109",
                        "country": "United States",
                        "geoPoint": {
                            "lat": 47.60621,
                            "lon": -122.33207
                        }
                    }
                ]
            },
            "ipdSharingStatementModule": {
                "ipdSharing": "NO"
            }
        },
        "derivedSection": {
            "miscInfoModule": {
                "versionHolder": "2023-07-28",
                "modelPredictions": {
                    "bmiLimits": {
                        "minBmi": 0.0,
                        "maxBmi": 101.0
                    }
                }
            },
            "conditionBrowseModule": {
                "meshes": [
                    {
                        "id": "D000011471",
                        "term": "Prostatic Neoplasms"
                    }
                ],
                "ancestors": [
                    {
                        "id": "D000005834",
                        "term": "Genital Neoplasms, Male"
                    },
                    {
                        "id": "D000014565",
                        "term": "Urogenital Neoplasms"
                    },
                    {
                        "id": "D000009371",
                        "term": "Neoplasms by Site"
                    },
                    {
                        "id": "D000009369",
                        "term": "Neoplasms"
                    },
                    {
                        "id": "D000005832",
                        "term": "Genital Diseases, Male"
                    },
                    {
                        "id": "D000091662",
                        "term": "Genital Diseases"
                    },
                    {
                        "id": "D000091642",
                        "term": "Urogenital Diseases"
                    },
                    {
                        "id": "D000011469",
                        "term": "Prostatic Diseases"
                    },
                    {
                        "id": "D000052801",
                        "term": "Male Urogenital Diseases"
                    }
                ],
                "browseLeaves": [
                    {
                        "id": "M14025",
                        "name": "Prostatic Neoplasms",
                        "asFound": "Prostate Cancer",
                        "relevance": "HIGH"
                    },
                    {
                        "id": "M8636",
                        "name": "Genital Neoplasms, Male",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M17005",
                        "name": "Urogenital Neoplasms",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M2877",
                        "name": "Genital Diseases",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M8634",
                        "name": "Genital Diseases, Male",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M2876",
                        "name": "Urogenital Diseases",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M14023",
                        "name": "Prostatic Diseases",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M26785",
                        "name": "Male Urogenital Diseases",
                        "relevance": "LOW"
                    }
                ],
                "browseBranches": [
                    {
                        "abbrev": "BC04",
                        "name": "Neoplasms"
                    },
                    {
                        "abbrev": "BXS",
                        "name": "Urinary Tract, Sexual Organs, and Pregnancy Conditions"
                    },
                    {
                        "abbrev": "All",
                        "name": "All Conditions"
                    }
                ]
            },
            "interventionBrowseModule": {
                "browseLeaves": [
                    {
                        "id": "M11590",
                        "name": "Mitogens",
                        "relevance": "LOW"
                    },
                    {
                        "id": "M5953",
                        "name": "Coal Tar",
                        "relevance": "LOW"
                    },
                    {
                        "id": "T18",
                        "name": "Serine",
                        "relevance": "LOW"
                    },
                    {
                        "id": "T20",
                        "name": "Threonine",
                        "relevance": "LOW"
                    }
                ],
                "browseBranches": [
                    {
                        "abbrev": "All",
                        "name": "All Drugs and Chemicals"
                    },
                    {
                        "abbrev": "Derm",
                        "name": "Dermatologic Agents"
                    },
                    {
                        "abbrev": "AA",
                        "name": "Amino Acids"
                    }
                ]
            }
        },
        "hasResults": false
    },
    "topics": {
        "GHR": [
            {
                "name": "Prostate cancer",
                "url": "https://medlineplus.gov/genetics/condition/prostate-cancer"
            }
        ],
        "MedlinePlus": [
            {
                "name": "Prostate Cancer",
                "url": "https://medlineplus.gov/prostatecancer.html"
            }
        ]
    },
    "history": {
        "changes": [
            {
                "version": 0,
                "date": "2018-09-27",
                "status": "NOT_YET_RECRUITING",
                "moduleLabels": []
            },
            {
                "version": 1,
                "date": "2018-10-16",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 2,
                "date": "2018-11-15",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Study Identification",
                    "Conditions",
                    "Study Design",
                    "Arms and Interventions",
                    "Contacts/Locations",
                    "Study Description"
                ]
            },
            {
                "version": 3,
                "date": "2018-11-16",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 4,
                "date": "2018-12-11",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 5,
                "date": "2019-01-18",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Study Identification",
                    "Study Description",
                    "Arms and Interventions",
                    "Outcome Measures",
                    "Eligibility",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 6,
                "date": "2019-01-22",
                "status": "RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 7,
                "date": "2019-07-16",
                "status": "ACTIVE_NOT_RECRUITING",
                "moduleLabels": [
                    "Study Status",
                    "Study Design",
                    "Contacts/Locations"
                ]
            },
            {
                "version": 8,
                "date": "2019-12-04",
                "status": "ACTIVE_NOT_RECRUITING",
                "moduleLabels": [
                    "Study Status"
                ]
            },
            {
                "version": 9,
                "date": "2020-04-27",
                "status": "COMPLETED",
                "moduleLabels": [
                    "Study Status"
                ]
            }
        ],
        "originalData": {
            "primaryOutcomes": [
                {
                    "measure": "Anti-tumor response as defined by a patient achieving either of the following outcomes:",
                    "description": "<ul><li>A ≥50% PSA decline from baseline at any time point after therapy and maintained for ≥4 weeks</li><li>Objective response according to RECIST 1.1</li></ul>",
                    "timeFrame": "52 weeks"
                }
            ],
            "secondaryOutcomesSame": true,
            "enrollmentInfo": {
                "count": 30,
                "type": "ESTIMATED"
            },
            "orgFullNameSame": true,
            "responsiblePartySame": true,
            "leadSponsorSame": true
        },
        "lastUpdateVersions": {
            "outcomes": 5,
            "primaryOutcomes": 5,
            "secondaryOutcomes": 0,
            "enrollmentInfo": 7
        },
        "outcomesUpdateCount": 1
    }
}
```
