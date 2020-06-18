import graphene
from service_bus.service_bus_client.service import getTopicList
from service_bus.service_bus_client.models import Topic


class Query(graphene.ObjectType):
    get_topic_list = graphene.List(Topic)

    def resolve_get_topic_list(self, _info):
        return getTopicList()
