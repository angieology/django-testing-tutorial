from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://graphql.bitquery.io/CUAEuPFx2m")

# Create the query string and variables required for the request.
query = """
  query(
  $from: ISO8601DateTime, 
  $till: ISO8601DateTime,
){
  ethereum {
    smartContractEvents(
      options: {desc: "date.date"},
      ##smartContractEvent: {is: "NameRegistered"},
      smartContractAddress: 
      {is: "0x00000000219ab540356cbb839cbe05303d7705fa"}
      date: {since: $from, till: $till}, 

    ) {
      date{
         date:startOfInterval(unit:day)
      }
      smartContractEvent{
        __typename
        name
      }
      times: count
      uniqueCallers: count(uniq: callers)
    }
  }
}
"""
variables = {"from": "2020-11-06", "till": "2021-01-13" }

# Synchronous request
data = client.execute(query=query, variables=variables)
print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}