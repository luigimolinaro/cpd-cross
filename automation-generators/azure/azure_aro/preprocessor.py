from generatorPreProcessor import GeneratorPreProcessor


def preprocessor(attributes=None, fullConfig=None, moduleVariables=None):
    g = GeneratorPreProcessor(attributes,fullConfig,moduleVariables)

    #Level 1
    g('name').isRequired()
    g('resource_group').isRequired()
    g('vnet').isRequired()
    g('control_plane').isRequired()
    g('compute').isRequired()

    #Level 2
    if len(g.getErrors()) == 0:    
        g('resource_group.name').isRequired()
        g('resource_group.location').isRequired()    
        g('vnet.name').isRequired()
        g('vnet.address_space').isRequired()    
        g('control_plane.subnet').isRequired()    
        g('control_plane.vm').isRequired()    
        g('compute.subnet').isRequired()   
        g('compute.vm').isRequired()

    # Level 3:
    if len(g.getErrors()) == 0:    
        g('control_plane.subnet.name').isRequired()
        g('control_plane.subnet.address_prefixes').isRequired()
        g('control_plane.vm.size').isRequired()
        g('compute.subnet.name').isRequired()
        g('compute.subnet.address_prefixes').isRequired()
        g('compute.vm.size').isRequired()
        g('compute.vm.disk_size_gb').isRequired()
        g('compute.vm.count').isRequired()  

    result = {
        'attributes_updated': g.getExpandedAttributes(),
        'errors': g.getErrors()
    }
    return result