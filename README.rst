What is this?
=============
Consider is a parser for the ThinkGear protocol used by NeuroSky devices (MindSet, BrainBand and others).

Consider connects to ThinkGear Connector ("ThinkGear Connector.exe" for Windows) to get packets, so it can be used on Windows or Mac OS X easily.

See also thinkgear (https://github.com/groner/pythinkgear) that parses it more directly (not use ThinkGear Connector).


Getting started
===============
Consider can be installed with pip or easy_install from github::

    pip install https://github.com/lanius/consider/zipball/master

Firstly, start ThinkGear Connector. In the case of Windows, execute "ThinkGear Connector.exe" that is included in SDK, specify a COM port and push "Start" button.

Create Consider object, and you can get a ThinkGear packet::

    >>> from consider import Consider
    >>> con = Consider()
    >>> packet = con.get_packet()
    >>> print(packet.attention)
    16
    >>> print(packet.high_beta)
    1.90662092336e-06
    >>> print(packet)
    {'high_beta': 1.9066209233642439e-06, 'low_beta': 7.4952608883904759e-06, 'attention': 16, 'low_gamma': 4.8011397666414268e-06, 'delta': 7.1328349804389291e-06, 'meditation': 87, 'poor_signal': 0, 'high_alpha': 4.27748489073565e-07, 'high_gamma': 0.00022232596529647708, 'length': 32, 'theta': 2.0189656879665563e-06, 'low_alpha': 9.1102498345208005e-07}

You can get a packet generator for streaming::

    >>> from itertools import islice
    >>> for p in islice(con.packet_generator(), 10):
    ...     # get 10 packets
    ...     print(p.meditation, p.high_alpha, p.low_alpha)
    
	(96, 7.493017619708553e-05, 5.1031893235631287e-05)
	(99, 0.00021125955390743911, 2.6392026484245434e-06)
	(98, 5.571280894400843e-07, 5.3168583690421656e-05)
	(91, 2.5947028348127787e-07, 1.6530602806597017e-06)
	(79, 3.5061493690591305e-05, 1.1179225793966907e-06)
	(64, 1.420417902409099e-06, 2.2484807686851127e-06)
	(48, 0.00025273021310567856, 2.7587668682826916e-07)
	(32, 3.7225916003080783e-06, 3.6896562960464507e-07)
	(17, 0.00020242333994247019, 1.2374764992273413e-05)
	(7, 0.00019503712246660143, 2.0322062482591718e-05)


License
=======
Consider is licensed under the MIT Licence. See LICENSE for more details.
