from trackers.ping_tracker import ping_tracker
from trackers.fake_tracker import fake_tracker
from trackers.ssh_tracker import ssh_tracker
from trackers.ssh_autodetect import ssh_autodetect
from trackers.ssh_autodetect_generic import ssh_autodetect_generic
from trackers.ssh_brctl import ssh_brctl
from trackers.ssh_routeros import ssh_routeros
from trackers.ssh_routeros_arp import ssh_routeros_arp
from trackers.ssh_zyxel_arp import ssh_zyxel_arp
from trackers.ssh_unifi_usg_arp import ssh_unifi_usg_arp
from trackers.http_orbi import http_orbi
from trackers.http_unifi import http_unifi

poll_methods = {
    'default': ssh_autodetect,
    'forcegeneric': ssh_autodetect_generic,
    'prefab': ssh_tracker,
    'brctl': ssh_brctl,
    'routeros': ssh_routeros,
    'routeros-arp': ssh_routeros_arp,
    'zyxel-arp': ssh_zyxel_arp,
    'unifiusg-arp': ssh_unifi_usg_arp,
    'unifi-http': http_unifi,
    'orbi-http': http_orbi,
    'dummy': fake_tracker,
    'ping': ping_tracker
}