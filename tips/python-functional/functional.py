import builtins
import inspect
import functools
import types


def macro_curry_definition(argsize):
    body = 'f('
    lambdas = ''.join(f'lambda a{n}: ' for n in range(argsize))
    argbody = ', '.join(f'a{n}' for n in range(argsize))
    return f'lambda f: {lambdas}f({argbody})'


def macro_uncurry_definition(argsize):
    body = 'f('
    lambdas_args = ', '.join(f'a{n}' for n in range(argsize))
    arg_applying = ''.join(f'(a{n})' for n in range(argsize))
    return f'lambda f: lambda {lambdas_args}: f{arg_applying}'


def eval_macro(expression):
    return eval(expression, {}, {})


# currying1 = id_
currying1 = eval_macro(macro_curry_definition(1))
currying2 = eval_macro(macro_curry_definition(2))
currying3 = eval_macro(macro_curry_definition(3))
currying4 = eval_macro(macro_curry_definition(4))
currying5 = eval_macro(macro_curry_definition(5))
currying6 = eval_macro(macro_curry_definition(6))

# currying1 = id_
uncurrying1 = eval_macro(macro_uncurry_definition(1))
uncurrying2 = eval_macro(macro_uncurry_definition(2))
uncurrying3 = eval_macro(macro_uncurry_definition(3))
uncurrying4 = eval_macro(macro_uncurry_definition(4))
uncurrying5 = eval_macro(macro_uncurry_definition(5))
uncurrying6 = eval_macro(macro_uncurry_definition(6))

reduce_ = (
    lambda f:
    lambda xs:
    lambda init:
    currying3(functools.reduce)(uncurrying2(f))(xs)(init)
)
compose = lambda f: lambda g: lambda x: f(g(x))
compose_n = lambda fns: reduce_(compose)(fns)(id_)

identity = lambda x: x
id_ = identity
value = lambda x: lambda _: x
true = value(True)
none = value(None)
flip1 = lambda f: lambda x: lambda y: f(y)(x)
no_argument = lambda f: lambda _: f()

ifelse = (
    lambda cond:
    lambda ifbody:
    lambda elsebody:
    ifbody(none) if cond(none) else elsebody(none)
)
if_ = lambda cond: lambda ifbody: ifelse(cond)(ifbody)(none)

tranceduce_both = (
    lambda predicate:
    lambda mapper:
    lambda concat:
    lambda xs:
    lambda x:
    ifelse(
        lambda _: predicate(x)
    )(
        lambda _: concat(xs)(mapper(x))
    )(
        lambda _: xs
    )
)
tranceduce_as_map = tranceduce_both(true)
tranceduce_as_filter = flip1(tranceduce_both)(id_)

inverse = lambda f: lambda x: not f(x)
is_zero = lambda n: n == 0
is_not_zero = inverse(is_zero)
is_multiple_of_n = lambda n: lambda x: is_zero(x % n)
is_multiple_of_3 = is_multiple_of_n(3)
is_multiple_of_5 = is_multiple_of_n(5)

minus_one = lambda n: n - 1
plus_two = lambda n: n + 2


@currying2
def concat_list(xs, x):
    xs.append(x)
    return xs


@currying2
def concat_tuple(xs, x):
    return xs + (x,)


@currying2
def concat_generator(xs, x):
    yield from xs
    yield x


@no_argument
def test_tranceduce():
    target_list = list(range(0, 100))
    answer = [1, 16, 31, 46, 61, 76, 91]

    original_version = map(plus_two,
                           map(minus_one,
                               filter(is_multiple_of_5,
                                      filter(is_multiple_of_3,
                                             target_list))))

    composed = compose_n((
        tranceduce_as_filter(is_multiple_of_3),
        tranceduce_as_filter(is_multiple_of_5),
        tranceduce_as_map(minus_one),
        tranceduce_as_map(plus_two),
    ))

    tranceduce_list_version = reduce_(composed(concat_list))(target_list)([])

    tranceduce_tuple_version = reduce_(composed(concat_tuple))(target_list)(())

    tranceduce_generator_version = reduce_(composed(concat_generator))(target_list)(iter(()))

    assert list(answer) == list(original_version)
    assert list(answer) == list(tranceduce_list_version)
    assert list(answer) == list(tranceduce_tuple_version)
    assert list(answer) == list(tranceduce_generator_version)


@no_argument
def test_everything_is_single_argument_function():
    for name, value in tuple(globals().items()):
        ## ignore special keywords and modules
        if name.startswith('__') and name.endswith('__'):
            continue
        elif isinstance(value, types.ModuleType):
            continue
        elif callable(value):
            assert len(inspect.getargspec(value).args) == 1
            continue


@no_argument
def test():
    test_tranceduce(none)
    test_everything_is_single_argument_function(none)


if __name__ == '__main__':
    test(none)
