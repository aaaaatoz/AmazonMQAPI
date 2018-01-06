#! env python
import boto3
from mqConfiguration import MQConfiguration
from mqBroker import MQBroker
from mqUser import MQUser
import time

if __name__=="__main__":
    # create a configuration or reuse it
    print("step - 1: create configuration ")
    myconfiguration = MQConfiguration("rafatest")

    # update the configuration to generate a new Revision
    print("step - 2: update configuration ")
    latestConfiguration = myconfiguration.updateConfiguration()

    time.sleep(10)
    # print the configuration
    myconfiguration.printConfiguration()

    #
    print("step - 3: create broker")
    myBroker = MQBroker("demo2", latestConfiguration)

    print("step - 4: waiting for broker to be ready")
    while True:
        time.sleep(60)
        if myBroker.get_broker_property("BrokerState") == "RUNNING":
            break
        print("Broker still not running yet")
    myBroker.print_broker()
    myUser = MQUser(myBroker.BrokerId)

    print("step - 5: create new user")
    time.sleep(10)
    myUser.create_user("newuser", "Passw0rd1357")
    time.sleep(10)
    myUser.printUser("newuser")
    time.sleep(10)
    myUser.list_users()

    print("step - 6: create new configuration")
    latestConfiguration = myconfiguration.updateConfiguration("./configuration/mqconfigurationnew.xml")

    print("step - 7: udpate broker with new configuration")
    myBroker.update_broker(latestConfiguration)
    time.sleep(10)
    myBroker.print_broker()

    print("step - 8: reboot broker")
    myBroker.reboot_broker()

    print("step - 9: waiting for broker to be ready")
    while True:
        time.sleep(60)
        if myBroker.get_broker_property("BrokerState") == "RUNNING":
            break
        print("Broker still not running yet")

    myBroker.print_broker()

    print("step - 10: delete broker")
    myBroker.delete_broker()

