import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token
from allapps.models import Apps, Placement, AdNetwork, Source
# from django.contrib.auth.models import User
from users.models import NewUser


from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']

class AppsType(DjangoObjectType):
    class Meta:
        model = Apps
        fields = '__all__'

class PlacementType(DjangoObjectType):
    class Meta:
        model = Placement
        fields = '__all__'

class AdNetworkType(DjangoObjectType):
    class Meta:
        model = AdNetwork
        fields = '__all__'

class SourceType(DjangoObjectType):
    class Meta:
        model = Source
        fields = '__all__'

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

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    app = graphene.Field(AppsType, id=graphene.Int())
    apps = graphene.List(AppsType)

    placement = graphene.Field(PlacementType, id=graphene.Int())
    placements = graphene.List(PlacementType)

    ad_network = graphene.Field(AdNetworkType, id=graphene.Int())
    ad_networks = graphene.List(AdNetworkType)

    source = graphene.Field(SourceType, id=graphene.Int())
    sources = graphene.List(SourceType)

    @login_required
    def resolve_user(self, info, id):
        return get_user_model().objects.get(pk=id)

    @login_required
    def resolve_users(self, info):
        return get_user_model().objects.all()

    @login_required
    def resolve_app(self, info, id):
        return Apps.objects.get(pk=id)

    @login_required
    def resolve_apps(self, info):
        return Apps.objects.all()

    @login_required
    def resolve_placement(self, info, id):
        return Placement.objects.get(pk=id)

    @login_required
    def resolve_placements(self, info):
        return Placement.objects.all()

    @login_required
    def resolve_ad_network(self, info, id):
        return AdNetwork.objects.get(pk=id)

    @login_required
    def resolve_ad_networks(self, info):
        return AdNetwork.objects.all()

    @login_required
    def resolve_source(self, info, id):
        return Source.objects.get(pk=id)

    @login_required
    def resolve_sources(self, info):
        return Source.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
