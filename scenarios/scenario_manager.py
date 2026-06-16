# =====================================
# scenario_manager.py
# =====================================

SCENARIOS = {

    "SALARY": {

        "title": "💼 Salary Negotiation",

        "role": "HR Manager",

        "goal":
        "Hire a talented candidate while ensuring fairness.",

        "constraints": [
            "Need position filled quickly",
            "Must justify hiring decisions"
        ]
    },

    "FREELANCE": {

        "title": "💻 Freelance Contract",

        "role": "Client",

        "goal":
        "Hire a freelancer for a critical project.",

        "constraints": [
            "Delivery timeline matters",
            "Need reliable communication"
        ]
    },

    "CAR": {

        "title": "🚗 Car Purchase",

        "role": "Car Dealer",

        "goal":
        "Sell a vehicle while maintaining value.",

        "constraints": [
            "Limited inventory",
            "Need customer satisfaction"
        ]
    },

    "RENT": {

        "title": "🏠 House Rent",

        "role": "Landlord",

        "goal":
        "Find a reliable tenant.",

        "constraints": [
            "Property is in high demand"
        ]
    },

    "PRODUCT": {

        "title": "📦 Product Pricing",

        "role": "Sales Manager",

        "goal":
        "Close a sale while maintaining value.",

        "constraints": [
            "Customer is comparing competitors"
        ]
    }
}


class ScenarioManager:

    def __init__(self):

        self.scenarios = SCENARIOS

    def get_scenarios(self):

        return list(
            self.scenarios.keys()
        )

    def get_scenario(
        self,
        scenario_name
    ):

        return self.scenarios.get(
            scenario_name.upper()
        )

    def describe(
        self,
        scenario_name
    ):

        scenario = self.get_scenario(
            scenario_name
        )

        if scenario is None:

            return "Scenario not found."

        return (
            f"Role: {scenario['role']}\n"
            f"Goal: {scenario['goal']}"
        )