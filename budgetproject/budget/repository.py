from python_graphql_client import GraphqlClient

class MembershipsRepository:
    def __init__(self):
        headers = {
            "content-type": "application/json",
            "apollographql-client-name": "playground",
            "apollographql-client-version": "1.0",
        }
        self.gql_client = GraphqlClient(endpoint="https://www.prodigygame.net/graphql/", headers=headers)
    
    def get_grades():
        # Create the query string and variables required for the request.
        query = """
            query FIND_GRADE ($id: ID!) {
                grade(id: $id) {
                    name
                }
            }
        """
        variables = { "id": 1 }

        # Synchronous request
        response = self.gql_client.execute(query=query, variables=variables)

        data = response.get("data")
        return data