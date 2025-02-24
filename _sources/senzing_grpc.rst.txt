senzing_grpc
============

The `senzing_grpc`_ Python package has 5 major modules / classes.
Senzing objects are created using an `Abstract Factory Pattern`_.

.. list-table:: Senzing classes
   :widths: 20 20 60
   :header-rows: 1

   * - Module
     - Class
     - Creation
   * - szconfig
     - SzConfigGrpc
     - `sz_config = sz_abstract_factory.create_config()`
   * - szconfigmanager
     - SzConfigManagerGrpc
     - `sz_configmanager = sz_abstract_factory.create_configmanager()`
   * - szdiagnostic
     - SzDiagnosticGrpc
     - `sz_diagnostic = sz_abstract_factory.create_diagnostic()`
   * - szengine
     - SzEngineGrpc
     - `sz_engine = sz_abstract_factory.create_engine()`
   * - szproduct
     - SzProductGrpc
     - `sz_product = sz_abstract_factory.create_product()`

For the full implementation of the documentation examples, visit the source code on
`GitHub`_.

szabstractfactory
-----------------

.. automodule:: senzing_grpc.szabstractfactory
   :members:
   :undoc-members:
   :show-inheritance:

szconfig
--------

.. automodule:: senzing_grpc.szconfig
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

szconfigmanager
---------------

.. automodule:: senzing_grpc.szconfigmanager
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

szdiagnostic
------------

.. automodule:: senzing_grpc.szdiagnostic
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

szengine
--------

.. automodule:: senzing_grpc.szengine
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

szproduct
---------

.. automodule:: senzing_grpc.szproduct
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. _Abstract Factory Pattern: https://en.wikipedia.org/wiki/Abstract_factory_pattern
.. _GitHub: https://github.com/senzing-garage/sz-sdk-python-grpc/tree/main/examples
.. _senzing-core: https://garage.senzing.com/sz-sdk-python-core
.. _senzing_grpc: https://github.com/senzing-garage/sz-sdk-python-grpc