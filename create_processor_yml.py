#!/bin/env python3

import yaml
import os

breach_condition = os.environ['param_breach_condition']
load_condition = os.environ['param_load_condition']

processor_dict = {'$1': {'ExtractInundationCensusTracts':
                              {'breach_condition': breach_condition,
                               'load_condition': load_condition,
                               'floodmap_path': '/compute_shared/Aging_Dams/inundation_maps/NID_FIM_'+load_condition+'_'+breach_condition,
                               'dam_ids': os.environ['param_dam_ids']}}}

with open('/job/executable/extractinundationcensustracts.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
