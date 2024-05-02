from djongo import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.DateField(null=True, blank=True)
    born_location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.text[:50]
