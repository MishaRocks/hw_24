from rest_framework.pagination import PageNumberPagination


class LessonsPaginator(PageNumberPagination):
    page_size = 5