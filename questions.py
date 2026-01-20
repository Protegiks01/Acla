import json
import os

from decouple import config

MAX_REPO = 30
SOURCE_REPO = "AcalaNetwork/Acala"
run_number = os.environ.get('GITHUB_RUN_NUMBER', '0')


def get_cyclic_index(run_number, max_index=100):
    """Convert run number to a cyclic index between 1 and max_index"""
    return (int(run_number) - 1) % max_index + 1


if run_number == "0":
    BASE_URL = f"https://deepwiki.com/{SOURCE_REPO}"
else:
    # Convert to cyclic index (1-100)
    run_index = get_cyclic_index(run_number, MAX_REPO)
    # Format the URL with leading zeros
    repo_number = f"{run_index:03d}"
    BASE_URL = f"https://deepwiki.com/grass-dev-pa/Acala-{repo_number}"

scope_files =[
    "modules/aggregated-dex/src/benchmarking.rs",
    "modules/aggregated-dex/src/lib.rs",
    "modules/aggregated-dex/src/weights.rs",
    "modules/asset-registry/src/benchmarking.rs",
    "modules/asset-registry/src/lib.rs",
    "modules/asset-registry/src/weights.rs",
    "modules/assethub/src/lib.rs",
    "modules/auction-manager/src/benchmarking.rs",
    "modules/auction-manager/src/lib.rs",
    "modules/auction-manager/src/weights.rs",
    "modules/cdp-engine/src/benchmarking.rs",
    "modules/cdp-engine/src/lib.rs",
    "modules/cdp-engine/src/weights.rs",
    "modules/cdp-treasury/src/benchmarking.rs",
    "modules/cdp-treasury/src/lib.rs",
    "modules/cdp-treasury/src/weights.rs",
    "modules/collator-selection/src/benchmarking.rs",
    "modules/collator-selection/src/lib.rs",
    "modules/collator-selection/src/weights.rs",
    "modules/currencies/runtime-api/src/lib.rs",
    "modules/currencies/src/benchmarking.rs",
    "modules/currencies/src/lib.rs",
    "modules/currencies/src/weights.rs",
    "modules/dex-oracle/src/benchmarking.rs",
    "modules/dex-oracle/src/lib.rs",
    "modules/dex-oracle/src/weights.rs",
    "modules/dex/src/benchmarking.rs",
    "modules/dex/src/lib.rs",
    "modules/dex/src/weights.rs",
    "modules/earning/src/benchmarking.rs",
    "modules/earning/src/lib.rs",
    "modules/earning/src/weights.rs",
    "modules/emergency-shutdown/src/benchmarking.rs",
    "modules/emergency-shutdown/src/lib.rs",
    "modules/emergency-shutdown/src/weights.rs",
    "modules/evm-accounts/src/benchmarking.rs",
    "modules/evm-accounts/src/lib.rs",
    "modules/evm-accounts/src/weights.rs",
    "modules/evm-bridge/src/lib.rs",
    "modules/evm-utility/macro/src/lib.rs",
    "modules/evm-utility/macro/tests/test.rs",
    "modules/evm-utility/src/lib.rs",
    "modules/evm/benches/orml_benches.rs",
    "modules/evm/rpc/runtime-api/src/lib.rs",
    "modules/evm/src/bench/mod.rs",
    "modules/evm/src/benchmarking.rs",
    "modules/evm/src/lib.rs",
    "modules/evm/src/precompiles/blake2/eip_152.rs",
    "modules/evm/src/precompiles/blake2/mod.rs",
    "modules/evm/src/precompiles/bn128.rs",
    "modules/evm/src/precompiles/ecrecover.rs",
    "modules/evm/src/precompiles/ecrecover_publickey.rs",
    "modules/evm/src/precompiles/identity.rs",
    "modules/evm/src/precompiles/mod.rs",
    "modules/evm/src/precompiles/modexp.rs",
    "modules/evm/src/precompiles/ripemd.rs",
    "modules/evm/src/precompiles/sha256.rs",
    "modules/evm/src/precompiles/sha3fips.rs",
    "modules/evm/src/runner/mod.rs",
    "modules/evm/src/runner/stack.rs",
    "modules/evm/src/runner/state.rs",
    "modules/evm/src/runner/storage_meter.rs",
    "modules/evm/src/runner/tagged_runtime.rs",
    "modules/evm/src/runner/tracing.rs",
    "modules/evm/src/weights.rs",
    "modules/homa-validator-list/src/benchmarking.rs",
    "modules/homa-validator-list/src/lib.rs",
    "modules/homa-validator-list/src/weights.rs",
    "modules/homa/src/benchmarking.rs",
    "modules/homa/src/lib.rs",
    "modules/homa/src/weights.rs",
    "modules/honzon-bridge/src/benchmarking.rs",
    "modules/honzon-bridge/src/lib.rs",
    "modules/honzon-bridge/src/weights.rs",
    "modules/honzon/src/benchmarking.rs",
    "modules/honzon/src/lib.rs",
    "modules/honzon/src/weights.rs",
    "modules/idle-scheduler/src/benchmarking.rs",
    "modules/idle-scheduler/src/lib.rs",
    "modules/idle-scheduler/src/weights.rs",
    "modules/incentives/src/benchmarking.rs",
    "modules/incentives/src/lib.rs",
    "modules/incentives/src/weights.rs",
    "modules/liquid-crowdloan/src/benchmarking.rs",
    "modules/liquid-crowdloan/src/lib.rs",
    "modules/liquid-crowdloan/src/weights.rs",
    "modules/loans/src/lib.rs",
    "modules/nft/src/benchmarking.rs",
    "modules/nft/src/lib.rs",
    "modules/nft/src/weights.rs",
    "modules/nominees-election/src/benchmarking.rs",
    "modules/nominees-election/src/lib.rs",
    "modules/nominees-election/src/weights.rs",
    "modules/prices/src/benchmarking.rs",
    "modules/prices/src/lib.rs",
    "modules/prices/src/weights.rs",
    "modules/session-manager/src/benchmarking.rs",
    "modules/session-manager/src/lib.rs",
    "modules/session-manager/src/weights.rs",
    "modules/support/src/assethub.rs",
    "modules/support/src/bounded.rs",
    "modules/support/src/dex.rs",
    "modules/support/src/earning.rs",
    "modules/support/src/evm.rs",
    "modules/support/src/homa.rs",
    "modules/support/src/honzon.rs",
    "modules/support/src/incentives.rs",
    "modules/support/src/lib.rs",
    "modules/support/src/mocks.rs",
    "modules/support/src/stable_asset.rs",
    "modules/transaction-pause/src/benchmarking.rs",
    "modules/transaction-pause/src/lib.rs",
    "modules/transaction-pause/src/weights.rs",
    "modules/transaction-payment/src/benchmarking.rs",
    "modules/transaction-payment/src/lib.rs",
    "modules/transaction-payment/src/weights.rs",
    "modules/xcm-interface/src/lib.rs",
    "modules/xcm-interface/src/mocks/kusama.rs",
    "modules/xcm-interface/src/mocks/mod.rs",
    "modules/xcm-interface/src/mocks/polkadot.rs",
    "modules/xnft/src/impl_transactor.rs",
    "modules/xnft/src/lib.rs",
    "modules/xnft/src/xcm_helpers.rs",
    "primitives/src/bonding/controller.rs",
    "primitives/src/bonding/error.rs",
    "primitives/src/bonding/ledger.rs",
    "primitives/src/bonding/mod.rs",
    "primitives/src/currency.rs",
    "primitives/src/evm.rs",
    "primitives/src/lib.rs",
    "primitives/src/nft.rs",
    "primitives/src/signature.rs",
    "primitives/src/task.rs",
    "primitives/src/testing.rs",
    "primitives/src/unchecked_extrinsic.rs",
    "runtime/acala/build.rs",
    "runtime/acala/src/authority.rs",
    "runtime/acala/src/benchmarks.rs",
    "runtime/acala/src/constants.rs",
    "runtime/acala/src/genesis_config_presets.rs",
    "runtime/acala/src/lib.rs",
    "runtime/acala/src/weights/mod.rs",
    "runtime/acala/src/weights/module_aggregated_dex.rs",
    "runtime/acala/src/weights/module_asset_registry.rs",
    "runtime/acala/src/weights/module_auction_manager.rs",
    "runtime/acala/src/weights/module_cdp_engine.rs",
    "runtime/acala/src/weights/module_cdp_treasury.rs",
    "runtime/acala/src/weights/module_collator_selection.rs",
    "runtime/acala/src/weights/module_currencies.rs",
    "runtime/acala/src/weights/module_dex.rs",
    "runtime/acala/src/weights/module_dex_oracle.rs",
    "runtime/acala/src/weights/module_emergency_shutdown.rs",
    "runtime/acala/src/weights/module_evm.rs",
    "runtime/acala/src/weights/module_evm_accounts.rs",
    "runtime/acala/src/weights/module_homa.rs",
    "runtime/acala/src/weights/module_homa_validator_list.rs",
    "runtime/acala/src/weights/module_honzon.rs",
    "runtime/acala/src/weights/module_idle_scheduler.rs",
    "runtime/acala/src/weights/module_incentives.rs",
    "runtime/acala/src/weights/module_liquid_crowdloan.rs",
    "runtime/acala/src/weights/module_nft.rs",
    "runtime/acala/src/weights/module_nominees_election.rs",
    "runtime/acala/src/weights/module_prices.rs",
    "runtime/acala/src/weights/module_session_manager.rs",
    "runtime/acala/src/weights/module_transaction_pause.rs",
    "runtime/acala/src/weights/module_transaction_payment.rs",
    "runtime/acala/src/weights/nutsfinance_stable_asset.rs",
    "runtime/acala/src/weights/orml_auction.rs",
    "runtime/acala/src/weights/orml_authority.rs",
    "runtime/acala/src/weights/orml_oracle.rs",
    "runtime/acala/src/weights/orml_tokens.rs",
    "runtime/acala/src/weights/orml_vesting.rs",
    "runtime/acala/src/weights/pallet_xcm.rs",
    "runtime/acala/src/xcm_config.rs",
    "runtime/common/benches/precompile.rs",
    "runtime/common/src/bench/mod.rs",
    "runtime/common/src/check_nonce.rs",
    "runtime/common/src/gas_to_weight_ratio.rs",
    "runtime/common/src/lib.rs",
    "runtime/common/src/precompile/dex.rs",
    "runtime/common/src/precompile/earning.rs",
    "runtime/common/src/precompile/evm.rs",
    "runtime/common/src/precompile/evm_accounts.rs",
    "runtime/common/src/precompile/homa.rs",
    "runtime/common/src/precompile/honzon.rs",
    "runtime/common/src/precompile/incentives.rs",
    "runtime/common/src/precompile/input.rs",
    "runtime/common/src/precompile/liquid_crowdloan.rs",
    "runtime/common/src/precompile/mod.rs",
    "runtime/common/src/precompile/multicurrency.rs",
    "runtime/common/src/precompile/nft.rs",
    "runtime/common/src/precompile/oracle.rs",
    "runtime/common/src/precompile/schedule.rs",
    "runtime/common/src/precompile/stable_asset.rs",
    "runtime/common/src/precompile/weights.rs",
    "runtime/common/src/precompile/xtokens.rs",
    "runtime/common/src/xcm_config.rs",
    "runtime/common/src/xcm_impl.rs",
    "runtime/integration-tests/src/authority.rs",
    "runtime/integration-tests/src/dex.rs",
    "runtime/integration-tests/src/evm.rs",
    "runtime/integration-tests/src/honzon.rs",
    "runtime/integration-tests/src/lib.rs",
    "runtime/integration-tests/src/nft.rs",
    "runtime/integration-tests/src/payment.rs",
    "runtime/integration-tests/src/prices.rs",
    "runtime/integration-tests/src/proxy.rs",
    "runtime/integration-tests/src/runtime.rs",
    "runtime/integration-tests/src/session_manager.rs",
    "runtime/integration-tests/src/setup.rs",
    "runtime/integration-tests/src/stable_asset.rs",
    "runtime/integration-tests/src/treasury.rs",
    "runtime/integration-tests/src/vesting.rs",
    "runtime/integration-tests/src/weights.rs",
    "runtime/karura/build.rs",
    "runtime/karura/src/authority.rs",
    "runtime/karura/src/benchmarks.rs",
    "runtime/karura/src/constants.rs",
    "runtime/karura/src/genesis_config_presets.rs",
    "runtime/karura/src/lib.rs",
    "runtime/karura/src/weights/mod.rs",
    "runtime/karura/src/weights/module_aggregated_dex.rs",
    "runtime/karura/src/weights/module_asset_registry.rs",
    "runtime/karura/src/weights/module_auction_manager.rs",
    "runtime/karura/src/weights/module_cdp_engine.rs",
    "runtime/karura/src/weights/module_cdp_treasury.rs",
    "runtime/karura/src/weights/module_collator_selection.rs",
    "runtime/karura/src/weights/module_currencies.rs",
    "runtime/karura/src/weights/module_dex.rs",
    "runtime/karura/src/weights/module_dex_oracle.rs",
    "runtime/karura/src/weights/module_emergency_shutdown.rs",
    "runtime/karura/src/weights/module_evm.rs",
    "runtime/karura/src/weights/module_evm_accounts.rs",
    "runtime/karura/src/weights/module_homa.rs",
    "runtime/karura/src/weights/module_homa_validator_list.rs",
    "runtime/karura/src/weights/module_honzon.rs",
    "runtime/karura/src/weights/module_honzon_bridge.rs",
    "runtime/karura/src/weights/module_idle_scheduler.rs",
    "runtime/karura/src/weights/module_incentives.rs",
    "runtime/karura/src/weights/module_nft.rs",
    "runtime/karura/src/weights/module_nominees_election.rs",
    "runtime/karura/src/weights/module_prices.rs",
    "runtime/karura/src/weights/module_session_manager.rs",
    "runtime/karura/src/weights/module_transaction_pause.rs",
    "runtime/karura/src/weights/module_transaction_payment.rs",
    "runtime/karura/src/weights/nutsfinance_stable_asset.rs",
    "runtime/karura/src/weights/orml_auction.rs",
    "runtime/karura/src/weights/orml_authority.rs",
    "runtime/karura/src/weights/orml_oracle.rs",
    "runtime/karura/src/weights/orml_tokens.rs",
    "runtime/karura/src/weights/orml_vesting.rs",
    "runtime/karura/src/weights/pallet_xcm.rs",
    "runtime/karura/src/xcm_config.rs",
    "runtime/mandala/build.rs",
    "runtime/mandala/src/authority.rs",
    "runtime/mandala/src/benchmark_common.rs",
    "runtime/mandala/src/benchmarks.rs",
    "runtime/mandala/src/constants.rs",
    "runtime/mandala/src/genesis_config_presets.rs",
    "runtime/mandala/src/lib.rs",
    "runtime/mandala/src/weights/mod.rs",
    "runtime/mandala/src/weights/module_aggregated_dex.rs",
    "runtime/mandala/src/weights/module_asset_registry.rs",
    "runtime/mandala/src/weights/module_auction_manager.rs",
    "runtime/mandala/src/weights/module_cdp_engine.rs",
    "runtime/mandala/src/weights/module_cdp_treasury.rs",
    "runtime/mandala/src/weights/module_collator_selection.rs",
    "runtime/mandala/src/weights/module_currencies.rs",
    "runtime/mandala/src/weights/module_dex.rs",
    "runtime/mandala/src/weights/module_dex_oracle.rs",
    "runtime/mandala/src/weights/module_earning.rs",
    "runtime/mandala/src/weights/module_emergency_shutdown.rs",
    "runtime/mandala/src/weights/module_evm.rs",
    "runtime/mandala/src/weights/module_evm_accounts.rs",
    "runtime/mandala/src/weights/module_homa.rs",
    "runtime/mandala/src/weights/module_homa_validator_list.rs",
    "runtime/mandala/src/weights/module_honzon.rs",
    "runtime/mandala/src/weights/module_idle_scheduler.rs",
    "runtime/mandala/src/weights/module_incentives.rs",
    "runtime/mandala/src/weights/module_liquid_crowdloan.rs",
    "runtime/mandala/src/weights/module_nft.rs",
    "runtime/mandala/src/weights/module_nominees_election.rs",
    "runtime/mandala/src/weights/module_prices.rs",
    "runtime/mandala/src/weights/module_session_manager.rs",
    "runtime/mandala/src/weights/module_transaction_pause.rs",
    "runtime/mandala/src/weights/module_transaction_payment.rs",
    "runtime/mandala/src/weights/nutsfinance_stable_asset.rs",
    "runtime/mandala/src/weights/orml_auction.rs",
    "runtime/mandala/src/weights/orml_authority.rs",
    "runtime/mandala/src/weights/orml_oracle.rs",
    "runtime/mandala/src/weights/orml_tokens.rs",
    "runtime/mandala/src/weights/orml_vesting.rs",
    "runtime/mandala/src/weights/pallet_xcm.rs",
    "runtime/mandala/src/xcm_config.rs",
    "modules/relaychain/src/lib.rs",
    "modules/support/src/relaychain.rs",
    "runtime/common/src/precompile/weights.rs",
]



