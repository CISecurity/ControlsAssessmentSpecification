CIS Control 1: Inventory and Control of Enterprise Assets
=======================================================

Actively manage (inventory, track, and correct) all enterprise assets (end-user devices, including portable and mobile; network devices; non-computing/Internet of Things (IoT) devices; and servers) connected to the infrastructure, physically, virtually, remotely, and those within cloud environments, to accurately know the totality of assets that need to be monitored and protected within the enterprise. This will also support identifying unauthorized and unmanaged assets to remove or remediate.

**Why is this CIS Control Critical?**

Enterprises cannot defend what they do not know they have. Managed control of all enterprise assets also plays a critical role in security monitoring, incident response, system backup, and recovery. Enterprises should know what data is critical to them, and proper asset management will help identify those enterprise assets that hold or manage this critical data, so appropriate security controls can be applied. 

External attackers are continuously scanning the internet address space of target enterprises, premise-based or in the cloud, identifying possibly unprotected assets attached to enterprises' networks. Attackers can take advantage of new assets that are installed, yet not securely configured and patched. Internally, unidentified assets can also have weak security configurations that can make them vulnerable to web or email-based malware; and adversaries can leverage weak security configurations for traversing the network, once they are inside.

Additional assets that connect to the enterprise’s network (e.g., demonstration systems, temporary test systems, guest networks, etc.) should be identified and/or isolated, in order to prevent adversarial access from affecting the security of enterprise operations.

Large, complex, dynamic enterprises understandably struggle with the challenge of managing intricate, fast-changing environments. However, attackers have shown the ability, patience, and willingness to “inventory and control” our enterprise assets at very large scale in order to support their opportunities.

Another challenge is that portable end-user devices will periodically join a network and then disappear, making the inventory of currently available assets very dynamic. Likewise, cloud environments and virtual machines can be difficult to track in asset inventories when they are shut down or paused.
Another benefit of complete enterprise asset management is supporting incident response. Both when investigating the origination of network traffic from an asset on the network, and to be able to identify all potentially vulnerable, or impacted, assets of similar type or location during an incident.


.. toctree::
   :maxdepth: 1
   :name: toc-control-1

   1.1: Establish and Maintain Detailed Enterprise Asset Inventory <control-1.1>
   1.2: Address Unauthorized Assets <control-1.2>
   1.3: Utilize an Active Discovery Tool <control-1.3>
   1.4: Use Dynamic Host Configuration Protocol (DHCP) Logging to Update Enterprise Asset Inventory <control-1.4>
   1.5: Use a Passive Asset Discovery Tool <control-1.5>
   
.. history
.. authors
.. license
