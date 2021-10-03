import requests
from flask_restful import Resource

class LeetcodeProblems(Resource):
  def run_query(self, query, variables): # A simple function to use requests.post to make the API call. Note the json= section.
      request = requests.post('https://leetcode.com/graphql', json={'query': query, 'variables': variables})
      if request.status_code == 200:
          return request.json()
      else:
          raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

  def get(self):
    # The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        questions: data {
          title
          titleSlug
        }
      }
    }
    """

    variables = {
      "categorySlug": "",
      "skip": 0,
      "limit": 100000,
      "filters": {}
    }

    return self.run_query(query, variables)