import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from allapps.models import *
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']

class AuthMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = NewUser.objects.get(username=username)
        if user.check_password(password):
            return AuthMutation(user=user, token=get_token(user))
        raise Exception("Invalid credentials")

class Mutation(graphene.ObjectType):
    token_auth = AuthMutation.Field()

class AdNetworkType(DjangoObjectType):
    class Meta:
        model = AdNetwork

class SourceType(DjangoObjectType):
    class Meta:
        model = Source

    ad_network = graphene.List(AdNetworkType)
    def resolve_ad_network(self, info):
        return AdNetwork.objects.filter(source=self)

class PlacementType(DjangoObjectType):
    class Meta:
        model = Placement
    ad_source = graphene.List(SourceType)
    ad_networks = graphene.List(SourceType)

    def resolve_ad_source(self, info):
        return Source.objects.filter(placement=self)
    
    def resolve_ad_networks(self, info):
        return Source.objects.filter(placement=self)

class Query(graphene.ObjectType):
    ad_sources = graphene.List(PlacementType, package=graphene.String())
    
    def resolve_ad_sources(self, info, package):
        app = Apps.objects.filter(package=package).first()
        return Placement.objects.filter(app=app)

schema = graphene.Schema(query=Query, mutation=Mutation)
