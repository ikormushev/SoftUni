import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from django.db.models import Count, Q, Avg
from main_app.models import Author, Article


# Django Queries I
def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""
    elif search_name is not None and search_email is None:
        query = Q(full_name__icontains=search_name)
    elif search_name is None and search_email is not None:
        query = Q(email__icontains=search_email)
    else:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)

    authors = Author.objects.filter(query).order_by("-full_name")

    if not authors:
        return ""

    return "\n".join([f"Author: {a.full_name}, "
                      f"email: {a.email}, "
                      f"status: {'Banned' if a.is_banned else 'Not Banned'}" for a in authors])


def get_top_publisher():
    top_author = (Author.objects
                  .annotate(article_count=Count('article'))
                  .order_by('-article_count', 'email')).first()

    if not top_author or top_author.article_count == 0:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.article_count} published articles."


def get_top_reviewer():
    top_author = (Author.objects
                  .annotate(reviews_count=Count('review'))
                  .order_by('-reviews_count', 'email')).first()

    if not top_author or top_author.reviews_count == 0:
        return ""

    return f"Top Reviewer: {top_author.full_name} with {top_author.reviews_count} published reviews."


# Django Queries II
def get_latest_article():
    latest_article = (Article.objects
                      .annotate(reviews_num=Count('review'))
                      .order_by('-published_on')).first()

    if not latest_article:
        return ""

    authors = ', '.join(a.full_name for a in latest_article.authors.all().order_by('full_name'))
    avg_rating = sum([r.rating for r in latest_article.review.all()]) / latest_article.reviews_num \
        if latest_article.reviews_num else 0

    return (f"The latest article is: {latest_article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {latest_article.reviews_num} times. "
            f"Average Rating: {avg_rating:.2f}.")


def get_top_rated_article():
    top_rated_article = (Article.objects
                         .annotate(reviews_num=Count('review'),
                                   avg_rating=Avg('review__rating'))
                         .filter(reviews_num__gt=0)
                         .order_by('-avg_rating', 'title')
                         .first())

    if top_rated_article is None:
        return ""

    avg_rating = top_rated_article.avg_rating if top_rated_article.avg_rating is not None else 0

    return (f"The top-rated article is: {top_rated_article.title}, "
            f"with an average rating of {avg_rating:.2f}, "
            f"reviewed {top_rated_article.reviews_num} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.prefetch_related('review').filter(email__exact=email).first()
    if not author:
        return "No authors banned."

    author.is_banned = True
    reviews_count = author.review.all().count()
    author.save()
    author.review.all().delete()

    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."
