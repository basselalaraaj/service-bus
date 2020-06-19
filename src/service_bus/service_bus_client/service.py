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
        subscriptions = getSubscriptionsList(topic)
        topic_list.append({"name": topic.name, "subscriptions": subscriptions})
    return topic_list


def getSubscriptionsList(topic):
    servicebus_client = getServiceBusClient()
    subscriptions = servicebus_client.list_subscriptions(topic.name)

    subscriptionsList = []
    for subscription in subscriptions:
        subscriptionsList.append({"name": subscription.name})
    return subscriptionsList


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
