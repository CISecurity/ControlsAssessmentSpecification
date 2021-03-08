6.7: Centralize Access Control
=========================================================
Centralize access control for all enterprise assets through a directory service or SSO provider, where supported.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory

Operations
----------
#. Use :code:`GV5` to identify all directory and SSO services 
#. Use :code:`GV1` to identify and enumerate assets that support directory and SSO services (M1)
#. Check the output of Operations 1 and 2 to ensure each asset is covered by at least one directory or SSO service
	#. Identify and enumerate assets that are covered by at least one directory or SSO services (M2)
	#. Identify and enumerate assets that are not covered by at least one directory or SSO service (M3)

Measures
--------
* M1 = Count of assets capable of supporing directory and/or SSO services
* M2 = Count of assets covered by at least one directory or SSO service
* M3 = Count of assets not covered by at least one directory or SSO service

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets that can support directory and SSO service
	  - | covered by at least one directory or SSO service.
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
