from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.photo import CREATE_PHOTO_DOC, SHOW_PHOTO_DOC, LIST_PHOTO_DOC
from api.v1.serializers.photo.show import PhotoSerializer
from api.v1.services.photo.create import PhotoCreateService
from api.v1.services.photo.delete import PhotoDeleteService
from api.v1.services.photo.list import PhotoListService
from api.v1.services.photo.show import PhotoShowService
from api.v1.services.photo.update import PhotoUpdateService, PhotoPartialUpdateService
from utils.pagination import CustomPagination


class ListPhotoView(APIView):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(**LIST_PHOTO_DOC)
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(PhotoListService, request.GET.dict() | {'current_user': user})
        return Response(
            {
                "pagination": CustomPagination(
                    outcome.result,
                    current_page=outcome.service.cleaned_data["page"],
                    per_page=outcome.service.cleaned_data["per_page"],
                ).to_json(),
                "results": PhotoSerializer(
                    outcome.result.object_list, many=True
                ).data,
            }
        )

class CreatePhotoView(APIView):
    serializer_class = PhotoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**CREATE_PHOTO_DOC)
    def post(self, request: Request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoCreateService,
                                 request.POST.dict() | {'current_user': request.user},
                                 request.FILES)
        return Response(PhotoSerializer(outcome.result).data, status=status.HTTP_200_OK)

class RetrieveUpdateDeletePhotoView(APIView):
    serializer_class = PhotoSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**SHOW_PHOTO_DOC)
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(PhotoShowService, kwargs | {'current_user': user})
        return Response(PhotoSerializer(outcome.result).data, status=outcome.response_status)

    def put(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(PhotoUpdateService, request.data | kwargs | {'current_user': user})
        return Response(PhotoSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(PhotoPartialUpdateService, request.data | kwargs | {'current_user': user})
        return Response(PhotoSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        ServiceOutcome(PhotoDeleteService, kwargs | {'current_user': user})
        return Response(None, status=status.HTTP_200_OK)
