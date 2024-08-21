/**
 * Use this file to configure your Truffle project. It's common to configure
 * different networks for development, testing, and production.
 */

module.exports = {
  // Configure your networks
  networks: {
    // Local development network (e.g., Ganache)
    development: {
      host: "127.0.0.1", // Localhost (default: none)
      port: 7545,        // Standard Ethereum port (default: none)
      network_id: "*",   // Any network (default: none)
    },

    // Ropsten testnet
    ropsten: {
      provider: () => new HDWalletProvider(
        "your_mnemonic_here", // Replace with your wallet mnemonic
        `https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID` // Infura or other provider URL
      ),
      network_id: 3,       // Ropsten's network id
      gas: 5500000,        // Gas limit used for deploys
      confirmations: 2,    // Number of confirmations to wait between deployments
      timeoutBlocks: 200,  // Number of blocks before a deployment times out
      skipDryRun: true     // Skip dry run before migrations
    },

    // Mainnet (for deploying to the Ethereum main network)
    mainnet: {
      provider: () => new HDWalletProvider(
        "your_mnemonic_here", // Replace with your wallet mnemonic
        `https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID` // Infura or other provider URL
      ),
      network_id: 1,       // Mainnet's network id
      gas: 5500000,        // Gas limit used for deploys
      confirmations: 2,    // Number of confirmations to wait between deployments
      timeoutBlocks: 200,  // Number of blocks before a deployment times out
      skipDryRun: true     // Skip dry run before migrations
    }
  },

  // Configure your compilers
  compilers: {
    solc: {
      version: "0.8.0",    // Fetch exact version from solc-bin (default: truffle's version)
      settings: {          // See the solidity docs for advice about optimization and evmVersion
        optimizer: {
          enabled: true,
          runs: 200
        },
        evmVersion: "istanbul" // Target specific Ethereum Virtual Machine version
      }
    }
  },

  // Mocha testing framework configuration
  mocha: {
    timeout: 100000 // Sets a timeout for your tests (in milliseconds)
  },

  // Add plugins
  plugins: ["truffle-plugin-verify"], // Example plugin: for contract verification on Etherscan
};
