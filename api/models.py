from django.db import models


class Advisers(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    image = models.URLField(null=True)
    seen = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        # Ordering by last_name, first_name, and created_at
        ordering = ['last_name', 'first_name', '-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['last_name', 'first_name']),
        ]

    def __str__(self):
        return self.first_name


class Review(models.Model):
    adviser = models.ForeignKey(Advisers, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.adviser.name}'

class Services(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True)
    seen = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering by title and created_at
        ordering = ['title', '-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Features(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.URLField(null=True)
    seen = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering by title and created_at
        ordering = ['title', '-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Offers(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True)
    seen = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering by title and created_at
        ordering = ['title', '-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Admin(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    image = models.URLField(null=True)
    password = models.CharField(max_length=100)
    seen = models.PositiveBigIntegerField(default=0)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        # Ordering by last_name, first_name, and username
        ordering = ['last_name', 'first_name', 'username']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['username']),
            models.Index(fields=['last_name', 'first_name']),
        ]

    def __str__(self):
        return self.username


class Blog(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True)
    seen = models.PositiveBigIntegerField(default=0)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordering by title and created_at
        ordering = ['title', '-created_at']

        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Clients(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    education = models.CharField(max_length=50, null=True)
    seen = models.PositiveBigIntegerField(default=0)
    image = models.URLField(null=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        # Ordering by last_name, first_name, and nickname
        ordering = ['last_name', 'first_name', 'nickname']

        # Adding indexes for performance improvements
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['nickname']),
            models.Index(fields=['last_name', 'first_name']),
        ]

    def __str__(self):
        return self.nickname


class Comments(models.Model):
    slug = models.SlugField(unique=True, null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
