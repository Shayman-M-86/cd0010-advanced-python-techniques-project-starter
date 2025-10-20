# 📝 Update Summary

## **File:** `models.py`

### **Class:** `NearEarthObject`

#### **Added**

    @property
    def details(self) -> str: 
    """Return a short detail string for this NEO."""
    name_str = f", '{self.name}'" if self.name is not None else ""
    diameter_str = f", {self.diameter} km" if not math.isnan(self.diameter) else ""
    hazard_str = ", Hazardous" if self.hazardous else ""

    return f"({self.designation}{name_str}{diameter_str}{hazard_str})"

#### **Description**

Added a `details` property that returns a concise, human-readable summary of a Near-Earth Object (NEO).  
This makes output easier to read when streaming results from `CloseApproach` objects.

#### **Example Output**

    print(neo.details)# → (2021 AB, 'Apophis', 0.325 km, Hazardous)

#### **Purpose**

To provide a **clearer, more readable string representation** of NEO data when listing or streaming close-approach results in the console
