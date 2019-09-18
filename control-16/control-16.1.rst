16.1: Maintain an Inventory of Authentication Systems
=========================================================
Maintain an inventory of each of the organization’s authentication systems, including those located on-site or at a remote service provider.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Identify
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
-----------
#. Inventory of the organization's authentication systems (including onsite and remote)

Operations
----------
#. Verify that the inventory of authentication systems (Input 1) was provided.  The presence or absence of this list will be indicated with M1.
#. (Optional) Manually review Input 1 to ensure that it includes all of the authentication systems utilized by the organization, including those located onsite and by remote service providers (for instance, be sure authentication systems for any cloud services used by the organization are included).  An optional manual score can be generated from this review and provided as M2.

Measures
--------
* M1 = 1 if the inventory was provided, 0 if it was not provided
* M2 = (Optional) Indicates manual review of the authentication systems inventory was performed; 0 otherwise

Metrics
-------

Existence
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does the organization's authentication systems inventory exist?
	* - **Calculation**
	  - :code:`M1`

Manual Review
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Was a manual review of the organization's systems inventory performed?
	* - **Calculation**
	  - :code:`M2`

.. history
.. authors
.. license