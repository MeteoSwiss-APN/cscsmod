==================
CSCS Module Loader
==================



Utility function to manage modules Package at CSCS.

Features
--------

* Full access to the module command (for detail see man module)

Quick Start
-----------

To use CSCS Module Loader in a project::

    from cscsmod import module
    import sh
    
    # Print available netcdf modules
    print(module("avail", "netcdf"))
    
    # Load the netcdf module for example
    module("load", "netcdf")
    
    # Execute the just loaded command ncdump 
    sh.ncdump("--help")

Valid arguments for the function ``module`` are the same as 
for the module command. For further details see its manpage 
(``man module``).

The function ``module`` returns the output of the module
command.

Credits
-------

This package was created with Cookiecutter_ and the `MeteoSwiss-APN/mch-python-blueprint`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`MeteoSwiss-APN/mch-python-blueprint`: https://github.com/MeteoSwiss-APN/mch-python-blueprint
