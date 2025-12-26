RULES = {
    "Replay / Double Execution Risk": [
        "nonce",
        "confirm",
        "already_confirm",
        "ENONCE_ALREADY_CONFIRM"
    ],
    "Weak Access Control": [
        "public entry fun",
        "signer"
    ],
    "Potential Missing State Validation": [
        "state",
        "assert!"
    ],
    "Event Before Final State": [
        "event::emit"
    ],
    "Execute Before Verify": [
        "execute",
        "transfer"
    ]
}
