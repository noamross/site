#!/usr/bin/env python
'''
Utilities for site regeneration.
'''

import os
import re
import yaml

# Template for metadata.
STANDARD_YML = 'standard_config.yml'

# Standard name for metadata files.
CONFIG_YML = '_config.yml'

# Patterns used to extract content and excerpts from compiled blog
# entries.  Using regular expressions is a hack, but is *much* simpler
# than trying to parse and un-parse the not-quite HTML.
P_BLOG_CONTENT = re.compile(r'<!--\s+start\s+content\s+-->\s+(.+)\s+<!--\s+end\s+content\s+-->', re.DOTALL)
P_BLOG_EXCERPT = re.compile(r'<!--\s+start\s+excerpt\s+-->\s+(.+)\s+<!--\s+end\s+excerpt\s+-->', re.DOTALL)

#----------------------------------------

def load_info(folder, filename=CONFIG_YML):
    '''Load metadata info file from specified directory and return content.'''
    path = os.path.join(folder, filename)
    assert os.path.isfile(path), \
           'No info file found in folder "{0}"'.format(folder)
    with open(path, 'r') as reader:
        return yaml.load(reader)
