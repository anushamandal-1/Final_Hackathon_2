import os

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "dataset1.csv")

# ── Supplier locations (source nodes) ─────────────────────────────────────────
SUPPLIER_COORDS = {
    "Chennai":   (13.08,  80.27),
    "Mumbai":    (19.07,  72.87),
    "Delhi":     (28.61,  77.20),
    "Kolkata":   (22.57,  88.36),
    "Hyderabad": (17.38,  78.48),
    "Ahmedabad": (23.02,  72.57),
    "Pune":      (18.52,  73.86),
    "Surat":     (21.17,  72.83),
}

# ── Plant / destination locations ─────────────────────────────────────────────
PLANT_OPTIONS = {
    "Bangalore Plant":  (12.97, 77.59),
    "Chennai Hub":      (13.08, 80.27),
    "Pune Facility":    (18.52, 73.86),
    "Hyderabad Depot":  (17.38, 78.48),
    "Delhi Warehouse":  (28.61, 77.20),
    "Mumbai Port":      (19.07, 72.87),
    "Kolkata Yard":     (22.57, 88.36),
    "Ahmedabad Plant":  (23.02, 72.57),
}

# Default (backward-compat)
PLANT_COORDS = (12.97, 77.59)
PLANT_NAME   = "Bangalore Plant"

CO2_BASE  = 0.21
SPEED_KMH = 60

# ── UI option lists ────────────────────────────────────────────────────────────
SHIPPING_MODES    = ["Standard Class", "First Class", "Second Class", "Same Day"]
CUSTOMER_SEGMENTS = ["Consumer", "Corporate", "Home Office"]
TRAFFIC_OPTIONS   = ["Low", "Medium", "High"]
DISRUPTION_TYPES  = ["None", "Port Delay", "Strike", "Weather"]
VEHICLE_TYPES     = ["Truck", "Van", "Bike"]
SUPPLIER_LOCS     = list(SUPPLIER_COORDS.keys())
PLANT_LOCS        = list(PLANT_OPTIONS.keys())
OPT_MODES         = ["Cost Efficient", "Fast Delivery", "Eco Friendly"]

# ── Encoding maps ─────────────────────────────────────────────────────────────
SHIPPING_MODE_MAP = {v: i for i, v in enumerate(sorted(SHIPPING_MODES))}
CUSTOMER_SEG_MAP  = {v: i for i, v in enumerate(sorted(CUSTOMER_SEGMENTS))}
TRAFFIC_MAP       = {"High": 0, "Low": 1, "Medium": 2}
DISRUPTION_MAP    = {"None": -1, "Port Delay": 0, "Strike": 1, "Weather": 2}
SUPPLIER_LOC_MAP  = {"Chennai": 0, "Delhi": 1, "Mumbai": 2,
                     "Kolkata": 0, "Hyderabad": 0, "Ahmedabad": 2,
                     "Pune": 2, "Surat": 2}