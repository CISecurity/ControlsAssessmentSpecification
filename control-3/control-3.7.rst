3.7: Establish and Maintain a Data Classification Scheme
==================================
Establish and maintain an overall data classification scheme for the enterprise. Enterprises may use labels, such as “Sensitive”, “Confidential” and “Public”, and classify their data according to those labels. Review and update the classification scheme annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 3.1: Establish and Maintain a Data Management Process
* Safeguard 3.2: Establish and Maintain a Data Inventory

Inputs
------
#. Enterprise's data classification scheme
#. :code:`GV17`: Sensitive Data types
#. :code:`GV12`: Sensitive Data Inventory
#. Date of last review of the data classification scheme

Operations
----------
#. Check if the enterprise has a data classification scheme (Input 1).
	#. If Input 1 exists M = 1
	#. Otherwise M1 = 0
#. Using :code:`GV17`determine if the enterprise has a way to categorize the type of data within the classification scheme
	#. Enumerate the sensitivity types that are included in the classification scheme (M2)
	#. Enumerate the sensitivity types that are not included in the classification scheme (M3)
#. Compare :code:`GV12` and Input 1
	#. Identify and enumerate data that contains an accurate classification per the classification scheme (M4)
	#. Identify and enumerate data that does not contain a classsification or contains an innaccurate classification per the classification scheme (M5)
#. Compare the current date to that provided in Input 4.  Note the timeframe in months. (M8)

Measures
--------
* M1 = Output of Operation 1 
* M2 = Sensitivity addressed by the classification scheme
* M3 = Sensitivity not addressed by the classification scheme
* M4 = Data properly catergorized per the classification scheme
* M5 = Data lacking or improperly categorized per the classification scheme
* M6 = Count of items in :code:`GV17`
* M7 = Count of :code:`GV12`
* M8 = Count of months since last review of the classification scheme

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M8 is greater than twelve, this safeguard receives a failing score. The other metrics don't apply.

Completeness of Classification Scheme
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of sensitive data types covered within the classification
	  - | scheme.
	* - **Calculation**
	  - :code:`M2 / M6`

Implementation of the Classification Scheme
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of data categorized using the classification scheme.
	* - **Calculation**
	  - :code:`M4 / M7`

.. history
.. authors
.. license
