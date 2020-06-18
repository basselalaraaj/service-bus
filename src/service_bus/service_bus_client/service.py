from azure.servicebus import ServiceBusClient
from service_bus.config import CONNECTION_STR

servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=CONNECTION_STR)


def getTopicList():
    topics = []
    topic_listASB = servicebus_client.list_topics()
    for topic in topic_listASB:
        subscriptions = []
        subscriptionsASB = servicebus_client.list_subscriptions(topic.name)
        for subscription in subscriptionsASB:
            subscriptions.append({"name": subscription.name})
        topics.append({"name": topic.name, "subscriptions": subscriptions})
    return topics
