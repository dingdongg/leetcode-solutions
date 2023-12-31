import os
import requests
import json

# constants
API_URL = "https://leetcode.com/graphql/"
QUESTIONS_FILE = "questions.json"

ATTR_DIFFICULTY = "difficulty"
ATTR_TITLE = "title"
ATTR_TITLE_SLUG = "titleSlug"
ATTR_ID = "frontendQuestionId"

def fetch_questions():
    """
    Fetch the entire list of leetcode questions via their GraphQL API
    and cache results to a local `json` file
    """
    res = requests.post(API_URL, json = {
        'query': '''
            query problemsetQuestionList(
                $categorySlug:String,
                $limit:Int,
                $skip:Int,
                $filters:QuestionListFilterInput
            ) {
                problemsetQuestionList:questionList(
                    categorySlug:$categorySlug 
                    limit:$limit 
                    skip:$skip 
                    filters:$filters
                ) {
                    total:totalNum 
                    questions:data {
                        questionId
                        difficulty 
                        frontendQuestionId:questionFrontendId 
                        title 
                        titleSlug 
                    }
                }
            }
        ''',
        'variables': {
            'categorySlug': '',
            'skip': 0,
            'limit': -1,
            'filters': {},
        },
    })

    results = res.json()
    questions = results['data']['problemsetQuestionList']['questions']

    # dummy object to prevent headaches from 0-based indexing in ./add_soln.sh
    qs_formatted = [{}] 

    for q in questions:
        qs_formatted.append({
            ATTR_DIFFICULTY: q[ATTR_DIFFICULTY],
            ATTR_ID: q[ATTR_ID],
            ATTR_TITLE: q[ATTR_TITLE],
            ATTR_TITLE_SLUG: q[ATTR_TITLE_SLUG],
        })

    qs_json = json.dumps(qs_formatted, indent=4)

    with open(QUESTIONS_FILE, "w") as file:
        file.write(qs_json)
        file.close()

if __name__ == "__main__": 
    if os.stat(QUESTIONS_FILE).st_size == 0:
        fetch_questions()
    else:
        print("Questions previously fetched. Use the cached results.")
