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


class CreatePublisher(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        id     = graphene.String()
        p_name = graphene.String(required=True)
        city = graphene.String(required=True)
        zip  = graphene.String(required=True)

    # Class attributes define the response of the mutation
    publisher = graphene.Field(PublisherType)

    @classmethod
    def mutate(cls, root, info, p_name, city ,zip):
        publisher = Publisher()
        publisher.p_name = p_name
        publisher.city = city
        publisher.zip = zip
        publisher.save()
        
        return CreatePublisher(publisher=publisher)


class UpdatePublisher(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        p_name = graphene.String(required=True)
        city = graphene.String(required=True)
        zip = graphene.String(required=True)
        id = graphene.ID()


    publisher = graphene.Field(PublisherType)
    
    @classmethod
    def mutate(cls, root, info, title, id):
        category = Publisher.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdatePublisher(category=category)


class CreateBooks(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        id     = graphene.String()
        pub = graphene.String(required=True)
        title = graphene.String(required=True)
        price = graphene.Float(required=True)
        category  = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        b_format  = graphene.String(required=True)
        prod_year = graphene.Int(required=True)
        filesize = graphene.Int(required=True)
        

    # Class attributes define the response of the mutation
    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, pub, title ,price, category, quantity, b_format, prod_year, filesize):
        book = Book()
        book.pub = pub
        book.title = title
        book.price = price
        book.category = category
        book.quantity = quantity
        book.b_format = b_format
        book.prod_year = prod_year
        book.filesize = filesize
        book.save()
        
        return CreateBooks(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        pub = graphene.String(required=True)
        title = graphene.String(required=True)
        price = graphene.Float(required=True)
        category  = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        b_format  = graphene.String(required=True)
        prod_year = graphene.Int(required=True)
        filesize = graphene.Int(required=True)
        id = graphene.ID()


    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, pub, title ,price, category, quantity, b_format, prod_year, filesize, id):
        books = Book.objects.get(pk=id)
        books.pub = pub
        books.title = title
        books.price = price
        books.category = category
        books.quantity = quantity
        books.b_format = b_format
        books.prod_year = prod_year
        books.filesize = filesize
        books.save()
        
        return UpdateBook(books=books)


class Mutation(graphene.ObjectType):
    update_publisher = UpdatePublisher.Field()
    create_publisher = CreatePublisher.Field()
    update_book = UpdateBook.Field()
    create_book = CreateBooks.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)