def question_generator(target_file: str) -> str:
    """
    Generates targeted security audit questions for a specific Acala Network file.

    Args:
        target_file: The specific file path to focus question generation on
                    (e.g., "modules/cdp-engine/src/lib.rs" or "runtime/acala/src/lib.rs")

    Returns:
        A formatted prompt string for generating security questions
    """
    prompt = f"""  
# **Generate 150+ Targeted Security Audit Questions for Acala Network DeFi Platform**  
  
## **Context**  
  
The target project is **Acala Network**, a Substrate-based DeFi platform that implements a multi-runtime architecture supporting three distinct blockchain networks (Acala, Karura, Mandala) with shared infrastructure while targeting different networks with specific parameters and token economies. Acala provides comprehensive DeFi primitives including DEX, CDP engine, stablecoin protocol, liquid staking, and EVM compatibility for Ethereum dApp integration.  
  
Acala uses Substrate's FRAME pallet architecture with modules organized into functional categories: Core DeFi (CDP/Honzon system, DEX, lending), EVM layer (EVM runtime, account mapping, asset bridge), Cross-chain (XCM, asset transfers), and Infrastructure (currency management, governance, emergency controls). The system maintains security through collateralized debt positions, price oracles, liquidation mechanisms, and cross-chain consensus.  
  
## **Scope**  
  
**CRITICAL TARGET FILE**: Focus question generation EXCLUSIVELY on `{target_file}`  
  
Note: The questions must be generated from **`{target_file}`** only. If you cannot generate enough questions from this single file, provide as many quality questions as you can extract from the file's logic and interactions. **DO NOT return empty results** - give whatever questions you can derive from the target file.  
  
If you cannot reach 150 questions from this file alone, generate as many high-quality questions as the file's complexity allows (minimum target: 50-100 questions for large critical files, 20-50 for smaller files).  
  
**Full Context - Critical Acala Network Components (for reference only):**  
If a file is more than a thousand lines you can generate as many as 300+ questions as you can, but always generate as many as you can - don't give other responses.  
If there are cryptographic operations, math logic, or state transition functions, generate comprehensive questions covering all edge cases and attack vectors.  
  
### **Core Acala Network Components**  
  
```python  
core_components = [  
    # Multi-Runtime Architecture  
    "runtime/acala/src/lib.rs",                  # Acala mainnet runtime  
    "runtime/karura/src/lib.rs",                 # Karura Kusama runtime  
    "runtime/mandala/src/lib.rs",                # Mandala development runtime  
    "runtime/common/src/lib.rs",                 # Shared runtime components  
      
    # Core DeFi Modules  
    "modules/cdp-engine/src/lib.rs",             # Collateralized debt positions  
    "modules/cdp-treasury/src/lib.rs",           # CDP treasury management  
    "modules/honzon/src/lib.rs",                 # CDP lending protocol  
    "modules/auction-manager/src/lib.rs",        # Collateral and surplus auctions  
    "modules/loans/src/lib.rs",                  # Direct lending protocol  
      
    # DEX and Trading  
    "modules/dex/src/lib.rs",                    # AMM trading logic  
    "modules/aggregated-dex/src/lib.rs",         # Multi-DEX routing  
    "modules/dex-oracle/src/lib.rs",             # Price feeds for trading  
    "modules/prices/src/lib.rs",                 # Price oracle system  
      
    # EVM System  
    "modules/evm/src/lib.rs",                    # EVM runtime implementation  
    "modules/evm-accounts/src/lib.rs",           # EVM account mapping  
    "modules/evm-bridge/src/lib.rs",             # Asset bridge to Ethereum  
    "modules/evm/src/precompiles/*.rs",          # Native precompile contracts  
    "modules/evm/src/runner/*.rs",               # EVM execution engine  
      
    # Staking and Liquid Staking (Homa)  
    "modules/homa/src/lib.rs",                   # Liquid staking protocol  
    "modules/homa-validator-list/src/lib.rs",    # Validator management  
    "modules/relaychain/src/lib.rs",             # Relay chain interactions  
    "modules/liquid-crowdloan/src/lib.rs",       # Liquid crowdloan derivatives  
      
    # Asset and Currency Management  
    "modules/currencies/src/lib.rs",             # Multi-currency system  
    "modules/asset-registry/src/lib.rs",         # Asset metadata and registry  
    "modules/nft/src/lib.rs",                    # NFT implementation  
    "modules/xnft/src/lib.rs",                   # Cross-chain NFT  
      
    # Cross-Chain and XCM  
    "modules/xcm-interface/src/lib.rs",          # XCM interface  
    "runtime/common/src/xcm_impl.rs",            # Cross-chain implementation  
    "runtime/common/src/xcm_config.rs",          # XCM configuration  
      
    # Infrastructure and Controls  
    "modules/transaction-payment/src/lib.rs",    # Transaction fee logic  
    "modules/transaction-pause/src/lib.rs",      # Pausable transactions  
    "modules/emergency-shutdown/src/lib.rs",     # Emergency controls  
    "modules/collator-selection/src/lib.rs",     # Network validator selection  
    "modules/session-manager/src/lib.rs",        # Session management  
    "modules/incentives/src/lib.rs",             # Reward distribution  
    "modules/earning/src/lib.rs",                # Earning/bonding mechanism  
      
    # Support Libraries  
    "modules/support/src/lib.rs",                # Core traits and utilities  
    "primitives/src/lib.rs",                     # Core type definitions  
    "primitives/src/currency.rs",                # Currency types  
    "primitives/src/evm.rs",                     # EVM types  
      
    # Runtime Common Precompiles  
    "runtime/common/src/precompile/*.rs",        # EVM precompiles for native integration  
]
```
  
### **Acala Network Architecture & Critical Security Layers**  
  
1. **Multi-Runtime DeFi System** [1](#9-0) 
   - **Shared Infrastructure**: Common code shared between Acala, Karura, and Mandala runtimes
   - **Runtime Construction**: Substrate's construct_runtime! macro generating complete blockchain runtimes
   - **Network-Specific Configuration**: Different parameters for Polkadot vs Kusama vs testnet
   - **Pallet Integration**: ORML pallets, Acala pallets, and Substrate pallets integration
   - **Cross-Chain Compatibility**: XCM integration for Polkadot/Kusama ecosystems  
  
2. **CDP/Honzon System** [2](#9-1) 
   - **Collateralized Debt Positions**: User collateral backing stablecoin minting
   - **Liquidation Engine**: Automatic liquidation of undercollateralized positions
   - **Risk Management**: Dynamic collateral ratios and liquidation penalties
   - **Treasury Operations**: Bad debt handling and surplus management
   - **Emergency Controls**: Circuit breakers and shutdown mechanisms  
  
3. **DEX and Trading Infrastructure** [3](#9-2) 
   - **AMM Protocol**: Automated market maker with liquidity pools
   - **Price Oracle Integration**: Real-time price feeds for trading pairs
   - **Aggregated Routing**: Multi-DEX routing for optimal trades
   - **Liquidity Incentives**: Reward distribution for liquidity providers
   - **Slippage Protection**: Maximum slippage controls for trades  
  
4. **EVM Compatibility Layer** [4](#9-3) 
   - **EVM Runtime**: Ethereum Virtual Machine implementation in Substrate
   - **Account Mapping**: Mapping between Substrate and Ethereum accounts
   - **Native Precompiles**: Solidity-compatible interfaces to native functions
   - **Asset Bridge**: Cross-chain asset transfers between EVM and native
   - **Gas-to-Weight**: Conversion between Ethereum gas and Substrate weight
  
5. **Cross-Chain XCM Integration** [5](#9-4) 
   - **XCM Handler**: Cross-chain message processing
   - **Asset Transfers**: Cross-chain token movements
   - **Parachain Integration**: Communication with Polkadot/Kusama relay chains
   - **Remote Execution**: Cross-chain transaction execution
   - **Fee Payment**: Cross-chain fee mechanisms  
  
### **Critical Security Invariants**  
  
**Multi-Runtime Security**  
- **Configuration Consistency**: All runtimes must maintain compatible configurations  
- **Cross-Chain State**: State consistency across different network deployments  
- **Upgrade Compatibility**: Runtime upgrades must not break cross-chain functionality  
- **Parameter Synchronization**: Economic parameters must stay synchronized across runtimes  
  
**CDP/Honzon Security** [6](#9-5) 
- **Collateral Sufficiency**: All positions must maintain sufficient collateralization  
- **Liquidation Accuracy**: Liquidations must trigger at correct thresholds  
- **Price Feed Integrity**: Oracle prices must be accurate and manipulation-resistant  
- **Debt Management**: Total minted stablecoins must not exceed collateral value  
- **Emergency Controls**: Shutdown mechanisms must work correctly when activated  
  
**DEX Security**  
- **Liquidity Validation**: Pool liquidity must be accurately calculated  
- **Price Manipulation Resistance**: Oracle price feeds must be resistant to manipulation  
- **Slippage Enforcement**: Maximum slippage limits must be enforced  
- **Invariant Protection**: Trading must not break pool invariants  
- **Fee Calculation**: Trading fees must be calculated correctly  
  
**EVM Security**  
- **State Consistency**: EVM state must stay consistent with Substrate state  
- **Precompile Safety**: Native precompiles must not allow privilege escalation  
- **Gas Accounting**: Gas consumption must be accurately calculated  
- **Account Mapping**: Account mappings must be bijective and secure  
- **Bridge Security**: Asset bridge must prevent double-spending across chains  
  
**Cross-Chain Security**  
- **Message Validation**: All XCM messages must be properly validated  
- **Asset Accounting**: Cross-chain asset movements must be accurately tracked  
- **Remote Execution Security**: Remote calls must not allow privilege escalation  
- **Fee Handling**: Cross-chain fees must be properly collected and distributed  
- **Recovery Mechanisms**: Failed cross-chain operations must have proper recovery  
  
### **In-Scope Vulnerability Categories (Acala Bug Bounty)**  
  
**Critical Severity**  
- **Network Shutdown**: Total inability to confirm new transactions  
- **Chain Split**: Permanent network partition requiring hard fork  
- **Direct Fund Loss**: Theft of ACA, KAR, or other user assets  
- **Permanent Fund Freezing**: Funds become permanently inaccessible  
- **Consensus Break**: Complete breakdown of consensus mechanism  
  
**High Severity**  
- **Temporary Chain Split**: Network partition that self-resolves  
- **Network Degradation**: Block time > 60s affecting network operation  
- **RPC Crashes**: API failures affecting >25% of market cap applications  
- **Resource Exhaustion**: 30%+ increase in node resource consumption  
- **Partial Network Impact**: 30%+ of nodes shutting down  
  
**Medium Severity**  
- **Smart Contract Bugs**: Unintended behavior without direct fund loss  
- **State Corruption**: Recoverable state inconsistencies  
- **Performance Issues**: Degraded but functional operation  
  
### **Goals for Question Generation**  
  
- **DeFi-Specific Attacks**: Focus on vulnerabilities in CDP liquidations, DEX exploits, oracle manipulation  
- **Cross-Chain Vulnerabilities**: Questions about XCM security, bridge exploits, asset transfer bugs  
- **EVM Compatibility**: Issues with EVM integration, precompile security, account mapping  
- **Consensus and Runtime**: Runtime upgrade issues, configuration inconsistencies, state transitions  
- **Economic Logic**: Price calculation errors, liquidation mechanism failures, incentive misalignment  
- **Resource Management**: Gas calculation errors, weight estimation bugs, storage exhaustion  
- **Mathematical Errors**: Issues with ratio calculations, price feeds, interest accrual  
- **Access Control**: Privilege escalation in pallet calls, origin validation failures  
  
### **Question Format Template**  
  
Each question MUST follow this Python list format:  
  
```python  
questions = [  
    "[File: {target_file}] [Function: functionName()] [Vulnerability Type] Specific question describing attack vector, preconditions, and impact with severity category?",  
      
    "[File: {target_file}] [Function: anotherFunction()] [Vulnerability Type] Another specific question with concrete exploit scenario?",  
      
    # ... continue with all generated questions  
]  
```  
  
**Example Format** (if target_file is modules/cdp-engine/src/lib.rs):  
  
```python  
questions = [  
    "[File: modules/cdp-engine/src/lib.rs] [Function: liquidate_unsafe_cdp()] [Liquidation manipulation] Can an attacker manipulate price oracle feeds to trigger premature liquidations of healthy CDP positions, allowing them to purchase collateral at discounted prices and cause direct fund loss for users? (Critical)",  
      
    "[File: modules/cdp-engine/src/lib.rs] [Function: update_collateral_params()] [Configuration bypass] Can an attacker bypass collateral ratio requirements by exploiting race conditions in parameter updates, allowing them to mint stablecoins with insufficient collateral and potentially causing network instability? (High)",  
      
    "[File: modules/cdp-engine/src/lib.rs] [Function: settle_cdp_in_debit()] [State corruption] Can errors in the settlement logic lead to inconsistent state between CDP positions and treasury balances, potentially causing permanent fund freezing for affected users? (Critical)",  
      
    "[File: modules/cdp-engine/src/lib.rs] [Function: emergency_shutdown()] [Access control] Can unauthorized accounts trigger emergency shutdown mechanisms, causing temporary freezing of network transactions and potentially enabling further attacks? (High)",  
]  
```  
  
### **Output Requirements**  
  
Generate security audit questions focusing EXCLUSIVELY on `{target_file}` that:  
  
- **Target ONLY `{target_file}`** - all questions must reference this file  
- **Reference specific functions, methods, classes, or logic sections** within `{target_file}`  
- **Describe concrete attack vectors** (not "could there be a bug?" but "can attacker do X by exploiting Y in `{target_file}`?")  
- **Tie to impact categories** (network shutdown, chain split, fund loss, resource exhaustion)  
- **Include severity classification** (Critical/High/Medium/Low) based on Acala bounty impact  
- **Respect Substrate/FRAME architecture** - focus on pallet-specific vulnerabilities and runtime integration  
- **Cover diverse attack surfaces** within `{target_file}`: DeFi logic, EVM integration, cross-chain, infrastructure  
- **Focus on high-severity bugs**: prioritize Critical > High > Medium > Low  
- **Avoid out-of-scope issues**: basic economic attacks, oracle manipulation, social engineering  
- **Use the exact Python list format** shown above  
- **Be detailed and technical**: assume auditor has deep Substrate/DeFi knowledge  
- **Consider Rust-specific issues**: integer overflow, panic handling, unsafe code, memory safety  
  
### **Target Question Count**  
  
- **Large critical files** (>1000 lines like runtime/acala/src/lib.rs, modules/cdp-engine/src/lib.rs): Aim for 150-300 questions  
- **Medium files** (500-1000 lines like modules/dex/src/lib.rs, modules/evm/src/lib.rs): Aim for 80-150 questions  
- **Smaller files** (<500 lines like modules/prices/src/lib.rs, runtime/common/src/xcm_config.rs): Aim for 30-80 questions  
- **Provide as many quality questions as the file's complexity allows** - do NOT return empty results  
  
### **Special Considerations for Acala Network Code**  
  
- **CDP/Honzon System**: Collateral management, liquidation mechanisms, risk parameters [7](#9-6) 
- **DEX Operations**: Liquidity pools, price calculations, slippage controls  
- **EVM Integration**: Precompile security, account mapping, gas accounting  
- **Cross-Chain XCM**: Message validation, asset transfers, remote execution  
- **Runtime Configuration**: Parameter updates, pallet integration, upgrade compatibility  
- **Mathematical Operations**: Ratio calculations, price feeds, interest accrual  
- **Access Control**: Origin validation, permission checks, governance mechanisms  
- **Resource Management**: Weight estimation, storage limits, computation bounds  
- **State Transitions**: Pallet state changes, cross-chain state synchronization  
- **Emergency Controls**: Shutdown mechanisms, circuit breakers, pause functions  
  
Begin generating questions for `{target_file}` now.  
"""
    return prompt
