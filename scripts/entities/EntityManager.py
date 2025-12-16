import pygame
import itertools
from scripts.components import Components
from scripts.components.Components import *

class EntityManager:
    def __init__(self):
        self._next_id = itertools.count()
        self.components = {}

    def create(self) -> int:
        entity_id = next(self._next_id)
        self.components[entity_id] = {}
        return entity_id
    
    def add_component(self, entity_id, component) -> int:
        self.components[type(entity_id)] = component
        return entity_id
    
    def add_components(self, entity_id, *components) ->dict:
        if entity_id not in self.components:
            self.components[entity_id] = {}
        for comp in components:
            self.components[entity_id][type(comp)] = comp
        return self.components
    

    def delete(self, entity_id):
        self.components.remove(entity_id)

    def get(self, entity_id, component_type) -> Components:
        return self.components[entity_id].get(component_type)
    
    def entities_with(self, *component_types):
        for entity_id, comps in self.components.items():
            if all(ct in comps for ct in component_types):
                yield entity_id, comps
