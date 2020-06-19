import graphene
from service_bus.service_bus_client.service import getTopicList, getDlqMessages
from service_bus.service_bus_client.models import Topic, Message


class Query(graphene.ObjectType):
    get_topic_list = graphene.List(Topic)
    get_dlq_messages = graphene.List(
        Message, topic=graphene.String(), subscription=graphene.String(), count=graphene.Int(default_value=10))

    def resolve_get_topic_list(self, _info):
        return getTopicList()

    def resolve_get_dlq_messages(self, _info, topic, subscription, count):
        return getDlqMessages(topic, subscription, count)
