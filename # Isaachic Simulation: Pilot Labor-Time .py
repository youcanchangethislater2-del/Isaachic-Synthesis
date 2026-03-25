# Isaachic Simulation: Pilot Labor-Time Voucher System
# Base logic developed by Isaac MX Nielens on Wednesday, March, 2026
# This simulation models a simplified version of the Isaachic economic system, focusing on labor-time vouchers and their impact on production and consumption decisions.

class CentralPlan:
    def __init__(self):
        self.products = {
            "Bread": {"planned_labor": 100, "spent_vouchers": 0, "enlt": 5}, #Changed ENLT to 500 for Bread to reflect lower ecological cost in which it VETOED THE DECISION IVE DONE IT 
            "Medicine": {"planned_labor": 50, "spent_vouchers": 0, "enlt": 20},
            "Water": {"planned_labor": 150, "spent_vouchers": 0, "enlt": 80},
            "Clothing": {"planned_labor": 80, "spent_vouchers": 0, "enlt": 30},
            "Wood": {"planned_labor": 120, "spent_vouchers": 0, "enlt": 60},
            "Steel": {"planned_labor": 200, "spent_vouchers": 0, "enlt": 100},
            "Natural Gas": {"planned_labor": 180, "spent_vouchers": 0, "enlt": 90},
            "Electricity": {"planned_labor": 160, "spent_vouchers": 0, "enlt": 70},
            "Plastic": {"planned_labor": 140, "spent_vouchers": 0, "enlt": 50},
            "Paper": {"planned_labor": 110, "spent_vouchers": 0, "enlt": 40},
            "chairs": {"planned_labor": 90, "spent_vouchers": 0, "enlt": 25},
            "tables": {"planned_labor": 130, "spent_vouchers": 0, "enlt": 35},
            "cars": {"planned_labor": 300, "spent_vouchers": 0, "enlt": 150},
            "smartphones": {"planned_labor": 250, "spent_vouchers": 0, "enlt": 120},
            "laptops": {"planned_labor": 220, "spent_vouchers": 0, "enlt": 110},
            "furniture": {"planned_labor": 180, "spent_vouchers": 0, "enlt": 80},
            "Education": {"planned_labor": 200, "spent_vouchers": 0, "enlt": 60},
            "Healthcare": {"planned_labor": 250, "spent_vouchers": 0, "enlt": 90},
            "Entertainment": {"planned_labor": 150, "spent_vouchers": 0, "enlt": 40},
            "Transportation": {"planned_labor": 220, "spent_vouchers": 0, "enlt": 100},
            "Agriculture": {"planned_labor": 170, "spent_vouchers": 0, "enlt": 70},
            "Construction": {"planned_labor": 200, "spent_vouchers": 0, "enlt": 80},
            "Textiles": {"planned_labor": 140, "spent_vouchers": 0, "enlt": 50},
            "Metals": {"planned_labor": 160, "spent_vouchers": 0, "enlt": 60},
            "Chemicals": {"planned_labor": 180, "spent_vouchers": 0, "enlt": 90},
            "Pharmaceuticals": {"planned_labor": 220, "spent_vouchers": 0, "enlt": 110},
            }

    def process_consumption(self, product_name, amount):
        if product_name in self.products:
            self.products[product_name]["spent_vouchers"] += amount
            print(f"Consumed {product_name}. Vouchers spent: {amount}")

    def calculate_suv(self):
        print("\n--- SUV Feedback (The PID Signal) ---")
        for name, data in self.products.items():
            # SUV = Vouchers spent / Planned labor
            suv = data["spent_vouchers"] / data["planned_labor"]
            
            # The Isaachic Adjudication: PS = (SNLT * SW) / sum(ENLT)
            # We use SUV as our Social Weighting (SW) proxy here
            priority_score = (data["planned_labor"] * suv) / data["enlt"]
            
            if priority_score < 1.0:
                action = "VETOED / THROTTLED (Ecological Cost too high)"
            elif suv > 1.0:
                action = "INCREASE production (High Social Urgency)"
            elif suv < 1.0:
                action = "DECREASE production (Avoid Waste)"
            else:
                action = "STASIS (Metabolic Equilibrium)"
            
            print(f"{name} | SUV: {suv:.2f} | PS: {priority_score:.2f} | Action: {action}")

            if data["enlt"] > 50:
                print(f"  * Warning: ENLT for {name} is high ({data['enlt']}), consider adjusting labor allocation.")

# Connect the "Brain" to the "Body"
plan = CentralPlan()

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


class IsaachicAgent:
    def __init__(self, name, training_hours, career_expected_hours):
        self.name = name
        self.training_hours = training_hours
        self.career_expected_hours = career_expected_hours
        
        # Formula: V_hour = 1 + (L_training / n_life)
        self.v_hour = 1 + (training_hours / career_expected_hours)
        self.vouchers = 0

    def work(self, actual_hours):
        # Value produced is based on Labor Density (SIL)
        credit = actual_hours * self.v_hour
        self.vouchers += credit
        print(f"{self.name} worked {actual_hours} hours. Vouchers earned: {credit:.2f}")

# Initializing agents based on social investment
surgeon = IsaachicAgent("Specialist", training_hours=20000, career_expected_hours=40000)
laborer = IsaachicAgent("Baseline", training_hours=0, career_expected_hours=40000)

print(f"--- SIL Multipliers ---")
print(f"{surgeon.name}: {surgeon.v_hour}")
print(f"{laborer.name}: {laborer.v_hour}")

print(f"\n--- Simulation Cycle ---")
surgeon.work(8)
laborer.work(8)
print(f"\n--- Total Vouchers ---")
print(f"{surgeon.name}: {surgeon.vouchers:.2f} vouchers")
print(f"{laborer.name}: {laborer.vouchers:.2f} vouchers")

#IM A FUCKING GENIUS!!!!!