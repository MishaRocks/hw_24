from rest_framework.pagination import PageNumberPagination


class CursesPaginator(PageNumberPagination):
    page_size = 5
