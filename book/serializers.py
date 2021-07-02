from .models import Book, BookDetails
from rest_framework import serializers

class BookDetailsSerializer(serializers.ModelSerializer):
    summary =serializers.CharField(max_length=200)

    class Meta:
        model = BookDetails
        fields  = ['id', 'summary']


class BookSerializer(serializers.ModelSerializer):
    rbook = BookDetailsSerializer(many=True)

    def create(self, validated_data):
        temp_book_detail = validated_data.pop('rbook')
        new_book= Book.objects.create(**validated_data)
        for i in temp_book_detail:
            BookDetails.objects.create(**i, book=new_book)
        return new_book

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.author=validated_data.get('author', instance.author)

        book_variants = validated_data.pop('rbook')
        instance.variants.summary = book_variants.get('summary', instance.variants.summary)
        instance.save()
        return instance


    class Meta:
        model = Book
        fields = ['id','rbook','title', 'author']





