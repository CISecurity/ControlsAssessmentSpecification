15.6: Disable Peer-to-Peer Wireless Network Capabilities on Wireless Clients
============================================================================
Disable peer-to-peer (ad hoc) wireless network capabilities on wireless clients.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of wireless clients (subset of hardware inventory)
#. Approved configurations to disable peer-to-peer (adhoc) wireless network capabilities

Operations
----------
#. For each wireless client in Input 1, compare its configuration against the appropriate approved configuration(s) from Input 2.
#. Make a list of wireless clients that adhere to the approved configurations (M1)
#. Make a list of wireless clients that do not (M2), noting the deviations from the approved configurations.

Measures
--------
* M1 = List of wireless clients properly configured to disable peer-to-peer (adhoc) wireless network capabilities (compliant list)
* M2 = List of wireless clients not properly configured to disable peer-to-peer (adhoc) wireless network capabilities (non-compliant list)
* M3 = Count of wireless clients with peer-to peer (adhoc) wireless network capabilities disabled (count of M1)
* M4 = Total count of wireless clients (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of wireless clients with peer-to-peer (adhoc) wireless network capabilities
	    | disabled
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
