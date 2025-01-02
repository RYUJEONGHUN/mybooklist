from django.db import models


class Book(models.Model):
  title=models.CharField(max_length=200)
  author=models.CharField(max_length=200)
  publication_date=models.DateField()
  price=models.DecimalField(max_digits=6,decimal_places=2)


class FineTunedModel(models.Model):
  Model_CHOICES=[
    ('ada','Ada'),
    ('babbage','Babbage'),
    ('curie','Curie'),
    ('davinci','Davinci'),
  ]

  model_name=models.CharField(max_length=100)
  base_model=models.CharField(max_length=100, choices=Model_CHOICES)

  def __str__(self):
    return self.model_name
  
class TrainingData(models.Model):
  fine_tuned_model=models.ForeignKey(FineTunedModel, on_delete=models.CASCADE, related_name='training_data')
  prompt=models.TextField()
  completion=models.TextField()

  def __str__(self):
    return f"{self.fine_tuned_model.model_name}의 훈련 데이터"
# Create your models here.

