# from django.test import TestCase
# from ..service import MembershipsService

# class TestMembershipService(TestCase):
#     def setUp(self):
#         self.service = MembershipsService()

#     @patch("app.memberships.repository.MembershipsRepository.get_users_by_emails")
#     def test_service_create_group_memberships(self, mock_get_user_id):
#         membership_data = [{"email": "test@email.com", "numMemberships": 2}]
#         mock_get_user_id.return_value = [{'grade': {'name': 'Ontario Grade 1'}}]

#         new_memberships, invalid_memberships = self.service.create_group_memberships(
#             membership_data, "", ""
#         )

        # self.assertEqual(MembershipModel.objects.filter(ownerID=31415).count(), 2)
        # self.assertEqual(len(new_memberships), 2)
        # self.assertEqual(len(invalid_memberships), 0)