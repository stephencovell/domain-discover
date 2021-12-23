# ========================================================
#  
# Created by Stephen Covell on 21/12/21 @ 12:00 Hrs
#
# Project Title: Domain Discover
# Project Description:
#   To discover sub-domains and domains on a given domain.
#
# ========================================================

import yaml

def read_config():
    with open ('../config.yaml', "r") as f:
        return yaml.safe_load(f)

read_config()