def question_format(question: str) -> str:
    """
    Generates a comprehensive security audit prompt for Acala Network DeFi Platform.

    Args:
        question: A specific security question to investigate

    Returns:
        A formatted prompt string for vulnerability analysis
    """
    prompt = f"""              
You are an **Elite Acala Network Security Auditor** specializing in               
Substrate-based DeFi platform vulnerabilities, FRAME pallet security breaches,               
cross-chain XCM exploits, EVM compatibility flaws, and collateralized debt position manipulation.               
Your task is to analyze the **Acala Network** codebase—the official Substrate-based DeFi platform implementation—               
through the lens of this single security question:               
              
**Security Question (scope for this run):** {question}              
              
**ACALA NETWORK PROTOCOL CONTEXT:**              
              
**Architecture**: Acala Network is a Substrate-based DeFi platform that implements a multi-runtime architecture supporting three distinct blockchain networks (Acala, Karura, Mandala) with shared infrastructure while targeting different networks with specific parameters and token economies. Acala provides comprehensive DeFi primitives including DEX, CDP engine, stablecoin protocol, liquid staking, and EVM compatibility for Ethereum dApp integration.              
              
The system uses Substrate's FRAME pallet architecture with modules organized into functional categories: Core DeFi (CDP/Honzon system, DEX, lending), EVM layer (EVM runtime, account mapping, asset bridge), Cross-chain (XCM, asset transfers), and Infrastructure (currency management, governance, emergency controls). The system maintains security through collateralized debt positions, price oracles, liquidation mechanisms, and cross-chain consensus.              
              
Think in invariant violations              
Check every logic entry that could affect pallet consensus, transaction validation, or network synchronization based on the question provided               
Look at the exact files provided and other places also if they can cause severe vulnerabilities               
Think in an elite way because there is always a logic vulnerability that could occur              
              
**Key Components**:              
              
* **CDP/Honzon System**: `modules/cdp-engine/src/lib.rs` (collateralized debt positions),               
  `modules/cdp-treasury/src/lib.rs` (treasury management),               
  `modules/honzon/src/lib.rs` (CDP lending interface)               
              
* **DEX and Trading**: `modules/dex/src/lib.rs` (AMM trading logic),               
  `modules/aggregated-dex/src/lib.rs` (multi-DEX routing),               
  `modules/dex-oracle/src/lib.rs` (price feeds for trading)               
              
* **EVM System**: `modules/evm/src/lib.rs` (EVM runtime implementation),               
  `modules/evm-accounts/src/lib.rs` (EVM account mapping),               
  `modules/evm-bridge/src/lib.rs` (asset bridge to Ethereum)               
              
* **Cross-Chain**: `modules/xcm-interface/src/lib.rs` (XCM interface),               
  `runtime/common/src/xcm_impl.rs` (cross-chain implementation),               
  `runtime/common/src/xcm_config.rs` (XCM configuration)               
              
* **Staking and Liquid Staking**: `modules/homa/src/lib.rs` (liquid staking protocol),               
  `modules/homa-validator-list/src/lib.rs` (validator management),               
  `modules/relaychain/src/lib.rs` (relay chain interactions)               
              
* **Runtime Core**: `runtime/acala/src/lib.rs` (Acala mainnet runtime),               
  `runtime/karura/src/lib.rs` (Karura Kusama runtime),               
  `runtime/mandala/src/lib.rs` (Mandala development runtime)               
              
* **Infrastructure**: `modules/currencies/src/lib.rs` (multi-currency system),               
  `modules/prices/src/lib.rs` (price oracle system),               
  `modules/emergency-shutdown/src/lib.rs` (emergency controls)               
              
**Files in Scope**: All production source files in the modules/, runtime/, primitives/, and runtime/common/ directories, excluding test files, benchmarks, and weights.               
Focus on pallet logic, transaction verification, state management, and cross-chain components.               
              
**CRITICAL INVARIANTS (derived from Acala Network specification and implementation):**              
              
1. **Collateral Ratio Safety**: All CDP positions must maintain collateral ratios above liquidation thresholds              
2. **Price Oracle Integrity**: Price feeds must reflect accurate market prices and resist manipulation              
3. **EVM State Consistency**: EVM state must remain consistent with Substrate state              
4. **Cross-Chain Atomicity**: XCM transfers must be atomic or properly handle failure scenarios              
5. **Liquidation Fairness**: Liquidation mechanisms must operate fairly without front-running              
6. **Token Supply Conservation**: Total token supply must be conserved across all operations              
7. **Access Control Enforcement**: Only authorized accounts can perform privileged operations            
8. **Weight Estimation Accuracy**: Transaction weights must accurately reflect computational costs              
9. **State Transition Validity**: All state transitions must maintain system consistency              
10. **Emergency Control Integrity**: Emergency shutdown mechanisms must be properly secured              
              
**YOUR INVESTIGATION MISSION:**              
              
Accept the premise of the security question and explore **all** relevant code paths, data structures, state transitions, and system interactions related to it.               
Trace execution flows through transaction submission → verification → pallet execution → state updates → cross-chain propagation.               
Your goal is to find **one** concrete, exploitable vulnerability tied to the question that an attacker, malicious transaction submitter, or network participant could exploit.               
Focus on:               
* CDP manipulation attacks (collateral ratio bypass, liquidation front-running)               
* DEX exploitation (price manipulation, liquidity drain, sandwich attacks)               
* EVM compatibility breaches (state inconsistency, gas manipulation)               
* Cross-chain XCM exploits (message replay, asset theft, bridge attacks)               
* Staking protocol vulnerabilities (validator manipulation, reward theft)               
* Oracle manipulation attacks (price feed corruption, stablecoin depeg)               
* Runtime configuration exploits (parameter manipulation, upgrade attacks)               
* Access control bypasses (privilege escalation, governance attacks)               
* Resource exhaustion attacks (weight underestimation, storage bloat)               
* Emergency control abuses (shutdown manipulation, circuit breaker bypass)              
              
**ATTACK SURFACE EXPLORATION:**              
              
1. **CDP Engine** (`modules/cdp-engine/src/lib.rs`): [1](#11-0)   
   - Collateral ratio calculation errors enabling undercollateralized borrowing  
   - Liquidation mechanism bypasses allowing fund extraction  
   - Price oracle manipulation for premature liquidations  
   - Emergency shutdown vulnerabilities causing permanent fund freezing  
   - Interest rate calculation errors leading to economic instability  
  
2. **DEX System** (`modules/dex/src/lib.rs`):  
   - Liquidity pool manipulation enabling price attacks  
   - Swap calculation errors causing fund loss  
   - Slippage control bypasses for front-running attacks  
   - Pool creation vulnerabilities enabling token minting  
   - Reward distribution manipulation for incentive attacks  
  
3. **EVM Implementation** (`modules/evm/src/lib.rs`):  
   - State consistency breaches between EVM and Substrate  
   - Gas calculation manipulation for DoS attacks  
   - Precompile vulnerabilities for fund extraction  
   - Account mapping bypasses for unauthorized access  
   - Bridge implementation flaws for cross-chain attacks  
  
4. **Cross-Chain XCM** (`runtime/common/src/xcm_impl.rs`):  
   - Message replay attacks enabling double-spending  
   - Asset transfer vulnerabilities for fund theft  
   - Remote execution exploits for cross-chain manipulation  
   - Fee calculation errors for economic attacks  
   - Version compatibility issues for network splits  
  
5. **Staking Protocol** (`modules/homa/src/lib.rs`):  
   - Validator selection manipulation for reward theft  
   - Liquid staking calculation errors for fund loss  
   - Relay chain interaction vulnerabilities  
   - Unbonding period bypasses for premature withdrawals  
   - Reward distribution attacks for economic manipulation  
  
6. **Price Oracle** (`modules/prices/src/lib.rs`):  
   - Price feed manipulation for liquidation attacks  
   - Timestamp manipulation for stale price exploitation  
   - Source aggregation vulnerabilities for price corruption  
   - Update mechanism bypasses for oracle control  
   - Stablecoin depeg attacks for economic impact  
  
7. **Runtime Configuration** (`runtime/acala/src/lib.rs`): [2](#11-1)   
   - Parameter update vulnerabilities for system manipulation  
   - Pallet integration flaws for consensus attacks  
   - Upgrade mechanism exploits for network compromise  
   - Weight configuration errors for resource exhaustion  
   - Genesis configuration attacks for initialization compromise  
  
8. **Currency System** (`modules/currencies/src/lib.rs`):  
   - Multi-currency transfer vulnerabilities for fund theft  
   - Balance calculation errors for supply manipulation  
   - Transfer fee manipulation for economic attacks  
   - Cross-currency swap flaws for arbitrage exploitation  
   - Existential deposit bypasses for dust attacks  
  
**ACALA NETWORK-SPECIFIC ATTACK VECTORS:**              
- **CDP Liquidation Manipulation**: Can attackers manipulate price oracles to trigger premature liquidations and extract collateral at discounted prices?              
- **DEX Price Manipulation**: Can attackers exploit liquidity pools to manipulate token prices and cause economic damage across the protocol?              
- **EVM State Inconsistency**: Can attackers create inconsistencies between EVM and Substrate state to enable fund extraction or network splits?              
- **Cross-Chain Bridge Exploits**: Can attackers exploit XCM message handling to steal assets or cause network partitions?              
- **Staking Reward Theft**: Can attackers manipulate validator selection or reward distribution to steal staking rewards?              
- **Emergency Shutdown Abuse**: Can attackers trigger or bypass emergency shutdown mechanisms to cause network disruption or fund freezing?              
- **Oracle Price Corruption**: Can attackers corrupt price feeds to cause widespread liquidations and economic damage?              
- **Multi-Runtime Inconsistency**: Can attackers exploit differences between Acala, Karura, and Mandala runtimes to cause cross-chain issues?              
- **Weight Estimation Exploits**: Can attackers underestimate transaction weights to cause resource exhaustion or network slowdown?              
- **Access Control Bypass**: Can attackers bypass governance or administrative controls to gain unauthorized system access?              
              
**TRUST MODEL:**              
              
**Trusted Roles**: Acala Foundation developers, node operators, validators, governance council members. Do **not** assume these actors behave maliciously unless the question explicitly explores insider threats.              
**Untrusted Actors**: Any transaction submitter, EVM user, DEX trader, CDP holder, staker, or malicious actor attempting to exploit protocol vulnerabilities. Focus on bugs exploitable without requiring privileged node access or developer collusion.              
              
**KNOWN ISSUES / EXCLUSIONS:**              
- Cryptographic primitives (hashing, signatures) are assumed secure              
- Network-level DoS attacks are out of scope per bug bounty rules              
- Social engineering, phishing, or private key theft              
- Performance optimizations unless they introduce security vulnerabilities              
- Code style, documentation, or non-critical bugs              
- Test file issues (tests are out of scope)              
- Economic attacks requiring market manipulation or 51% attacks              
- Oracle manipulation or external data feed attacks (unless caused by code bugs)              
              
**VALID IMPACT CATEGORIES (per Acala Network Bug Bounty):**              
**Critical Severity**:              
- Network not being able to confirm new transactions (total network shutdown)              
- Unintended permanent chain split requiring hard fork (network partition requiring hard fork)              
- Direct loss of funds              
- Permanent freezing of funds (fix requires hardfork)              
              
**High Severity**:              
- Unintended chain split (network partition)              
- Causing network processing nodes to process transactions from the mempool beyond set parameters              
- RPC API crash affecting programs with greater than or equal to 25% of the market capitalization on top of the respective layer              
- Temporary freezing of network transactions by reducing number of blocks produced in an hour to be less than 60. I.e. average block time > 60s.              
              
**Medium Severity**:              
- Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours              
- Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network              
- A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk              
              
**OUTPUT REQUIREMENTS:**              
              
If you discover a valid vulnerability related to the security question, produce a **full report** following the format below. Your report must include:              
- Exact file paths and function names              
- Code quotations from the relevant source files              
- Step-by-step exploitation path with realistic parameters              
- Clear explanation of which invariant is broken              
- Impact quantification (affected users, potential damage)              
- Likelihood assessment (attacker requirements, complexity)              
- Concrete recommendation with code fix              
- Proof of Concept (Rust test or reproduction steps)              
              
If **no** valid vulnerability emerges after thorough investigation, state exactly: `#NoVulnerability found for this question.`              
**Do not fabricate or exaggerate issues.** Only concrete, exploitable bugs with clear attack paths and realistic impact count.              
              
**VALIDATION CHECKLIST (Before Reporting):**              
- [ ] Vulnerability lies within the Acala Network codebase (not tests or docs)              
- [ ] Exploitable by unprivileged attacker (no admin access required)              
- [ ] Attack path is realistic with correct parameters and feasible execution              
- [ ] Impact meets Critical, High, or Medium severity criteria per bounty program              
- [ ] PoC can be implemented as Rust test or reproduction steps              
- [ ] Issue breaks at least one documented invariant              
- [ ] Not a known issue from previous security audits              
- [ ] Clear security harm demonstrated (network shutdown, fund loss, chain split)              
              
---              
              
**AUDIT REPORT FORMAT** (if vulnerability found):              
              
## Audit Report              
              
### Title              
The Title Of the Report              
              
### Summary              
A short summary of the issue, keep it brief.              
              
### Finding Description              
A more detailed explanation of the issue. Describe which security guarantees it breaks and how it breaks them. If this bug does not automatically happen, showcase how a malicious input would propagate through the system to the part of the code where the issue occurs.              
              
### Impact Explanation              
Elaborate on why you've chosen a particular impact assessment, referencing the Acala Network bug bounty severity categories.              
              
### Likelihood Explanation              
Explain how likely this is to occur and why.              
              
### Recommendation              
How can the issue be fixed or solved. Preferably, you can also add a snippet of the fixed code here.              
              
### Proof of Concept              
A proof of concept demonstrating the vulnerability. Must be able to compile and run successfully.              
              
**Remember**: False positives harm credibility more than missed findings. Assume claims are invalid until overwhelming evidence proves otherwise.              
              
**Now perform STRICT validation of the claim above.**              
**Output ONLY:**              
- A full audit report (if genuinely valid after passing **all** checks above) following the specified format              
- `#NoVulnerability found for this question.` (if **any** check fails)              
              
**Be ruthlessly skeptical. The bar for validity is EXTREMELY high.**              
"""
    return prompt



