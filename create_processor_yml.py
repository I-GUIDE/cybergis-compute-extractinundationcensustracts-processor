#!/bin/env python3

import yaml
import os

processor_dict = {'$1': {'ExtractInundationCensusTracts':
                              {'floodmap_path': '/compute_shared/'+os.environ['param_floodmap_path'],
                               'version': os.environ['param_version']}}}

with open('/job/executable/extractinundationcensustracts.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
