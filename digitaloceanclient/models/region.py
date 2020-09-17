class Region(object):
    # The Region unique identifier
    slug = ''

    # The display name of the Region
    name = ''

    # An array which contains the identifying slugs for the sizes 
    # available in this region
    sizes = []

    # Whether new Droplets can be created in this region
    available = False

    # An array which contains features available in this region
    features = []
