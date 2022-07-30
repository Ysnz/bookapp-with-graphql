import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from graphene import ObjectType, Schema
from .models import Publisher, Book


class PublisherType(DjangoObjectType):
    
    class Meta:
        model  = Publisher
        fields = ("id", "p_name", "city", "zip")


class BookType(DjangoObjectType):
    
    class Meta:
        model  = Book
        fields = ("id", "pub", "title", "price", "category", "quantity", "b_format", "prod_year", "filesize")
        
        
class Query(ObjectType):
    all_book      = graphene.List(BookType)
    all_publisher = graphene.List(PublisherType)

schema = graphene.Schema(query=Query)