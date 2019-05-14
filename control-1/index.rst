CIS Control 1: Inventory and Control of Hardware Assets
=======================================================

Actively manage (inventory, track, and correct) all hardware devices on the network so that only authorized devices are given access, and unauthorized and unmanaged devices are found and prevented from gaining access.

**Why is this CIS Control Critical?**

Attackers, who can be located anywhere in the world, are continuously scanning the address space of target organizations, waiting for new and possibly unprotected systems to be attached to the network. They are particularly interested in devices which come and go off of the enterprise’s network such as laptops or Bring-Your-Own-Device (BYOD) which might be out of synchronization with security updates or might already be compromised. Attacks can take advantage of new hardware that is installed on the network one evening but not configured and patched with appropriate security updates until the following day. Even devices that are not visible from the Internet can be used by attackers who have already gained internal access and are hunting for internal pivot points or victims. Additional systems that connect to the enterprise’s network (e.g., demonstration systems, temporary test systems, guest networks) should also be managed carefully and/or isolated in order to prevent adversarial access from affecting the security of enterprise operations.

Large, complex enterprises understandably struggle with the challenge of managing intricate, fast-changing environments. But attackers have shown the ability, patience, and willingness to “inventory and control” our assets at very large scale in order to support their opportunities.

Managed control of all devices also plays a critical role in planning and executing system backup, incident response, and recovery.

.. toctree::
   :maxdepth: 1
   :name: toc-control-1

   1.1: Utilize an Active Discovery Tool <control-1.1>
   1.2: Use a Passive Asset Discovery Tool <control-1.2>
   1.3: Use DHCP Logging to Update Asset Inventory <control-1.3>
   1.4: Maintain Detailed Asset Inventory <control-1.4>
   1.5: Maintain Asset Inventory Information <control-1.5>
   1.6: Address Unauthorized Assets <control-1.6>
   1.7: Deploy Port Level Access Control <control-1.7>
   1.8: Utilize Client Certificates to Authenticate Hardware Assets <control-1.8>
   
.. history
.. authors
.. license