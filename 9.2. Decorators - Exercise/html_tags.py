def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            return f"<{tag}>{func_ref(*args)}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))