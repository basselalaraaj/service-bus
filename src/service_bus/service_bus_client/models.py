import graphene


class Subscription(graphene.ObjectType):
    name = graphene.String()


class Topic(graphene.ObjectType):
    name = graphene.String()
    subscriptions = graphene.List(Subscription)


class Message(graphene.ObjectType):
    body = graphene.JSONString()
