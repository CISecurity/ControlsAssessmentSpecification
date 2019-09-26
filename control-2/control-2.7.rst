2.7: Utilize Application Whitelisting
=========================================================
Utilize application whitelisting technology on all assets to ensure that only authorized software executes and all unauthorized software is blocked from executing on assets.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
------
#. The list of endpoints
#. The list of authorized software

Operations
----------
#. Enumerate endpoints capable of leveraging whitelisting technology (e.g. some network and other devices may not enable third-party software installation or otherwise have constrained environments precluding the use of whitelisting software)
#. For each eligible endpoint (operation 1), examine the software inventory for whitelisting applications related to that endpoint, noting endpoints with and without whitelisting capabilities
#. For each endpoint with whitelisting capabilities, examine the whitelisting software's configuration to ensure only authorized software is considered executable and that attempts to execute unauthorized software is blocked, noting appropriately and inappropriately configured software

Measures
--------
* M1 = List of endpoints capable of leveraging whitelisting technology
* M2 = List of endpoints with whitelisting capabilities installed
* M3 = List of endpoints without whitelisting capabilities installed
* M4 = List of endpoints with appropriately configured whitelisting capabilities
* M5 = List of endpoints with inappropriately configured whitelisting capabilities
* M6 = Count of endpoints capable of leveraging whitelisting technology (count of M1)
* M7 = Count of endpoints with whitelisting capabilities installed (count of M2)
* M8 = The number of endpoints without whitelisting capabilities installed (count of M3)
* M9 = Count of endpoints with appropriately configured whitelisting capabilities (count of M4)
* M10 = Count of endpoints with inappropriately configured whitelisting capabilities (count of M5)


Metrics
-------

Whitelisting Installation Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with whitelisting capabilities installed to the number of
	    | whitelisting-eligible endpoints
	* - **Calculation**
	  - :code:`M7 / M6`

Whitelisting Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with appropriately configured whitelisting capabilities
	    | to the number of endpoints with whitelisting capabilities
	* - **Calculation**
	  - :code:`M9 /  M7`

.. history
.. authors
.. license
