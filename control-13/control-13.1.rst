13.1: Maintain an Inventory of Sensitive Information
=========================================================
Maintain an inventory of all sensitive information stored, processed, or transmitted by the organization’s technology systems, including those located on-site or at a remote service provider.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Identify
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* TBD

Inputs
-----------
#. The organizationally-defined classification scheme
#. The data set of sensitive information for which the organization is responsible, mapped to the classification scheme defined by Input 1
#. A mapping of an organization's endpoints/systems containing sensitive information classified by Input 2.

Operations
----------
#. Create the mappings of information deemed "sensitive" to the organization to the organization's classification scheme.
#. Create the mappings of classified, sensitive information to the endpoints/systems on which that information is stored

Measures
--------
* M1 = 1 if the mappings of "sensitive" information to the organization's classification scheme is provided; 0 otherwise
* M2 = 1 if the mappings of classified, sensitive information to the endpoints/systems on which it resides is provided; 0 otherwise

Metrics
-------

Existence
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure the inventory of all sensitive information, cross-referenced with the systems
	    | on which that information is kept, exists.
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license