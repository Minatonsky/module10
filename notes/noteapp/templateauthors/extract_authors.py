from django import template

register = template.Library()


def authors(note_authors):
    return ', '.join([str(fullname) for fullname in note_authors.all()])


register.filter('authors', authors)

