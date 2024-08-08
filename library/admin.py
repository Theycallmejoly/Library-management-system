from django.contrib import admin
from django.contrib.auth.models import User
from .models import Book, Borrow

# Unregister the User model if it's already registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register the default User admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
admin.site.register(User, DefaultUserAdmin)

# Register the Book and Borrow models
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')
    search_fields = ('title', 'author')
    list_filter = ('available',)

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_at', 'returned_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('returned_at',)

admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
