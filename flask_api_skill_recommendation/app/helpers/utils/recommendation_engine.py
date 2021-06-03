import operator

def get_sorted_dictionary_based_on_skill_for_each_jobtitle(knowledge_dict):
    for i in knowledge_dict.keys():
        knowledge_dict[i]['skills'] = sorted(knowledge_dict[i]['skills'].items(), key=operator.itemgetter(1), reverse=True)
    return knowledge_dict

def get_recommendation_engine_model(final_list):
    knowledge_dict = {}
    for i in final_list:
        for jobtitle in i[0]:
            if jobtitle not in knowledge_dict.keys():
                knowledge_dict[jobtitle]={}
                knowledge_dict[jobtitle]['skills']={}
                knowledge_dict[jobtitle]['count']=1
            else:
                knowledge_dict[jobtitle]['count']+=1

            for skill in i[1]:
                if skill in knowledge_dict[jobtitle]['skills'].keys():
                    knowledge_dict[jobtitle]['skills'][skill]+=1
                else:
                    knowledge_dict[jobtitle]['skills'][skill]=1

    knowledge_dict = get_sorted_dictionary_based_on_skill_for_each_jobtitle(knowledge_dict)
    return knowledge_dict

def get_recommendation(knowledge_dict, job_title, count=10):
    if job_title in knowledge_dict.keys():
        skills = {i[0]: i[1]/knowledge_dict[job_title]['count'] for i in knowledge_dict[job_title]['skills'][:count]}
        skills = sorted(skills.items(), key=operator.itemgetter(1), reverse=True)
        count = knowledge_dict[job_title]['count']
        return {'count':count, 'skills':skills}
    else:
        raise ValueError('job_title not available in the dataset!! Try another job title')