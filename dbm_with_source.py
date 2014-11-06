from pylearn2.models.dbm import DBM, CompositeLayer
from pylearn2.space import CompositeSpace
from theano.compat.python2x import OrderedDict


class DBMWithSource(DBM):
    def __init__(self, input_space=None, *args, **kwargs):
        self.input_source = kwargs.pop('input_source', 'features')
        #self.target_source = kwargs.pop('target_source', 'targets')
        super(DBMWithSource, self).__init__(*args, **kwargs)
    # def __init__(self, input_source, input_space, layers, batch_size, niter):
    #     self.input_source = input_source
    #     #self.target_source = kwargs.pop('target_source', 'targets')
    #     super(DBMWithSource, self).__init__(input_source, input_space, layers, batch_size, niter)

    def get_input_source(self):
        return self.input_source

    # def get_target_source(self):
    #     return self.target_source


class CompositeLayerWithSource(CompositeLayer):
    def get_input_source(self):
        return tuple([layer.get_input_source() for layer in self.components])

    # def get_target_source(self):
    #     return tuple([layer.get_target_source() for layer in self.layers])

    # def set_input_space(self, space):
    #     self.input_space = space

    #     for layer, component in zip(self.layers, space.components):
    #         layer.set_input_space(component)

    #     self.output_space = CompositeSpace(tuple(layer.get_output_space()
    #                                              for layer in self.components))

    # def fprop(self, state_below):
    #     return tuple(layer.fprop(component_state) for
    #                  layer, component_state in zip(self.layers, state_below))

    def get_monitoring_channels(self):
        return OrderedDict()