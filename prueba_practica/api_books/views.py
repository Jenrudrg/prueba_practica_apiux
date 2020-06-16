from django.shortcuts import render
# Generics Api 
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Models 
from .models import Books, Author
# Model Serializers
from .serializers import BooksSerializers, AuthorSerializers

def home(request):
    return render(request,'api_books/home.html')


# class AuthorApiView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
    
class AuthorApiView(APIView):

    serializer_class = AuthorSerializers
    
    def get(self, request, format=None):
        qs = Author.objects.all()
        
        authors = []
        
        for item in qs:
            books = [] 
            a =  {
            'id':item.id,
            'name':item.name,
            'nationality':item.nationality,
            'books':books,
            }
            
            qs2 = Books.objects.filter(author = item.id)
            for book in qs2: 
                b = {
                    'name':book.name, 
                    'pages':book.pages_number,
                }
                books.append(b)
            
            authors.append(a)

        
        result = {"Author's": authors}
        return Response(result)
    

    
    def post(self, request, format=None):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            new_author = Author()
            new_author.name = serializer.data.get('name')
            new_author.nationality = serializer.data.get('nationality')
            # new_author.books = []
            new_author.save()
            return Response({"message": 'Success'}, status = status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        

class AuthorDetailApiView(APIView):
           
    def get(self, request, pk, format=None):         
        qs = Author.objects.filter(pk = pk)
        authors = []
        
        for item in qs:
            books = [] 
            a =  {
            'id':item.id,
            'name':item.name,
            'nationality':item.nationality,
            'books':books,
            }
            
            qs2 = Books.objects.filter(author = item.id)
            for book in qs2: 
                b = {
                    'name':book.name, 
                    'pages':book.pages_number,
                }
                books.append(b)
            
            authors.append(a)

        
        result = {"Author's": authors}
        return Response(result)

class BooksApiView(APIView): 
    
    # def get(self, request, format=None):
    #     qs = Books.objects.all()
    #     books = [] 
    #     for item in qs:
    #         qs2 = Author.objects.filter(books =  item.id)
    #         a =  {
    #         # 'id':item.id,
    #         'author_id':qs2[0].id,
    #         'name':item.name,
    #         'pages_number':item.pages_number,
    #         }
    #         books.append(a)
    #     result = {"Books": books}
    #     return Response(result)      
    
    def post(self, request, format=None):
        data = request.data
        if request.data.get('author_id') \
            and request.data.get('name') \
                and request.data.get('pages_number'):
            author_id = request.data.get('author_id')
            name = request.data.get('name')
            pages_number = request.data.get('pages_number')
            
            qs2 = Author.objects.filter(id = author_id)
            if qs2.exists():
                books = Books()
                books.name = name
                books.pages_number = pages_number
                books.save()

                qs2[0].books.add(books.id)
            
            else:
                books = Books()
                books.name = name
                books.pages_number = pages_number
                books.save()
                
                new_author = Author.objects.create(
                    name = '',
                    nationality = '',
                )
                qs3 = Author.objects.filter(id = new_author.id)
                qs3[0].books.add(books.id)
            
            return Response({"message": 'Success'}, status = status.HTTP_201_CREATED)
        return Response({"message":'Error: Datos incorrectos ó Incompletos'}, status = status.HTTP_400_BAD_REQUEST)      
    