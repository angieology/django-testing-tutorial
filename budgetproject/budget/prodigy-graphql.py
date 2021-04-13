
from python_graphql_client import GraphqlClient

headers = {
        "content-type": "application/json",
        "apollographql-client-name": "playground",
        "apollographql-client-version": "1.0",
    }

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://www.prodigygame.net/graphql/", headers=headers)

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
data = client.execute(query=query, variables=variables)
print(data) 

