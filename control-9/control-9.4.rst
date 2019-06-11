9.4: Apply Host-Based Firewalls or Port-Filtering
=========================================================
Apply host-based firewalls or port-filtering tools on end systems, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Status
------
In Development

Inputs
------
#. 

Assumptions
^^^^^^^^^^^
* It is assumed that, as part of an asset inventory, the list of ports allowed to be open for a given endpoint, is available.
* It is assumed that an active testing tool is available to query an endpoint's listing of open ports.

Operations
----------
#. 

Measures
--------
* M1 = Listing of ports allowed to be open
* M2 = Listing of open ports

Metrics
-------

Unallowed Ports
^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to convey if any unallowed ports are open on a given endpoint
	    | under test.
	* - **Answer**
	  - | The calculation of this metric is determined via comparison of the list of open ports
	    | to the allowed list.
	* - **Calculation**
	  - :code:`If M2-M1`

.. history
.. authors
.. license