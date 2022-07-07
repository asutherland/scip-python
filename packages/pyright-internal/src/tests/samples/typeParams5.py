# This sample tests the handling of type parameter syntax used for
# bounded and constrained TypeVars, TypeVarTuples, and ParamSpecs.

from typing import Any

class ClassA[R, *Ts, **P]:
    ...

class ClassB[R: int | str]:
    ...

# This should generate an error because 'dummy' is not declared.
class ClassC[R: dummy]:
    ...

class ClassD[R: "ClassE[Any]"]:
    ...


class ClassE[T]:
    ...

# This should generate an error because variadic type params don't 
# support bound expressions.
class ClassF[*Ts: int]: ...

# This should generate an error because ParamSpecs don't 
# support bound expressions.
class ClassG[**P: int]: ...

# This should generate an error because the expression isn't
# a valid type.
class ClassH[R: 1]: ...

# This should generate an error because a constrained type
# must contain at least two types.
class ClassI[R: ()]: ...

# This should generate an error because a constrained type
# must contain at least two types.
class ClassJ[R: (int, )]: ...

class ClassK[R: (bytes, str)]: ...

t2 = (bytes, str)
# This should generate an error because a literal tuple expression
# must be used for constrained types.
class ClassL[R: t2]: ...

