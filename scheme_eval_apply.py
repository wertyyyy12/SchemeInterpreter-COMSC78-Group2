import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        operator = scheme_eval(expr.first, env)
        args = expr.rest.map(lambda arg: scheme_eval(arg, env))
        return scheme_apply(operator, args, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if not isinstance(env, Frame):
        assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):

        # BEGIN PROBLEM 2
        "*** MO'S CODE HERE ***"
        # Convert Scheme list to Python list
        py_list = []
        # As long as Scheme list is not empty
        while args is not nil:
            # Append first element to py_list
            py_list.append(args.first)
            # Sets Scheme list to the the remaining elements
            args = args.rest

        # need_env: a Boolean flag that indicates whether or not
        # this built-in procedure will need the current environment
        # to be passed in as the last argument.
        # The environment is required, for instance,
        # to implement the built-in eval procedure.

        # Flag from scheme_builtins to check if
        # procedure needs environment or not
        if procedure.need_env is True:
            py_list.append(env)

        try:
            # BEGIN PROBLEM 2
            "*** MO'S CODE HERE ***"

            # py_func: the Python function that implements
            # the built-in Scheme procedure.

            # Executes the built-in procedure by calling
            # the Python function that implements the Scheme
            # procedure, using *py_list to unpack the list of args
            result = procedure.py_func(*py_list)
            return result
            # END PROBLEM 2

        except TypeError as err:
            raise SchemeError(
                'incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):

        # BEGIN PROBLEM 9
        # Create a new Frame instance using make_child_frame function
        # The new frame is a child of the frame in which the lambda is defined.
        child_frame = procedure.env.make_child_frame(procedure.formals, args)
        eval_result = eval_all(procedure.body, child_frame)

        # Return the evaluated result of evaluating expression in the body of precedure
        return eval_result
        # END PROBLEM 9

    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** MO'S CODE HERE ***"
        # Evaluate the body in the environment with provided arguments
        return scheme_eval(procedure.body, env.make_child_frame([], args))
        # END PROBLEM 11

    else:
        assert False, "Unexpectzed procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    for i in range(0, expressions.__len__() - 1):
        if expressions.first == nil:
            return None
        else:
            scheme_eval(expressions.first, env)
            expressions = expressions.rest

    # replace this with lines of your own code
    return scheme_eval(expressions.first, env)

    # END PROBLEM 6


class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val
