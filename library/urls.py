from django.urls import path
from .views import SignupView, LoginView, BookViewSet, BorrowBookView, ReturnBookView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('books/', BookViewSet.as_view(), name='book-list'),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
    
]
