"""Global set of constants for numerical differentiation"""


class _Dst(object):
    """Set of constants for AT numerical analysis"""
    XYStep = 1.e-8           # Coordinate step for differentiation
    DPStep = 1.e-6           # Momentum step for dispersion and chromaticity
    OrbConvergence = 1.e-12  # Convergence criterion for orbit
    OrbMaxIter = 20          # Max. number of iterations for orbit

    def __setattr__(self, name, value):
        _ = getattr(self, name)     # make sure attribute exists
        object.__setattr__(self, name, value)

    def reset(self, name):
        delattr(self, name)


DConstant = _Dst()
