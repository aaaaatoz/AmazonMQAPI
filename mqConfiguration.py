#! env python
import boto3
import base64

class MQConfiguration:
    def __init__(self, configuration_name, region="ap-southeast-2"):
        self.region = region
        self.configuration_name = configuration_name
        self.client = boto3.client("mq", region_name = region)

        configurations = self.client.list_configurations()['Configurations']

        for configuration in configurations:
                if configuration_name == configuration['Name']:
                    print("The configuration %s is already in... skip creation" %(configuration_name))
                    self.configurationid = configuration['Id']
                    return

        response = self.client.create_configuration(
                        EngineType='ACTIVEMQ',  # only support ACTIVEMQ now
                        EngineVersion='5.15.0', # only support 5.15.0 now
                        Name=configuration_name
            )
        self.configurationid = response['Id']
        print("The configuration %s is created" % (configuration_name))

    def printConfiguration(self):
        response = self.client.describe_configuration(ConfigurationId=self.configurationid)
        print("Configuratin Name: %s" %(response['Name']))
        print("Configuratin Arn: %s" %(response['Arn']))
        print("Configuratin EngineType: %s" %(response['EngineType']))
        print("Configuratin Id: %s" %(response['Id']))
        print("Configuratin Latest Revision: %s" %(response['LatestRevision']['Revision']))
        return response

    def __getConfigurationXML(self, file):
        fileText = ""
        for line in open(file, "rb"):
            fileText += line
        return fileText

    def updateConfiguration(self, file="./configuration/mqconfiguration.xml"):
        response = self.client.update_configuration(
            ConfigurationId=self.configurationid,
            Data=base64.b64encode(self.__getConfigurationXML(file)),
            Description='updated configuration'
        )
        print("configuration updated")
        return {
            'Id': self.configurationid,
            'Revision': response['LatestRevision']['Revision']
        }

    def listConfigurationRevisions(self):
        revisions=self.client.list_configuration_revisions(ConfigurationId=self.configurationid)['Revisions']
        print("configuration name: %s" %(self.configuration_name))
        print("configuration Id: %s" %(self.configurationid))
        for revision in revisions:
            print("\trevision id %d" %(revision['Revision']))
            print("\trevision description %s" %(revision['Description']))
        return revisions


    def describeConfigurationRevision(self, configurationid, ConfigurationRevision):
        pass


# if __name__=="__main__":
#     mqconfiguration = MQConfiguration("rafatest")
#     mqconfiguration.printConfiguration()
#     #mqconfiguration.updateConfiguration()
#     mqconfiguration.listConfigurationRevisions()


