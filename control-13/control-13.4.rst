13.4: Only Allow Access to Authorized Cloud Storage or Email Providers
======================================================================
Only allow access to authorized cloud storage or email providers.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Data
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
#. List of endpoints. For each, include the configuration locations that restrict which cloud providers the endpoint can access (this could be a firewall, etc.)
#. List of cloud storage providers (this list should be as complete as possible and should indicate whether each provider is allowed or prohibited)
#. List of cloud email providers (this list should be as complete as possible and should indicate whether each provider is allowed or prohibited)
#. Organization's security policy regarding access to cloud storage and cloud email providers, including a list of which ones are allowed

Operations
----------
#. For each of the endpoint configuration locations identified in Input 1, identify which of the cloud storage providers from Input 2 are reachable based on the configuration at that location, creating a list of reachable cloud storage providers by configuration location (M1). Mark each of the configuration locations in the list as either compliant (if it does not allow access to prohibited cloud storage providers), or non-compliant (if it allows access to at least one of the prohibited cloud storage providers).
#. For each of the endpoint configuration locations identified in Input 1, identify which of the cloud email providers from Input 3 are reachable based on the configuration at that location, creating a list of reachable cloud email providers by configuration location (M2). Mark each of the configuration locations in the list as either compliant (if it does not allow access to prohibited cloud storage providers), or non-compliant (if it allows access to at least one of the prohibited cloud storage providers).
#. For each endpoint in Input 1, check the status of each of that endpoint's configuration locations in M1 and M2, and create a count of the endpoints that have configuration locations that are all compliant (M3).
#. Manually review the organization's security policy provided in Input 4 to ensure that it properly outlines the organization's rules for accessing cloud storage and cloud email providers, including identifying which providers are allowed and which are prohibited. Score this review as M5 (could be a binary 1 for adequate, 0 for inadequate; or a more nuanced score could be generated).

Measures
--------
* M1 = List of reachable cloud storage providers by configuration location
* M2 = List of reachable cloud email providers by configuration location
* M3 = Count of endpoints for which all their configuration locations are compliant
* M4 = Total count of endpoints (count of Input 1)
* M5 = Score resulting from the manual review of the cloud provider access policy

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of endpoints with cloud provider access properly limited to the total number of
	    | endpoints
	* - **Calculation**
	  - :code:`M3 / M4`

Manual Review
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Manual policy review included for this Sub-Control because it is not feasible to 
	    | identify (and therefore check for) all cloud storage and email providers.
	* - **Calculation**
	  - :code:`M5`

.. history
.. authors
.. license