1.6: Address Unauthorized Assets
================================
Ensure that unauthorized assets are either removed from the network, quarantined or the inventory is updated in a timely manner.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Respond
	  - 1, 2, 3

Status
------
Draft

Inputs
-----------
#. A list of discovered assets not currently present in the asset inventory ("unauthorized" assets).
#. An updated asset inventory
#. An organizationally defined timeframe for "timely"
#. (Optional) Measurement results would be more useful if the disposition of the items (removed, added to inventory, quarantined, etc.) was provided to be verified, but this is not absolutely necessary.

Operations
----------
If the optional disposition list is provided, the checkes would be tailored to those dispositions.  For the following, assume no disposition list is available:

#. At the timeframe specified by Input 3, for each unauthorized asset (Input 1), check to see if the asset is present in the updated asset inventory (Input 2).
#. For those Input 1 items that are not in Input 2, scan the network to determine if the item is still reachable on the network.

Assumptions
^^^^^^^^^^^
(TBD) If the item is not reachable, assume it has been removed from the network and therefore dealt with?

Measures
--------
* M1 = The number of items from Input 1 **NOT** passing either Operation 1 or Operation 2
* M2 = The total number of items in Input 1

Metrics
-------

Unauthorized Asset Remediation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of unaccounted for, unauthorized assets, to the total assets in the asset 
	    | inventory
	* - **Calculation**
	  - | If the value of M2 is 0, there are no unauthorized assets that remain unaccounted for.
	    | In this case, the value of the metric is 1.  Otherwise, the value is :code:`(M2 - M1) / M2`

.. history
.. authors
.. license