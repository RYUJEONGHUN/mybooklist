from django.contrib import admin
from .models import Book
from .models import FineTunedModel, TrainingData


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display=['title','author','publication_date','price']
  search_fields=['title','author']
  list_filter=['author','publication_date']
# Register your models here.

@admin.register(FineTunedModel)
class FineTunedModelAdmin(admin.ModelAdmin):
  list_display=('model_name','base_model')
  search_fields=('model_name','base_model')


@admin.register(TrainingData)
class TrainingDataAdmin(admin.ModelAdmin):
  list_display=('prompt','completion','fine_tuned_model')
  search_fields=('prompt','completion','fine_tuned_model__model_name')
  list_filter=('fine_tuned_model',)