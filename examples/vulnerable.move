module demo::test {
    public entry fun settle_game(operator: &signer, nonce: u64) {
        event::emit(SettleEvent { nonce });
    }
}
