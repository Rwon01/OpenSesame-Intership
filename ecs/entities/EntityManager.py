import pygame
import itertools


class EntityManager:
    def __init__(self):
        self._next_id = itertools.count()
        self.components = {}

    def create(self):
        eid = next(self._next_id)
        self.components[eid] = {}
        return eid
    
    def add_component(self, eid, component):
        self.components[eid][type(component)] = component

    def get(self, eid, component_type):
        return self.components[eid].get(component_type)
    
    def entities_with(self, *component_types):
        for eid, comps in self.components.items():
            if all(ct in comps for ct in component_types):
                yield eid, comps