from .models import Book, BookDetails
from rest_framework import serializers

class BookDetailsSerializer(serializers.ModelSerializer):
    summary =serializers.CharField(max_length=200)

    class Meta:
        model = BookDetails
        fields = ['id', 'summary']


class BookSerializer(serializers.ModelSerializer):
    rbook = BookDetailsSerializer(many=True)

    def create(self, validated_data):
        temp_book_detail = validated_data.pop('rbook')
        new_book= Book.objects.create(**validated_data)
        # BookDetails.objects.create(new_book=new_book, **temp_book_detail)
        # return new_book
        for i in temp_book_detail:
            BookDetails.objects.create(**i, book=new_book)
        return new_book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)

        # sum = rbook.instance.summary
        # sum_data = validated_data.pop('rbook')
        # instance.sum_data.summary = validated_data.get('summary', instance.sum_data.summary)
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get('title', instance.title)
    #     instance.author=validated_data.get('author', instance.author)
    #
    #     book = validated_data.pop('rbook')
    #     instance.summary = book.get('summary', instance.book.summary)
    #     instance.save()
    #     return instance


    class Meta:
        model = Book
        fields = ['id','rbook','title', 'author']





