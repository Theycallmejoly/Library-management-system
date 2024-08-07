from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer
from rest_framework.permissions import IsAuthenticated


class  BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    

    @action(detail=True, methods=['post'])
    def borrow (self , request , pk = None):
        book = self.get_object()
        if not book.available:
            return Response({'status' : 'Book not available'} , status = status.HTTP_400_BAD_REQUEST)
        borrow = borrow.object.create(book = book , user = request.user)
        book.available = False
        book.save()
        return Response({'status' : 'Book Borrowed'} , status = status.HTTP_200_OK)
    

    @action(detail=True, methods=['post'])
    def retrunBook(self , Request , pk = None):
        book = self.get_object()
        try:
            borrow = Borrow.objects.get(book = book , user = Request.user , return_date__isnull = True)
        except Borrow.DoesNotExist:
            return Response({'stauts' : 'Borrow record not found'}, status = status.HTTP_400_BAD_REQUEST)
        borrow.return_date = models.DateField(auto_now_add=True)
        borrow.save()
        book.available = True
        book.save()
        return Response({'status' : 'Book returned'} , status = status.HTTP_200_OK)