from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Book, Borrow
from .serializers import UserSerializer, BookSerializer, BorrowSerializer




class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=400)

class BookViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BorrowBookView(generics.CreateAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.available:
            book.available = False
            book.save()
            serializer.save(user=self.request.user)
        else:
            serializer.ValidationError("This book is already borrowed.")

class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            borrow = Borrow.objects.get(pk=pk, user=request.user)
            borrow.returned_at = timezone.now()
            borrow.book.available = True
            borrow.book.save()
            borrow.save()
            return Response({'status': 'Book returned'})
        except Borrow.DoesNotExist:
            return Response({'error': 'Borrow record not found'}, status=404)
