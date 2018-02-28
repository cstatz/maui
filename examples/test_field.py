# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'christoph.statz <at> tu-dresden.de'

from maui.mesh import CartesianMesh
from maui.field import ScalarField


m = CartesianMesh(((-5., -5.), (5, 2.)), 0.1)

s = ScalarField(m, name="TestScalar", unit="NoUnit")
s2 = ScalarField(m, name="TestScalar", unit="NoUnit", distribute=False)
s.sync()
s2.sync()

print(s.d.keys(), s.get_value_by_point((0.4, 1.1)))
print(s2.d.keys(), s2.get_value_by_point((0.4, 1.1)))