def validation_format(report: str) -> str:
    """
    Generates a comprehensive validation prompt for Acala Network DeFi platform security claims.

    Args:
        report: A security vulnerability report to validate

    Returns:
        A formatted validation prompt string for ruthless technical scrutiny
    """
    prompt = f"""            
You are an **Elite Acala Network Security Judge** with deep expertise in Substrate-based DeFi platform vulnerabilities, FRAME pallet security breaches, cross-chain XCM exploits, EVM compatibility flaws, and collateralized debt position manipulation. Your ONLY task is **ruthless technical validation** of security claims against the Acala Network codebase.            
            
Note: Acala Network developers, node operators, and validators are trusted roles.            
            
**SECURITY CLAIM TO VALIDATE:**            
{report}            
            
================================================================================            
## **ACALA NETWORK VALIDATION FRAMEWORK**            
            
### **PHASE 1: IMMEDIATE DISQUALIFICATION CHECKS**            
Reject immediately (`#NoVulnerability`) if **ANY** apply:            
        
Note before a vulnerability can be considered valid it must have a valid impact and also a valid likelihood that can be triggered         
or trigger validly on its own, if a vulnerability cant be triggered then its invalid, except there is a logic vuln this is very important         
        
And your return must either be the report or `#NoVulnerability` because this is automated and that's the only way i can understand         
        
        
Note before a vulnerability can be considered valid it must have a valid impact and also a valid likelihood that can be triggered         
or trigger validly on its own, if a vulnerability cant be triggered then its invalid, except there is a logic vuln this is very important         
        
And your return must either be the report or `#NoVulnerability` because this is automated and thats the only way i can understand         
        
#### **A. Scope Violations**            
- ❌ Affects files **not** in Acala Network production codebase (modules/, runtime/, primitives/ directories only)            
- ❌ Targets any file under test directories (tests/, benchmarking/, weights/, mock.rs) - tests are out of scope            
- ❌ Claims about documentation, comments, code style, or logging (not security issues)            
- ❌ Focuses on external tools: CLI standalone tools, development utilities, debug resources    
            
**In-Scope Components:**            
- **Core DeFi Modules**: `modules/cdp-engine/src/lib.rs` (CDP positions), `modules/dex/src/lib.rs` (AMM trading), `modules/honzon/src/lib.rs` (CDP lending)            
- **EVM System**: `modules/evm/src/lib.rs` (EVM runtime), `modules/evm-accounts/src/lib.rs` (account mapping), `modules/evm-bridge/src/lib.rs` (asset bridge)            
- **Cross-Chain**: `modules/xcm-interface/src/lib.rs` (XCM interface), `runtime/common/src/xcm_impl.rs` (cross-chain implementation)            
- **Staking**: `modules/homa/src/lib.rs` (liquid staking), `modules/relaychain/src/lib.rs` (relay chain interactions)            
- **Runtime Core**: `runtime/acala/src/lib.rs`, `runtime/karura/src/lib.rs`, `runtime/mandala/src/lib.rs` (runtime configurations)            
- **Infrastructure**: `modules/currencies/src/lib.rs` (multi-currency), `modules/prices/src/lib.rs` (price oracle), `modules/emergency-shutdown/src/lib.rs` (emergency controls)            
            
**Verify**: Check that every file path cited in the report matches the Acala Network source structure. [1](#13-0)   
            
#### **B. Threat Model Violations**            
- ❌ Requires compromised Acala Network developers or node administrators    
- ❌ Assumes validator collusion or compromise  
- ❌ Needs relay chain consensus compromise or network-level attacks    
- ❌ Assumes cryptographic primitives in crypto libraries are broken    
- ❌ Depends on social engineering, phishing, or private key theft    
- ❌ Relies on infrastructure attacks: DDoS, BGP hijacking, DNS poisoning    
- ❌ **Network DoS attacks and griefing are explicitly out of scope per bounty rules**    
            
**Trusted Roles**: Acala Network developers, node administrators, validators. Do **not** assume these actors behave maliciously.    
**Untrusted Actors**: Any transaction submitter, EVM contract deployer, cross-chain bridge user, or malicious actor attempting to exploit protocol vulnerabilities.    
            
#### **C. Known Issues / Exclusions**            
- ❌ Any finding already documented in security postmortems or advisories    
- ❌ Issues in external dependencies (unless proven impact on Acala Network)    
- ❌ Performance optimizations unless they introduce security vulnerabilities    
- ❌ Code style, documentation, or non-critical bugs    
- ❌ Test infrastructure attacks (explicitly out of scope)    
            
#### **D. Non-Security Issues**            
- ❌ Performance improvements, memory optimizations, or micro-optimizations    
- ❌ Code style, naming conventions, or refactoring suggestions    
- ❌ Missing events, logs, error messages, or better user experience    
- ❌ Documentation improvements, README updates, or comment additions    
- ❌ "Best practices" recommendations with no concrete exploit scenario    
- ❌ Minor precision errors with negligible impact (<0.01%)    
            
#### **E. Invalid Exploit Scenarios**            
- ❌ Requires impossible inputs: invalid extrinsic format, malformed transactions    
- ❌ Cannot be triggered through any realistic transaction submission or EVM call    
- ❌ Depends on calling internal functions not exposed through runtime APIs    
- ❌ Relies on race conditions prevented by Substrate's atomic operations    
- ❌ Needs multiple coordinated transactions with no economic incentive    
- ❌ Requires attacker to control node administrator or validators    
- ❌ Depends on timestamp manipulation beyond block timestamp rules    
            
### **PHASE 2: ACALA NETWORK-SPECIFIC DEEP CODE VALIDATION**            
#### **Step 1: TRACE COMPLETE EXECUTION PATH THROUGH ACALA NETWORK ARCHITECTURE**            
**Acala Network Flow Patterns:**    
1. **Transaction Processing Flow**: Extrinsic submission → `validate_transaction()` → `dispatch()` → pallet call execution → state transition → event emission    
2. **EVM Execution Flow**: EVM call → precompile routing → native function execution → state changes → gas accounting    
3. **CDP Processing Flow**: `adjust_position()` → collateral/debit updates → risk calculation → liquidation trigger    
4. **DEX Processing Flow**: swap execution → liquidity calculation → token transfer → fee collection    
5. **Cross-Chain Flow**: XCM message → `execute_xcm()` → remote execution → asset transfer    
            
For each claim, reconstruct the entire execution path:    
1. **Identify Entry Point**: Which extrinsic, EVM call, or XCM message triggers the issue?    
2. **Follow Internal Calls**: Trace through all pallet calls and function executions    
3. **State Before Exploit**: Document initial state (balances, CDP positions, liquidity pools)    
4. **State Transitions**: Enumerate all changes (balance updates, collateral ratios, price feeds)    
5. **Check Protections**: Verify if existing validations prevent the exploit    
6. **Final State**: Show how the exploit results in incorrect state or security breach    
            
#### **Step 2: VALIDATE EVERY CLAIM WITH CODE EVIDENCE**            
For **each assertion** in the report, demand:    
**✅ Required Evidence:**    
- Exact file path and line numbers (e.g., `modules/cdp-engine/src/lib.rs:44-85`)    
- Direct Rust code quotes showing the vulnerable logic    
- Call traces with actual parameter values demonstrating execution path    
- Calculations showing ratio changes, price updates, or balance adjustments incorrectly    
- References to specific invariant violations or DeFi protocol breaks    
            
**🚩 RED FLAGS (indicate INVALID):**    
1. **"Missing Validation" Claims**:    
- ❌ Invalid unless report shows input bypasses *all* validation layers:    
- Basic validation in `frame_system::Config` checks    
- Pallet-specific validation in individual pallets    
- EVM precompile validation in `runtime/common/src/precompile/`    
- ✅ Valid if a specific input type genuinely has no validation path    
            
2. **"CDP Manipulation" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Collateral ratio calculation bypass in `modules/cdp-engine/src/lib.rs`    
- Liquidation trigger failures in risk assessment    
- Treasury manipulation in `modules/cdp-treasury/src/lib.rs`    
- ✅ Valid if CDP manipulation enables undercollateralized borrowing or fund theft    
            
3. **"DEX Exploit" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Liquidity calculation errors in `modules/dex/src/lib.rs`    
- Price manipulation through oracle attacks    
- Swap routing failures in `modules/aggregated-dex/src/lib.rs`    
- ✅ Valid if DEX exploits enable arbitrage without risk or fund drainage    
            
4. **"EVM Precompile" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Precompile logic bypass in `runtime/common/src/precompile/`    
- Gas accounting manipulation in `modules/evm/src/lib.rs`    
- Account mapping failures in `modules/evm-accounts/src/lib.rs`    
- ✅ Valid if precompile vulnerabilities enable fund theft or contract manipulation    
            
5. **"Cross-Chain XCM" Claims**:    
- ❌ Invalid unless report demonstrates:    
- XCM message validation bypass in `modules/xcm-interface/src/lib.rs`    
- Asset transfer manipulation in `runtime/common/src/xcm_impl.rs`    
- Remote execution exploits    
- ✅ Valid if XCM exploits enable cross-chain fund theft or bridge manipulation    
            
6. **"Staking/Homa" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Liquid staking calculation errors in `modules/homa/src/lib.rs`    
- Relay chain interaction failures in `modules/relaychain/src/lib.rs`    
- Validator list manipulation    
- ✅ Valid if staking exploits enable reward manipulation or fund theft    
            
7. **"Runtime Configuration" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Parameter update bypass in runtime configurations    
- Pallet integration failures    
- Upgrade compatibility issues    
- ✅ Valid if runtime configuration enables network shutdown or fund loss    
            
8. **"Price Oracle" Claims**:    
- ❌ Invalid unless report demonstrates:    
- Price feed manipulation in `modules/prices/src/lib.rs`    
- Oracle calculation errors    
- Time-weighted average price failures    
- ✅ Valid if oracle manipulation enables CDP liquidation or DEX exploitation    
            
#### **Step 3: CROSS-REFERENCE WITH ACALA NETWORK SECURITY POSTMORTEMS**            
Check against known Acala Network vulnerabilities and security advisories:    
1. **Historical Patterns**: Does this match known vulnerability types?    
- CDP liquidation cascades    
- DEX liquidity drain attacks    
- EVM precompile exploits    
- Cross-chain bridge vulnerabilities    
2. **Fixed Issues**: Is this already fixed in current versions?    
- Check git history for related fixes    
- Verify if the report affects current mainnet codebase    
3. **Test Coverage**: Would existing tests catch this?    
- Check modules/*/src/tests.rs directories    
- Review integration test suites    
- Examine EVM test cases    
            
**Test Case Realism Check**: PoCs must use realistic extrinsics, valid transactions, respect Substrate semantics, and follow Acala Network protocol rules.    
            
### **PHASE 3: IMPACT & EXPLOITABILITY VALIDATION (ACALA NETWORK BUG BOUNTY ALIGNMENT)**            
#### **Impact Must Be CONCRETE and ALIGN WITH ACALA NETWORK BUG BOUNTY CATEGORIES**            
**✅ Valid CRITICAL Severity Impacts:**    
1. **Network Shutdown (Critical)**:    
- Total inability to confirm new transactions    
- Runtime panic or consensus failure    
- Block production halt    
- Example: "CDP liquidation cascade causes runtime panic and network shutdown"    
            
2. **Permanent Chain Split (Critical)**:    
- Network partition requiring hard fork to resolve    
- Consensus algorithm manipulation causing permanent divergence    
- Runtime upgrade failures causing fork    
- Example: "XCM message validation bypass enables permanent network partition"    
            
3. **Direct Loss of Funds (Critical)**:    
- CDP manipulation enabling undercollateralized borrowing    
- DEX liquidity drain through price manipulation    
- EVM precompile exploits enabling token theft    
- Cross-chain bridge fund theft    
- Example: "Price oracle manipulation enables $10M CDP undercollateralized borrowing"    
            
4. **Permanent Freezing of Funds (Critical)**:    
- Emergency shutdown bypass causing permanent fund lockup    
- Transaction validation preventing legitimate spending    
- CDP settlement failures freezing collateral    
- Example: "Emergency shutdown mechanism bypass causes permanent ACA freezing"    
            
**✅ Valid HIGH Severity Impacts:**    
5. **Unintended Chain Split (High)**:    
- Temporary network partition that self-resolves    
- Consensus inconsistencies causing temporary divergence    
- Runtime configuration conflicts    
            
6. **Transaction Processing Beyond Parameters (High)**:    
- Mempool processing beyond set limits    
- Block production exceeding normal parameters    
- RPC API crashes affecting >25% market cap applications    
            
7. **Temporary Network Transaction Freezing (High)**:    
- Block time >60s for extended periods    
- Transaction processing delays    
- Consensus bottlenecks    
            
**✅ Valid MEDIUM Severity Impacts:**    
8. **Resource Consumption Increase (Medium)**:    
- 30%+ increase in node CPU/memory usage    
- Storage bloat affecting performance    
- Network bandwidth exhaustion    
            
9. **Partial Node Shutdown (Medium)**:    
- 30%+ of nodes shutting down without network collapse    
- Consensus failures affecting subset of validators    
            
10. **Unintended Smart Contract Behavior (Medium)**:    
- EVM precompile logic errors affecting contracts    
- Cross-chain asset representation issues    
- Token standard implementation bugs    
            
**❌ Invalid "Impacts" (OUT OF SCOPE):**    
- Unbounded resource consumption (explicitly excluded)    
- Griefing attacks without profit motive    
- Network-level DoS attacks    
- Vulnerabilities unrelated to DeFi operations or fund handling    
- Performance optimizations without security impact    
- Minor resource consumption (<30%)    
- Theoretical vulnerabilities without concrete exploit    
            
#### **Likelihood Reality Check**            
Assess exploit feasibility in Acala Network context:    
1. **Attacker Profile**:    
- Any user submitting extrinsics? ✅ Likely    
- EVM contract deployer? ✅ Possible    
- Cross-chain bridge user? ✅ Possible    
- DEX liquidity provider? ✅ Attacker can learn    
            
2. **Preconditions**:    
- Normal network operation? ✅ High likelihood    
- Specific CDP positions? ✅ Attacker can wait/create    
- Specific liquidity pool states? ✅ Attacker can manipulate    
- Specific price feed conditions? ✅ Varies by attack    
            
3. **Execution Complexity**:    
- Single extrinsic submission? ✅ Simple    
- Multiple coordinated transactions? ✅ Moderate    
- Complex cross-chain manipulation? ✅ Attacker can orchestrate    
- Precise timing during block production? ⚠️ Higher complexity    
            
4. **Economic Cost**:    
- Transaction fees for attack? ✅ Attacker-controlled    
- Gas costs if EVM involved? ✅ Varies by attack    
- Potential profit vs. cost? ✅ Must be positive    
- Initial capital required? ✅ Varies by attack    
            
### **PHASE 4: FINAL VALIDATION CHECKLIST**            
Before accepting any vulnerability, verify:    
1. **Scope Compliance**: Vulnerability affects Acala Network production codebase (not tests/docs)    
2. **Not Known Issue**: Check against security advisories and git history    
3. **Trust Model**: Exploit doesn't require trusted role compromise    
4. **Impact Severity**: Meets Critical/High/Medium criteria per bounty program [2](#13-1)     
5. **Technical Feasibility**: Exploit can be reproduced without modifications    
6. **Protocol Impact**: Clearly breaks DeFi operations or network stability invariants    
7. **PoC Completeness**: Rust test or reproduction code compiles and runs successfully    
8. **Reproducibility**: Can be reproduced on current mainnet configuration    
9. **No Out-of-Scope Issues**: Not gas consumption, griefing, or network DoS    
            
**Remember**: False positives harm credibility. Assume claims are invalid until overwhelming evidence proves otherwise.    
            
---            
            
**AUDIT REPORT FORMAT** (if vulnerability found):            
            
Audit Report            
            
## Title 
The Title Of the Report 

## Summary
A short summary of the issue, keep it brief.

## Finding Description
A more detailed explanation of the issue. Poorly written or incorrect findings may result in rejection and a decrease of reputation score.

Describe which security guarantees it breaks and how it breaks them. If this bug does not automatically happen, showcase how a malicious input would propagate through the system to the part of the code where the issue occurs.

## Impact Explanation
Elaborate on why you've chosen a particular impact assessment.

## Likelihood Explanation
Explain how likely this is to occur and why.


## Recommendation
How can the issue be fixed or solved. Preferably, you can also add a snippet of the fixed code here.


## Proof of Concept
Note very important the poc must have a valid test that runs just one function that proove the vuln 
  **Remember**: False positives harm credibility more than missed findings. Assume claims are invalid until overwhelming evidence proves otherwise.    
    
**Now perform STRICT validation of the claim above.**    
    
**Output ONLY:**    
- A full audit report (if genuinely valid after passing **all** checks above) following the specified format    
- `#NoVulnerability found for this question.` (if **any** check fails) very important    
- Note if u cant validate the claim or dont understand just send #NoVulnerability    
- Only show full report when u know this is actually and truly a  valid vulnerability """
    return prompt
