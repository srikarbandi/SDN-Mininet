from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str

log = core.getLogger()

class SDNController(object):
    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self, event):
        log.info("Switch %s connected.", dpid_to_str(event.dpid))

    def _handle_PortStatus(self, event):
        log.info("Link DOWN detected on Switch %s", dpid_to_str(event.dpid))
        msg = of.ofp_flow_mod(command=of.OFPFC_DELETE)
        event.connection.send(msg)
        log.info("Cleared OpenFlow rules for Switch %s", dpid_to_str(event.dpid))

def launch():
    core.registerNew(SDNController)
