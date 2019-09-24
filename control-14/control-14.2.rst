14.2: Enable Firewall Filtering Between VLANs
=========================================================
Enable firewall filtering between VLANs to ensure that only authorized systems are able to communicate with other systems necessary to fulfill their specific responsibilities.

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
* None

Inputs
-----------
#. List of the organization's VLANs, along with the systems (network devices, etc.) associated with administering, configuring, and filtering between them
#. Approved configuration(s) for these VLANs and related systems to enable firewall filtering between VLANs

Operations
----------
#. For each VLAN in Input 1, check each of its related systems to see if they are configured in accordance with the appropriate approved configurations from Input 2 to enable firewall filtering between VLANs.
#. Create a list of VLANs that are correctly configured (M1)
#. Create a list of VLANs that are not correctly configured (M2) noting which related systems are misconfigured and the details of the misconfiguration.

Measures
--------
* M1 = List of correctly configured VLANs (compliant list)
* M2 = List of incorrectly configured VLANs along with deviations (non-compliant list)
* M3 = Count of correctly configured VLANs (count of M1)
* M4 = Total count of VLANs (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of VLANs properly configured for firewall filtering to the total number of
	    | VLANs.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
