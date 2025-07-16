# LedgerForge: Decentralized Algorithmic Trading Framework

LedgerForge is a cutting-edge, decentralized, event-driven crypto bot framework designed for algorithmic trading strategies. It leverages WebSockets for real-time market data, serverless functions for automated execution, and on-chain smart contract automation for secure and transparent order management. This framework empowers developers and traders to build sophisticated trading bots that operate with increased autonomy and reduced reliance on centralized exchange infrastructure.

The core purpose of LedgerForge is to provide a modular and extensible platform for creating and deploying algorithmic trading strategies in the decentralized finance (DeFi) ecosystem. It addresses the limitations of traditional trading bots by integrating directly with blockchain technology, offering benefits such as reduced counterparty risk, enhanced transparency, and the ability to execute complex trading logic programmatically through smart contracts. LedgerForge aims to democratize access to sophisticated trading tools and strategies, making them available to a wider audience within the crypto community. Users can create trading strategies reacting to real-time market data, trigger automated actions based on predefined conditions, and ultimately execute trades on decentralized exchanges (DEXs) or other on-chain trading venues.

LedgerForge achieves its goals by providing a robust and flexible architecture built on a foundation of event-driven programming. The framework utilizes WebSockets to subscribe to real-time market data feeds, capturing price fluctuations, order book updates, and other relevant information. This data is then processed by serverless functions, which act as autonomous agents responsible for analyzing market conditions and making trading decisions based on pre-defined algorithmic strategies. These decisions can then be relayed to smart contracts deployed on a blockchain network, enabling the secure and automated execution of trades. This complete cycle, from data ingestion to on-chain execution, allows for truly decentralized and autonomous trading strategies.

## Key Features

*   **Real-time Market Data Integration:** Leverages WebSockets to subscribe to real-time market data streams from various cryptocurrency exchanges and data providers. The framework supports multiple exchange APIs and data formats and offers configurable data filtering and aggregation. For example, accessing Binance's websocket API to get price information for BTC/USDT would involve establishing a persistent connection using the `websockets` library and parsing the JSON responses for price updates. The `data_stream` module handles this.
*   **Serverless Function Automation:** Employs serverless functions (e.g., AWS Lambda, Google Cloud Functions) to execute trading logic and make automated trading decisions. These functions are triggered by real-time market data events and can perform complex technical analysis, pattern recognition, and risk management calculations. The deployment of these serverless functions are handled by Terraform scripts for infrastructure as code.
*   **On-Chain Smart Contract Execution:** Integrates with smart contracts deployed on blockchain networks (e.g., Ethereum, Polygon) to securely and transparently execute trading orders. The framework provides a secure interface for interacting with smart contracts, handling transaction signing, gas estimation, and error handling. Functions in the `smart_contract_interaction` module are used to interact with deployed smart contracts.
*   **Modular Architecture:** Designed with a modular architecture, allowing developers to easily extend and customize the framework to support new exchanges, data sources, and trading strategies. The modular design promotes code reusability and maintainability.
*   **Event-Driven Programming Model:** Utilizes an event-driven programming model, enabling real-time responsiveness to market changes and efficient resource utilization. The framework's core logic revolves around reacting to events triggered by market data updates.
*   **Backtesting Capabilities:** Includes integrated backtesting capabilities, allowing developers to evaluate and optimize trading strategies against historical market data. The backtesting module, `backtest`, simulates trading scenarios to assess strategy performance.
*   **Risk Management Tools:** Provides built-in risk management tools to protect capital and manage trading exposure. These tools include stop-loss orders, take-profit orders, and position sizing algorithms.

## Technology Stack

*   **Python:** The primary programming language used for the framework's core logic, including data processing, algorithmic trading strategies, and smart contract interaction.
*   **WebSockets (e.g., `websockets` library):** Used for establishing real-time communication channels with cryptocurrency exchanges and data providers, enabling the streaming of market data.
*   **Serverless Functions (e.g., AWS Lambda, Google Cloud Functions):** Provides the infrastructure for executing automated trading logic and making trading decisions in a scalable and cost-effective manner.
*   **Web3.py:** A Python library for interacting with Ethereum-compatible blockchains, enabling communication with smart contracts and execution of on-chain transactions.
*   **Solidity (Smart Contracts):** Used to write and deploy smart contracts on blockchain networks, enabling the secure and automated execution of trading orders.
*   **Terraform:** Used for infrastructure as code to deploy and manage serverless functions and other cloud resources.

## Installation

1.  **Clone the repository:**
    git clone https://github.com/jjfhwang/LedgerForge.git
    cd LedgerForge

2.  **Install Python dependencies:**
    python -m venv venv
    source venv/bin/activate  (or venv\Scripts\activate on Windows)
    pip install -r requirements.txt

3.  **Install Terraform:** Download and install Terraform from the official website: [https://www.terraform.io/downloads.html](https://www.terraform.io/downloads.html). Ensure Terraform is added to your system's PATH.

4.  **Configure cloud provider credentials:** Configure your AWS or Google Cloud credentials (depending on your serverless function provider) using the appropriate CLI tools (e.g., `aws configure`, `gcloud auth application-default login`).

## Configuration

1.  **Environment Variables:** Configure the following environment variables:
    *   `EXCHANGE_API_KEY`: Your API key for the cryptocurrency exchange.
    *   `EXCHANGE_API_SECRET`: Your API secret for the cryptocurrency exchange.
    *   `WEB3_PROVIDER_URI`: The URI of your Web3 provider (e.g., Infura, Alchemy).
    *   `SMART_CONTRACT_ADDRESS`: The address of the deployed smart contract.
    *   `PRIVATE_KEY`: The private key of the Ethereum address used for signing transactions.

    These environment variables can be set in a `.env` file or directly in your shell environment.

2.  **Smart Contract Configuration:** Deploy the smart contract on your chosen blockchain network and configure the `SMART_CONTRACT_ADDRESS` environment variable accordingly. Ensure the smart contract's ABI (Application Binary Interface) is available for interaction using `web3.py`.

3.  **Serverless Function Configuration:** Configure the serverless function to access the necessary environment variables and to communicate with the smart contract.

## Usage

Example: Subscribing to market data and printing the latest price:

from data_stream import MarketDataStream

def price_callback(price):
    print(f"Latest price: {price}")

market_data_stream = MarketDataStream("Binance", "BTC/USDT", price_callback)
market_data_stream.start()

# To interact with the deployed smart contract:

from smart_contract_interaction import SmartContractInterface

contract_interface = SmartContractInterface(
    WEB3_PROVIDER_URI,
    SMART_CONTRACT_ADDRESS,
    PRIVATE_KEY
)

# Example: Place a market order
transaction_hash = contract_interface.place_market_order("BTC", 0.1)
print(f"Transaction Hash: {transaction_hash}")

(Replace WEB3_PROVIDER_URI, SMART_CONTRACT_ADDRESS and PRIVATE_KEY with actual values.)

Further API documentation and examples can be found in the `docs` directory.

## Contributing

We welcome contributions to LedgerForge! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Follow the existing code style and conventions.
*   Include unit tests for any new code.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/LedgerForge/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the technologies used in this project.