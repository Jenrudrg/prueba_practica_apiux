from rest_framework import serializers
# Models
from .models import Books, Author

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'nationality'] 
        # fields = '__all__'

class BooksSerializers(serializers.ModelSerializer):
    author = AuthorSerializers(read_only=True, many=True)
    class Meta:
        model = Books
        fields = '__all__'

        