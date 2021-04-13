15.3: Classify Service Providers
=========================================================
Classify service providers. Classification consideration may include one or more characteristics, such as data sensitivity, data volume, availability requirements, applicable regulations, inherent risk, and mitigated risk. Update and review classifications annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 15.1: Establish and Maintain an Inventory of Service Providers
* Safeguard 15.2: Establish and Maintain a Service Provider Management Policy

Inputs
-----------
#. :code:`GV44`: Service Provider Inventory List
#. :code:`GV45`: Service Provider Management Policy
#. :code:`GV46`: Date of last review or update to service provider inventory


Operations
----------
#. Use Input 2 :code:`GV45` to determine if the enterprise policy includes classification process of service providers by one or more characteristics
	#. If the process exists, M1 = 1
	#. If the process does not exist, M1 = 0 
#. Compare date of Input 3 :code:`GV46` to current date and capture timeframe in months (M2)
#. Review Input 1 :code:`GV45` and determine whether service providers are classified using one or more characteristic per the enterprise's policy
	#. Identify and enumerate service providers with an assigned classification (M4)
	#. Identify and enumerate service providers without a classification (M5)

Measures
--------
* M1 = Output of Operation 1
* M2 = Timeframe since last update or review of service provider inventory
* M3 = Count of service providers in inventory
* M4 = Count of service providers with classification
* M5 = Count of service providers without classification

Metrics
-------
* If M1 is a 0, this safeguard receives a failing score. The other metrics don't apply.
* If M2 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of service providers with a classification
	* - **Calculation**
	  - :code:`M4 / M3`


.. history
.. authors
.. license
