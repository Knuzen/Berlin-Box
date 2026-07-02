#!/usr/bin/env python3
# Berlin-Box - autonomous Reticulum/LXMF test node
# Released under the MIT License
import os
import time
import threading
import RNS
import LXMF

APP_NAME = "BERLIN-BOX"

BASE_DIR = os.path.expanduser("~/.reticulum")
CONFIG_DIR = BASE_DIR
LXMF_STORAGE = os.path.join(BASE_DIR, "berlin_box_lxmf")
IDENTITY_FILE = os.path.join(BASE_DIR, "berlin_box_identity")

RNS.loglevel = RNS.LOG_INFO

def load_or_create_identity():
    os.makedirs(BASE_DIR, exist_ok=True)
    if os.path.exists(IDENTITY_FILE):
        return RNS.Identity.from_file(IDENTITY_FILE)
    identity = RNS.Identity()
    identity.to_file(IDENTITY_FILE)
    return identity

identity = load_or_create_identity()
os.makedirs(LXMF_STORAGE, exist_ok=True)

reticulum = RNS.Reticulum(configdir=CONFIG_DIR)

router = LXMF.LXMRouter(
    identity=identity,
    storagepath=LXMF_STORAGE,
    autopeer=True,
    name=APP_NAME
)

delivery_destination = router.register_delivery_identity(
    identity,
    display_name=APP_NAME
)

def on_message(message):
    RNS.log("LXMF Nachricht Callback ausgelöst")

    try:
        content = message.content_as_string()
    except Exception:
        content = str(message)

    RNS.log(f"Nachricht empfangen: {content}")

    reply_text = f"Antwort von {APP_NAME}: Ich habe empfangen: {content}"

    try:
        reply_destination = message.source
        reply_destination_hash = None

        if reply_destination is None:
            reply_destination_hash = message.source_hash
            RNS.log(f"Keine message.source, versuche OPPORTUNISTIC über source_hash: {reply_destination_hash.hex()}")

        reply = LXMF.LXMessage(
            destination=reply_destination,
            source=delivery_destination,
            content=reply_text,
            title=APP_NAME,
            desired_method=LXMF.LXMessage.OPPORTUNISTIC,
            destination_hash=reply_destination_hash
        )

        router.handle_outbound(reply)
        RNS.log("Antwort als OPPORTUNISTIC LXMF Nachricht in Outbound gelegt")

    except Exception as e:
        RNS.log(f"Antwort fehlgeschlagen: {e}")

router.register_delivery_callback(on_message)

def announce_loop():
    while True:
        try:
            router.announce(delivery_destination.hash)
            RNS.log("LXMF Announce gesendet")
        except Exception as e:
            RNS.log(f"Announce fehlgeschlagen: {e}")
        time.sleep(120)

threading.Thread(target=announce_loop, daemon=True).start()

RNS.log(f"{APP_NAME} online gestartet")
RNS.log(f"Identity: {identity.hash.hex()}")
RNS.log("Reticulum config: ~/.reticulum")
RNS.log("Delivery Destination registriert")
RNS.log("Warte auf Nachrichten...")

while True:
    time.sleep(1)

