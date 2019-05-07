CIS Control 9: Limitation and Control of Network Ports, Protocols and Services
==============================================================================

Manage (track/control/correct) the ongoing operational use of ports, protocols, and services
on networked devices in order to minimize windows of vulnerability available to attackers

**Why is this CIS Control Critical?**

Attackers search for remotely accessible network services that are vulnerable to exploitation.
Common examples include poorly configured web servers, mail servers, file and print services,
and DNS servers installed by default on a variety of different device types, often without a
business need for the given service. Many software packages automatically install services and
turn them on as part of the installation of the main software package without informing a user or
administrator that the services have been enabled. Attackers scan for such services and attempt
to exploit these services, often attempting to exploit default user IDs and passwords or widely
available exploitation code.

.. toctree::
   :maxdepth: 1
   :name: toc-control-x

   9.1: Associate Active Ports, Services and Protocols to Asset Inventory <control-9.1>
   9.2: Ensure Only Approved Ports, Protocols and Services are Running <control-9.2>
   9.3: Perform Regular Automated Port Scans <control-9.3>
   9.4: Apply Host-Based Firewalls or Port-Filtering <control-9.4>
   9.5: Implement Application Firewalls <control-9.5>
   
.. history
.. authors
.. license