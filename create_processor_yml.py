#!/bin/env python3

import yaml
import os

processor_dict = {'$1': {'ExtractInundationCensusTracts':
                              {'breach_condition': os.environ['breach_condition'],
                               'load_condition': os.environ['load_condition'],
                               'floodmap_path': '/compute_shared/Aging_Dams/inundation_maps/NID_FIM_'+os.environ['param_load_condition']+'_'+os.environ['param_breach_condition'],
                               'dam_ids': os.environ['param_dam_ids']}}}

with open('/job/executable/extractinundationcensustracts.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
