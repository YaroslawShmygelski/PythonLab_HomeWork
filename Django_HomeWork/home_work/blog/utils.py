import random


def unique_slugify(instance, slug):
    model = instance.__class__
    while model.objects.filter(slug=slug).exists():
        slug += str(random.randint(0,10))

    return slug
