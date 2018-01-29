master_doc = 'index'


import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

import re
scv_whitelist_branches = ("master", "dev")
scv_whitelist_tags = (re.compile(r'^v\d+\.\d+\.\d+$'),)

scv_greatest_tag = True

scv_show_banner = True
scv_banner_greatest_tag = True
