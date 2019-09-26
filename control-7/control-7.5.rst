7.5: Subscribe to URLCategorization Service
=========================================================
Subscribe to URL-categorization services to ensure that they are up-to-date with the most recent website category definitions available.  Uncategorized sites shall be blocked by default.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. The organization's URL categorization service subscription.

Assumptions
^^^^^^^^^^^
* Subscription to a URL categorization service provides an organization the ability to intercept a user's intended URL, determine if it has been categorized, and allow/prevent access to that URL based on the (lack of) categorization. Potentially a browser plugin? Potentially some filtering method on a network device or the organization's network perimeter?

Operations
----------
#. A user attempts to access an uncategorized URL

Measures
--------
* M1 = 1 if the organization subscribes to URL categorization services; 0 otherwise
* M2 = 1 if access to the uncategorized URL is blocked; 1 otherwise.

Metrics
-------

Enforcement
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Calculate whether URL categorization is successfully blocking uncategorized URL access.
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license
