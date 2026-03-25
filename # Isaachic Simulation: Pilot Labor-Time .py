# Isaachic Simulation: Integrated Labor-Time & Dynamic Metabolism
# Base logic by Isaac MX Nielens (March 2026)
# Integrated with Resource Scarcity & Metabolic Veto logic

class ResourceBank:
    def __init__(self):
        # Earth's Registry: capacity vs current available stock
        # Lower 'current' values trigger higher ENLT multipliers (scarcity)
        self.registry = {
            "Bread": {"capacity": 1000, "current": 900},
            "Medicine": {"capacity": 500, "current": 450},
            "Water": {"capacity": 5000, "current": 4800},
            "Steel": {"capacity": 1000, "current": 150},  # CRITICALLY LOW
            "Wood": {"capacity": 1200, "current": 600},
            "Electricity": {"capacity": 2000, "current": 1800},
            "Plastic": {"capacity": 1500, "current": 400}, # SCARCE
            "Healthcare": {"capacity": 1000, "current": 1000} # Infinite social resource
        }

    def get_enlt_multiplier(self, resource_name):
        """Calculates the Scarcity Multiplier based on available stock."""
        if resource_name in self.registry:
            res = self.registry[resource_name]
            # Multiplier = Capacity / Current. 
            # If we have 10% left, the ecological cost (ENLT) is 10x higher.
            return res["capacity"] / max(res["current"], 1)
        return 1.0

    def deplete(self, resource_name, amount):
        """Physical depletion of the resource stock."""
        if resource_name in self.registry:
            self.registry[resource_name]["current"] -= (amount * 0.1) # 1 voucher = 0.1 physical units
            if self.registry[resource_name]["current"] < 0:
                self.registry[resource_name]["current"] = 0

class CentralPlan:
    def __init__(self, resource_bank):
        self.bank = resource_bank
        # Base ENLT represents the "Initial Ecological Cost"
        self.products = {
            "Bread": {"planned_labor": 100, "spent_vouchers": 0, "base_enlt": 5},
            "Medicine": {"planned_labor": 50, "spent_vouchers": 0, "base_enlt": 20},
            "Water": {"planned_labor": 150, "spent_vouchers": 0, "base_enlt": 80},
            "Wood": {"planned_labor": 120, "spent_vouchers": 0, "base_enlt": 60},
            "Steel": {"planned_labor": 200, "spent_vouchers": 0, "base_enlt": 100},
            "Electricity": {"planned_labor": 160, "spent_vouchers": 0, "base_enlt": 70},
            "Plastic": {"planned_labor": 140, "spent_vouchers": 0, "base_enlt": 50},
            "Healthcare": {"planned_labor": 250, "spent_vouchers": 0, "base_enlt": 90},
        }

    def process_consumption(self, product_name, amount):
        if product_name in self.products:
            self.products[product_name]["spent_vouchers"] += amount
            self.bank.deplete(product_name, amount)
            print(f"Consumed {product_name:10} | Vouchers spent: {amount}")

    def calculate_suv(self):
        print("\n" + "="*80)
        print("--- ISAAC-CYBERNETIC FEEDBACK (THE PID SIGNAL) ---")
        print(f"{'Product':12} | {'SUV':4} | {'Dyn-ENLT':8} | {'PS':4} | {'Metabolic Action'}")
        print("-" * 80)
        
        for name, data in self.products.items():
            # SUV = Social Weighting proxy (Demand vs Plan)
            suv = data["spent_vouchers"] / data["planned_labor"]
            
            # Dynamic ENLT = Base Cost * Scarcity Multiplier
            multiplier = self.bank.get_enlt_multiplier(name)
            current_enlt = data["base_enlt"] * multiplier
            
            # Priority Score (The Core Isaachic Logic)
            priority_score = (data["planned_labor"] * suv) / current_enlt
            
            if priority_score < 1.0:
                action = f"VETOED (Scarcity: {multiplier:.1f}x)"
            elif suv > 1.0:
                action = "INCREASE PRODUCTION"
            elif suv < 1.0:
                action = "DECREASE PRODUCTION"
            else:
                action = "STASIS (Equilibrium)"
            
            print(f"{name:12} | {suv:.2f} | {current_enlt:8.1f} | {priority_score:.2f} | {action}")

class IsaachicAgent:
    def __init__(self, name, training_hours, career_expected_hours):
        self.name = name
        self.v_hour = 1 + (training_hours / career_expected_hours)
        self.vouchers = 0

    def work(self, actual_hours):
        credit = actual_hours * self.v_hour
        self.vouchers += credit
        return credit

# --- EXECUTION ---
earth = ResourceBank()
plan = CentralPlan(earth)

# Initialize Agents
surgeon = IsaachicAgent("Specialist", training_hours=20000, career_expected_hours=40000)
laborer = IsaachicAgent("Baseline", training_hours=0, career_expected_hours=40000)

print(f"--- SIL Multipliers ---")
print(f"Surgeon: {surgeon.v_hour:.2f}x | Laborer: {laborer.v_hour:.2f}x\n")

# Simulation Cycle: Work and then Consume
surgeon.work(40) 
laborer.work(40)

# Simulating high demand across various sectors
# Simulation: People spend their earned vouchers
plan.process_consumption("Bread", 120)  # High demand
plan.process_consumption("Medicine", 25) # Low demand (over-produced)
plan.process_consumption("Water", 200) # High demand for a life-necessity
plan.process_consumption("Healthcare", 300) # Urgent social investment
plan.process_consumption("Steel", 50) # Low demand for a high-pollution item
plan.process_consumption("Education", 180) # High demand for social investment
plan.process_consumption("Entertainment", 100) # Moderate demand for leisure
plan.process_consumption("Transportation", 250) # High demand for mobility
plan.process_consumption("Agriculture", 150) # Moderate demand for food production
plan.process_consumption("Construction", 220) # High demand for infrastructure
plan.process_consumption("Textiles", 80) # Low demand for clothing
plan.process_consumption("Metals", 60) # Moderate demand for raw materials
plan.process_consumption("Chemicals", 90) # Moderate demand for industrial inputs
plan.process_consumption("Pharmaceuticals", 200) # High demand for health products
plan.process_consumption("Electricity", 180) # High demand for energy
plan.process_consumption("Plastic", 70) # Moderate demand for consumer goods
plan.process_consumption("Paper", 50) # Low demand for paper products
plan.process_consumption("chairs", 30) # Low demand for furniture
plan.process_consumption("tables", 40) # Moderate demand for furniture
plan.process_consumption("cars", 150) # High demand for transportation
plan.process_consumption("smartphones", 120) # High demand for technology
plan.process_consumption("laptops", 110) # High demand for technology
plan.process_consumption("furniture", 90) # Moderate demand for home goods



plan.calculate_suv()

print(f"\n--- Total Vouchers ---")
print(f"Surgeon earned: {surgeon.vouchers:.2f} vouchers")
print(f"Laborer earned: {laborer.vouchers:.2f} vouchers")
