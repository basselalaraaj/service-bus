from azure.servicebus import ServiceBusClient
from service_bus.config import CONNECTION_STR


def getServiceBusClient():
    return ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STR)


def getTopicList():
    servicebus_client = getServiceBusClient()
    topics = servicebus_client.list_topics()

    topic_list = []
    for topic in topics:
        subscriptions = getSubscriptionList(topic.name)
        topic_list.append({"name": topic.name, "subscriptions": subscriptions})
    return topic_list


def getSubscriptionList(topic):
    servicebus_client = getServiceBusClient()
    subscriptions = servicebus_client.list_subscriptions(topic)

    subscriptionList = []
    for subscription in subscriptions:
        subscriptionList.append({"name": subscription.name})

    return subscriptionList


def getDlqMessages(topic, subscription, count):
    servicebus_client = getServiceBusClient()
    subscription = servicebus_client.get_subscription(
        topic_name=topic, subscription_name=subscription)
    dlqReceiver = subscription.get_deadletter_receiver()
    messages = dlqReceiver.peek(count)

    messages_list = []
    for message in messages:
        messages_list.append({"body": str(message)})

    dlqReceiver.close()
    return messages_list
