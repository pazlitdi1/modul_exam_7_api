from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import Advisers, Services, Features, Offers, Blog, Clients, Admin, Comments, Review
from .serializers import AdvisersSerializer, ServicesSerializer, FeaturesSerializer, OffersSerializer, BlogSerializer, ClientsSerializer, AdminSerializer, CommentsSerializer, ReviewSerializer


class AdvisersViewSet(ModelViewSet):
    queryset = Advisers.objects.all()
    serializer_class = AdvisersSerializer
    # permission_classes = ([IsAuthenticated, IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'first_name', 'last_name',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        advisers = self.get_object()
        advisers.seen += 1
        advisers.save()
        return Response(data={"seen": advisers.seen})

    @action(detail=False, methods=['GET', ])
    def advisers(self, request, *args, **kwargs):
        advisers = self.get_queryset().order_by('-seen')[:3]
        serializer = AdvisersSerializer(advisers, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_advisers(self, request, *args, **kwargs):
        advisers = self.get_queryset().order_by('seen')[:3]
        serializer = AdvisersSerializer(advisers, many=True)
        return Response(data=serializer.data)


class ReviewsViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @action(detail=True, methods=['get'])
    def review_count(self, request, pk=None):
        adviser = self.get_object()
        count = adviser.reviews.count()
        return Response({'review_count': count})


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # permission_classes = ([IsAuthenticated, IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'title', 'description',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        services = self.get_object()
        services.seen += 1
        services.save()
        return Response(data={"seen": services.seen})

    @action(detail=False, methods=['GET', ])
    def services(self, request, *args, **kwargs):
        services = self.get_queryset().order_by('-seen')[:3]
        serializer = ServicesSerializer(services, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_services(self, request, *args, **kwargs):
        services = self.get_queryset().order_by('seen')[:3]
        serializer = ServicesSerializer(services, many=True)
        return Response(data=serializer.data)


class FeaturesViewSet(ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
    permission_classes = ([IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'title', 'description',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        features = self.get_object()
        features.seen += 1
        features.save()
        return Response(data={"seen": features.seen})

    @action(detail=False, methods=['GET', ])
    def services(self, request, *args, **kwargs):
        features = self.get_queryset().order_by('-seen')[:3]
        serializer = FeaturesSerializer(features, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_features(self, request, *args, **kwargs):
        features = self.get_queryset().order_by('seen')[:3]
        serializer = FeaturesSerializer(features, many=True)
        return Response(data=serializer.data)


class OffersViewSet(ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    # permission_classes = ([IsAuthenticated, IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'title', 'description',)



    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        offers = self.get_object()
        offers.seen += 1
        offers.save()
        return Response(data={"seen": offers.seen})

    @action(detail=False, methods=['GET', ])
    def offers(self, request, *args, **kwargs):
        offers = self.get_queryset().order_by('-seen')[:3]
        serializer = OffersSerializer(offers, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_offers(self, request, *args, **kwargs):
        offers = self.get_queryset().order_by('seen')[:3]
        serializer = OffersSerializer(offers, many=True)
        return Response(data=serializer.data)


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = ([IsAuthenticated, IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'title', 'description',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.seen += 1
        blog.save()
        return Response(data={"seen": blog.seen})

    @action(detail=False, methods=['GET', ])
    def blog(self, request, *args, **kwargs):
        blog = self.get_queryset().order_by('-seen')[:3]
        serializer = BlogSerializer(blog, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_blog(self, request, *args, **kwargs):
        blog = self.get_queryset().order_by('seen')[:3]
        serializer = BlogSerializer(blog, many=True)
        return Response(data=serializer.data)


class ClientsViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    # permission_classes = ([IsAuthenticated, IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'first_name', 'last_name', 'nickname',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        clients = self.get_object()
        clients.seen += 1
        clients.save()
        return Response(data={"seen": clients.seen})

    @action(detail=False, methods=['GET', ])
    def clients(self, request, *args, **kwargs):
        clients = self.get_queryset().order_by('-seen')[:3]
        serializer = ClientsSerializer(clients, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_clients(self, request, *args, **kwargs):
        clients = self.get_queryset().order_by('seen')[:3]
        serializer = ClientsSerializer(clients, many=True)
        return Response(data=serializer.data)


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = ([IsAdminUser])
    # authentication_classes = [TokenAuthentication]

    filter_backends = (SearchFilter,)
    search_fields = ('slug', 'first_name', 'last_name', 'username',)

    @action(detail=True, methods=['GET', ])
    def seen(self, request, *args, **kwargs):
        admin = self.get_object()
        admin.seen += 1
        admin.save()
        return Response(data={"seen": admin.seen})

    @action(detail=False, methods=['GET', ])
    def admin(self, request, *args, **kwargs):
        admin = self.get_queryset().order_by('-seen')[:3]
        serializer = AdminSerializer(admin, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET', ])
    def top_minimal_admin(self, request, *args, **kwargs):
        admin = self.get_queryset().order_by('seen')[:3]
        serializer = AdminSerializer(admin, many=True)
        return Response(data=serializer.data)


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = ([IsAdminUser])
    # authentication_classes = [TokenAuthentication]

