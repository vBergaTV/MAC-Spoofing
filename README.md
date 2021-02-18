# MAC-Spoofing

Note for Windows 10: While it may appear that this script does work anymore, it does. The reason for this is that the change only appears in the Network Adapter proprieties in the Control Panel. Commands such as getmac or ipconfig will still show the original MAC address even trought it has been changed.
(NOTE: this actually appears to depend on the NIC (Network Interface Card). I tested it with my Desktop and ipconfig showed the change, however it does not show the change on my Laptop)

To see this for yourself, follow the below steps:
1. Open Control Panel
2. Click 'Network and Internet'
3. Click 'Network and Sharing Center'
4. On th panel to the left, click 'Change adapter settings' 
5. A new window'll appear showing all of the Network adapters. Right-Click the one that is currently active/enabled, and click 'Properties'
6. Near the top, click the button that says 'Configure'
7. Another window'll open. At the top, click 'Advanced' tab
