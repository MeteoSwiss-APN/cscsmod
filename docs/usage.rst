=====
Usage
=====

To use CSCS Module Loader in a project::

    from cscsmod import module
    
    # To load the netcdf module for example
    module("load", "netcdf")

Valid arguments for the function ``module`` are the same as 
for the module command. For further details see its manpage 
(``man module``).

The function ``module`` returns the output of the module
command.


