#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


def function():
    return "pineapple"


def function2():
    return "tractor"


class Class(object):
    def method(self):
        return "parrot"


class AboutMethodBindings(Koan):
    def test_methods_are_bound_to_an_object(self):
        obj = Class()
        self.assertEqual(True, obj.method.im_self == obj)

    def test_methods_are_also_bound_to_a_function(self):
        obj = Class()
        self.assertEqual("parrot", obj.method())
        self.assertEqual("parrot", obj.method.im_func(obj))

    def test_functions_have_attributes(self):
        self.assertEqual(31, len(dir(function)))
        self.assertEqual(True, dir(function) == dir(Class.method.im_func))

    def test_bound_methods_have_different_attributes(self):
        obj = Class()
        self.assertEqual(23, len(dir(obj.method)))

    def test_setting_attributes_on_an_unbound_function(self):
        function.cherries = 3
        self.assertEqual(3, function.cherries)

    def test_setting_attributes_on_a_bound_method_directly(self):
        obj = Class()
        try:
            obj.method.cherries = 3
        except AttributeError as ex:
            self.assertMatch("'instancemethod' object has no attribute 'cherries'", ex[0])

    def test_setting_attributes_on_methods_by_accessing_the_inner_function(self):
        obj = Class()
        obj.method.im_func.cherries = 3
        self.assertEqual(3, obj.method.cherries)

    def test_functions_can_have_inner_functions(self):
        function2.get_fruit = function
        self.assertEqual("pineapple", function2.get_fruit())

    def test_inner_functions_are_unbound(self):
        function2.get_fruit = function
        try:
            cls = function2.get_fruit.im_self
        except AttributeError as ex:
            self.assertMatch("'function' object has no attribute 'im_self'", ex[0])

    # ------------------------------------------------------------------

    class BoundClass(object):
        def __get__(self, obj, cls):
            return (self, obj, cls)

    binding = BoundClass()

    def test_get_descriptor_resolves_attribute_binding(self):
        bound_obj, binding_owner, owner_type = self.binding
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls

        self.assertEqual("BoundClass", bound_obj.__class__.__name__)
        self.assertEqual("AboutMethodBindings", binding_owner.__class__.__name__)
        self.assertEqual(AboutMethodBindings, owner_type)

    # ------------------------------------------------------------------

    class SuperColor(object):
        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

    color = SuperColor()

    def test_set_descriptor_changes_behavior_of_attribute_assignment(self):
        self.assertEqual(None, self.color.choice)
        self.color = 'purple'
        self.assertEqual('purple', self.color.choice)
