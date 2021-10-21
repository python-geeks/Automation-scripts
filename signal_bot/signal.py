from pydbus import SystemBus
from gi.repository import GLib
bus = SystemBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal', object_path='/org/asamk/Signal')

def reply_ping(timestamp, source, groupID, message, attachments):
    signal.sendMessage(message, [], [source])

signal.onMessageReceived = reply_ping
loop.run()

//for debugging
//ps aux | grep signal-cli
kill PROCESS_ID