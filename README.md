
# Table of Contents

1.  [naipyext](#orgcf318c9)
    1.  [Install](#orgdfcb1ab)


<a id="orgcf318c9"></a>

# naipyext

Nasy IPython Extensions.


<a id="orgdfcb1ab"></a>

## Install

    python -m install "naipyext[all]"

Add

    c.InteractiveShellApp.extensions = [
        "autoreload",
        "naipyext.autotime",
        "naipyext.be",
        "naipyext.ns",
        "naipyext.pt"
    ]

to ipython config file `$HOME/.ipython/profile_default/ipython_config.py`

