module.exports = {
    contracts_build_directory: "./build/contracts",
    compilers: {
        solc: {
            version: "0.8.26",
        }
    },
    db: {
        enabled: false
    },
	plugins: [
        "@chainsafe/truffle-plugin-abigen",
        "truffle-plugin-stdjsonin"
    ]
};
