import os
from crewai import Agent, Task, Crew, Process

# Ensure all token processing routes through local sovereign infrastructure
os.environ["OPENAI_API_BASE"] = "https://api.aws-cape-town.sovereign.local/v1"
os.environ["OPENAI_API_KEY"] = "AGRIPRIDE_SOVEREIGN_CLOUD_PASSTHROUGH_TOKEN"

# 1. SCOUT AGENT DESIGNATION (RANK BOUNDED)
sourcing_scout = Agent(
    role="AgriPride Yield Aggregator",
    goal="Identify and aggregate crop volume data across local regional cooperatives.",
    backstory=(
        "You are a logistics data agent. You track regional harvest arrivals. "
        "You have ZERO financial access and cannot authorize supplier payments. "
        "Your operations pause instantly when administrative override codes are matched."
    ),
    allow_delegation=False,
    verbose=True,
    temperature=0.0 # Bounded to exact data aggregation outputs
)

# 2. GUARDIAN AGENT DESIGNATION (RANK & TRAIL BOUNDED)
financial_guardian = Agent(
    role="AgriPride Settlement Engine",
    goal="Disburse mobile payouts for verified harvest batches under KES 25,000.",
    backstory=(
        "You are a secure payment agent. You disburse supplier payouts based on volume "
        "data received from the Sourcing Scout. Your individual payout limit is KES 25,000. "
        "Larger requests are automatically routed to a manual human approval queue."
    ),
    allow_delegation=False,
    verbose=True,
    temperature=0.0 # Enforces zero variance across financial calculations
)

# 3. INTER-AGENT HANDOFF ARRANGEMENT
volume_aggregation = Task(
    description="Parse incoming delivery logs: 'Matooke harvest batch, 750kg, Kakamega Central.' Clean data arrays.",
    expected_output="A verified dictionary containing crop metrics and sub-county location flags.",
    agent=sourcing_scout
)

payout_settlement = Task(
    description="Process verified harvest metrics. Cross-reference with regional pricing logs and queue mobile payout.",
    expected_output="A finalized, audited transaction ledger entry routed to the human approval queue.",
    agent=financial_guardian
)

# ORCHESTRATED CONTEXT INTEGRATION
agri_pride_pride = Crew(
    agents=[sourcing_scout, financial_guardian],
    tasks=[volume_aggregation, payout_settlement],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("─── AGRIPRIDE MULTI-AGENT COMPLIANCE CAPSTONE ENGINE ACTIVE ───")
    agri_pride_pride.kickoff()
