import graphene
from graphene_django import DjangoObjectType
# from graphene import ObjectType, Schema
from .models import Publisher, Book


class PublisherType(DjangoObjectType):
    
    class Meta:
        model  = Publisher
        fields = ("id", "p_name", "city", "zip")


class BookType(DjangoObjectType):
    
    class Meta:
        model  = Book
        fields = ("id", "pub", "title", "price", "category", "quantity", "b_format", "prod_year", "filesize")
        
        
class Query(graphene.ObjectType):
    all_book      = graphene.List(BookType)
    all_publisher = graphene.List(PublisherType)
    
    def resolve_all_book(root, info):
        return Book.objects.all()

    def resolve_all_publisher(root, info):
        return Publisher.objects.all()


schema = graphene.Schema(query=Query)