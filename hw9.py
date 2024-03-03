import redis
from typing import List, Any, Dict
from redis_lru import RedisLRU
from models import Author, Quote

client = redis.Redis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f'Find by {tag}')
    tags = tag.split()
    if len(tags) > 1:
        quotes = Quote.objects(tags__all=tags)
    else:
        quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


@cache
def find_by_author(author: str) -> dict[Any, list[Any]]:
    print(f'Find by {author}')
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result




if __name__ == '__main__':
    print(find_by_tag('mi'))
    print(find_by_tag('mi'))

    print(find_by_author('Ein'))
    print(find_by_author('Ein'))
