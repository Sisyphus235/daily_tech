# -*- coding: utf8 -*-


def simplify_path(path: str) -> str:
    simple = []
    for p in path.split('/'):
        if not p or p == '.':
            continue
        elif p == '..':
            if len(simple) < 2:
                simple = []
            else:
                simple.pop()
        else:
            simple.append(p)
    return '/' + '/'.join(simple)


if __name__ == '__main__':
    assert simplify_path('/home/') == '/home'
    assert simplify_path('/../') == '/'
    assert simplify_path('/home//foo/') == '/home/foo'
    assert simplify_path('/a/./b/../../c/') == '/c'
