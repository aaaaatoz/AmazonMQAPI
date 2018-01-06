# MQ API full list
    mq:ListBrokers
    mq:CreateBroker
    mq:ListUsers
    mq:DescribeBroker
    mq:DeleteUser
    mq:CreateUser
    mq:UpdateConfiguration
    mq:ModifyBroker
    mq:CreateConfiguration
    mq:DescribeUser
    mq:DescribeConfiguration
    mq:ListConfigurations
    mq:DescribeConfigurationRevision
    mq:UpdateUser
    mq:DeleteBroker
    mq:RestartBroker
    mq:ListConfigurationRevisions


## broker related
    - CreateBroker
    - DescribeBroker
    - ModifyBroker
    - ListBrokers
    - DeleteBroker
    - RestartBroker

## User related
    - CreateUser
    - ListUsers
    - DescribeUser
    - UpdateUser
    - DeleteUser

## Configuration related
    - CreateConfiguration
    - DescribeConfiguration
    - ListConfigurations
    - DescribeConfigurationRevision
    - ListConfigurationRevisions
    - UpdateConfiguration
    
# demo process
    1. create a configuration
    2. update the configuration
    3. generate a new Revision
    4. list the revisions of the configuration
    5. use the latest revision to create a broker
    6. create a broker based on latest configuration
    7. print the broker's information
    8. wait until the broker is running
    9. create an new user for the broker
    10. list users in the broker
    11. create an new configuration again
    12. modify the broker to use new configuration
    13. reboot the broker to make the change 9, 12 effective
    14. delete the broker