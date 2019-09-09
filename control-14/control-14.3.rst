14.3: Disable Workstation-to-Workstation Communication
=========================================================
Disable all workstation-to-workstation communication to limit an attacker’s ability to move laterally and compromise neighboring systems, through technologies such as private VLANs or micro segmentation.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints.  For each endpoint, include the corresponding policy configuration locations that are used to restrict workstation to workstation communication (network device configurations, workstation configurations, virtual network configurations, etc.)
#. Approved configuration(s) for each type of configuration in Input 1

Operations
----------
#. For each endpoint, check each corresponding policy configuration location specified in Input 1, comparing the configuration at that location against the appropriate configurations provided in Input 2.
#. Create a list of endpoints for which all of the endpoint's corresponding policy configuration points are configured in accordance with the approved configurations (M1), noting the approved configurations that were used for each.
#. Create a list of the endpoints that have at least one policy configuration points that is not configured appropriately (M2) noting the deviations from the approved configurations.

Measures
--------
* M1 = List of endpoints with all workstation to workstation policy configuration points configured appropriately (compliant list)
* M2 = List of endpoints with at least one misconfigured workstation to workstation policy configuration point (non-compliant list)
* M3 = Count of endpoints with all policy configuration points configured appropriately (count of M1)
* M4 = Total count of endpoints (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints correctly configured to restrict workstation to workstation
	    | communication to the total number of endpoints.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license