#! env python
import boto3
import base64

"""
    - CreateUser
    - ListUsers
    - DescribeUser
    - UpdateUser
    - DeleteUser
"""

class MQUser:
    def __init__(self, brokerId, region="ap-southeast-2"):
        self.brokerId=brokerId
        self.region = region
        self.client = boto3.client("mq", region_name=region)

    def create_user(self, username, password):
        self.client.create_user(
            BrokerId=self.brokerId,
            ConsoleAccess=False,
            Password=password,
            Username=username
        )

    def list_users(self):
        users=self.client.list_users(
            BrokerId=self.brokerId
        )

    def update_user_password(self, username, newpassword):
        self.client.update_user(
            BrokerId=self.brokerId,
            Password=newpassword,
            Username=username
        )

    def update_user_consoleAccess(self, username, console_access=True):
        self.client.update_user(
            BrokerId=self.brokerId,
            ConsoleAccess=console_access,
            Username=username
        )

    def update_user_groups(self, username, groups=[]):
        self.client.update_user(
            BrokerId=self.brokerId,
            Groups=groups,
            Username=username
        )

    def printUser(self, username):
        user = self.client.describe_user(
            BrokerId=self.brokerId,
            Username=username
        )
        print user

    def deleteUser(self, username):
        self.client.delete_user(
            BrokerId=self.brokerId,
            Username=username
        )