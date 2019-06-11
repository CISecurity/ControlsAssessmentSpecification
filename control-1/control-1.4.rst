1.4: Maintain Detailed Asset Inventory
======================================
Maintain an accurate and up-to-date inventory of all technology assets with the potential to store or process information. This inventory shall include all assets, whether connected to the organization’s network or not.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 1, 2, 3

Status
------
Draft

Inputs
-----------
#. The organization's current inventory list (the "to be checked" list).
#. A "ground truth" inventory list to compare with input 1.  This list would be enhanced by manual verification, but a tool-generated or aggregated list could be substituted here.  This should be an aggregation of the devices detected over a period of time, preferably not from a single scan.
#. A write-up of the procedure for adding or removing assets to or from the inventory - only for manual review.

Assumptions
^^^^^^^^^^^
* Devices belonging to the organization, but not connected to the organization's network, require manual discovery in order to be included in the "ground truth" inventory.

Operations
----------
* If Input 1 is not provided, this sub-control is measured at a 0 (complete fail).
* If Input 2 is not provided, no true accuracy measurement can be made for this sub-control.

Measures
--------
* M1 = The number of items in the intersection of Input 1 and Input 2
* M2 = The number of items in Input 2

Metrics
-------

Accuracy Score
^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of the "ground truth" inventory is accounted for in the organization's 
	    | current asset inventory?
	* - **Answer**
	  - | A positive percentage value greater than or equal to 0, and less than or equal to 100%.
	    | A value of "0" would indicate that none of the discovered assets have been inventoried; 
	    | a value of "100" indicates that all assets connected to the organization's network are 
	    | accounted for in the asset inventory.
	* - **Calculation**
	  - :code:`(M1/M2) * 100%`


Procedure Review
^^^^^^^^^^^^^^^^
Second, manual review/rating of the inventory procedures, to include adding and removing assets, and the time allowable or expected, after acquisition or disposal of assets.


.. history
.. authors
.. license