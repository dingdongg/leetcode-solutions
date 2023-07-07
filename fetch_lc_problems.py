import os
import requests
import json

# constants
API_URL = "https://leetcode.com/graphql/"
PROBLEMS_FILE = "problems.json"

ATTR_DIFFICULTY = "difficulty"
ATTR_TITLE = "title"
ATTR_TITLE_SLUG = "titleSlug"
ATTR_ID = "frontendQuestionId"

def get_problems():
    """
    Fetch the entire list of leetcode problems via their GraphQL API
    
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

    qs_formatted = {}

    for q in questions:
        qs_formatted[ATTR_ID] = {
            ATTR_DIFFICULTY: q[ATTR_DIFFICULTY],
            ATTR_ID: q[ATTR_ID],
            ATTR_TITLE: q[ATTR_TITLE],
            ATTR_TITLE_SLUG: q[ATTR_TITLE_SLUG],
        }

    qs_json = json.dumps(qs_formatted, indent=4)

    with open(PROBLEMS_FILE, "w") as file:
        file.write(str(qs_json))
        file.close()

if __name__ == "__main__": 
    if os.stat(PROBLEMS_FILE).st_size == 0:
        get_problems()
    else:
        print("Problems previously fetched. Use the cached results.")
