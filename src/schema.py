import graphene
from .service_bus.service import getTopicList
from .service_bus.models import Topic


class Query(graphene.ObjectType):
    get_topic_list = graphene.List(Topic)

    def resolve_get_topic_list(self, info):
        return getTopicList()
