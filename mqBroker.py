#! env python
import boto3
import base64



class MQBroker:
    def __init__(self, brokername, configuration={}, region="ap-southeast-2"):
        self.brokerName = brokername
        self.region = region
        self.client = boto3.client("mq", region_name=region)

        brokers = self.client.list_brokers()['BrokerSummaries']

        for broker in brokers:
            if self.brokerName == broker['BrokerName']:
                print("The Broker %s is already in... skip creation" % (self.brokerName))
                self.BrokerId = broker['BrokerId']
                self.BrokerArn = broker['BrokerArn']
                return

        response = self.client.create_broker(
            AutoMinorVersionUpgrade=True,
            BrokerName=brokername,
            Configuration=configuration,
            DeploymentMode='SINGLE_INSTANCE',
            EngineType='ACTIVEMQ',
            EngineVersion='5.15.0',
            HostInstanceType='mq.t2.micro',
            PubliclyAccessible=True,
            SecurityGroups=[
                'sg-b98d6fde',  # put my security group id as demo sample
            ],
            SubnetIds=[
                'subnet-4303ac35'  # put my subnet
            ],
            Users=[
                {
                    'ConsoleAccess': True,
                    'Password': 'pAssw0rd1357',  # replace with a complicated password
                    'Username': 'root'
                },
            ]
        )
        self.BrokerId = response['BrokerId']
        self.BrokerArn = response['BrokerArn']
        print("The Broker %s is created" % (brokername))
        return

    def print_broker(self):
        response = self.client.describe_broker(
            BrokerId=self.BrokerId
        )
        ## sameple output:

        print("Broker %s's information:===================" % response['BrokerName'])
        print("\tBroker's AutoMinorVersionUpgrade: %s" % response['AutoMinorVersionUpgrade'])
        print("\tBroker's BrokerState: %s" % response['BrokerState'])
        print("\tBroker's BrokerArn: %s" % response['BrokerArn'])
        print("\tBroker's BrokerId: %s" % response['BrokerId'])
        print("\tBroker's console: %s" % response['BrokerInstances'][0]['ConsoleURL'])
        print("\tBroker's Endpoints: %s" % response['BrokerInstances'][0]['Endpoints'])
        print("\tBroker's current Configuration ID: %s" % response['Configurations']['Current']['Id'])
        print("\tBroker's current Configuration Revision: %s" % response['Configurations']['Current']['Revision'])
        print("\tBroker's DeploymentMode: %s" % response['DeploymentMode'])
        print("\tBroker's EngineType: %s" % response['EngineType'])
        print("\tBroker's EngineVersion: %s" % response['EngineVersion'])
        print("\tBroker's HostInstanceType: %s" % response['HostInstanceType'])
        print("\tBroker's MaintenanceWindowStartTime: %s" % str(response['MaintenanceWindowStartTime']))
        print("\tBroker's Network PubliclyAccessible: %s" % str(response['PubliclyAccessible']))
        print("\tBroker's Network SecurityGroups: %s" % str(response['SecurityGroups']))
        print("\tBroker's Network SubnetIds: %s" % str(response['SubnetIds']))
        print("\tBroker's Users: %s" % str([user['Username'] for user in response['Users']]))

    def update_broker(self, configuration):
        self.client.update_broker(
            BrokerId=self.BrokerId,
            Configuration=configuration
        )

    def reboot_broker(self):
        self.client.reboot_broker(
            BrokerId=self.BrokerId
        )

    def delete_broker(self):
        self.client.delete_broker(
            BrokerId=self.BrokerId
        )
        print("Broker deleted")

    def get_broker_property(self, property_name):
        response = self.client.describe_broker(
            BrokerId=self.BrokerId
        )
        if property_name not in response:
            print("property %s is not supported." % property_name)
            return None
        else:
            return response[property_name]


if __name__ == "__main__":
    mqbroker = MQBroker("testbroker")
    mqbroker.print_broker()
