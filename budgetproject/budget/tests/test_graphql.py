# from app.memberships.repository import MembershipsRepository


# class TestMembershipRepository(TestCase):
#     def setUp(self):
#         self.repo = MembershipsRepository()
#         MembershipModelFactory(ownerID=123)
#         MembershipModelFactory(ownerID=987)
#         self.model = MembershipModel.objects.get(ownerID=123)
    
#     @patch("python_graphql_client.GraphqlClient.execute")
#     def test_get_users_by_username_handling_user_id_of_type_int(self, mock_execute):
#         mock_execute.return_value = {
#             "data": {
#                 "users": [
#                     {"id": "8158849", "username": "parent1@gmail.com"},
#                     {"id": "8158851", "username": "parent2@gmail.com"},
#                 ]
#             }
#         }
#         expected_results = [
#             {"id": "8158849", "email": "parent1@gmail.com"},
#             {"id": "8158851", "email": "parent2@gmail.com"},
#         ]

#         emails = ["parent1@gmail.com", "parent2@gmail.com"]

#         response = self.repo.get_users_by_emails(emails, 123, "123123123")

#         self.assertEqual(response, expected_results)
#         mock_execute.assert_called_once_with(
#             query=get_users_by_username,
#             variables={"emails": emails},
#             headers={"userID": "123", "token": "123123123"},
#         )