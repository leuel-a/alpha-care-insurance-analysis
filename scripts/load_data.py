#!/usr/bin/env python3
import pandas as pd

columns = [
    "UnderwrittenCoverID", "PolicyID", "TransactionMonth", "IsVATRegistered", "Citizenship", "LegalType", "Title",
    "Language", "Bank", "AccountType", "MaritalStatus", "Gender", "Country", "Province", "PostalCode", "MainCrestaZone",
    "SubCrestaZone", "ItemType", "mmcode", "VehicleType", "RegistrationYear", "make", "Model", "Cylinders",
    "cubiccapacity", "kilowatts", "bodytype", "NumberOfDoors", "VehicleIntroDate", "CustomValueEstimate",
    "AlarmImmobiliser", "TrackingDevice", "CapitalOutstanding", "NewVehicle", "WrittenOff", "Rebuilt", "Converted",
    "CrossBorder", "NumberOfVehiclesInFleet", "SumInsured", "TermFrequency", "CalculatedPremiumPerTerm",
    "ExcessSelected", "CoverCategory", "CoverType", "CoverGroup", "Section", "Product", "StatutoryClass",
    "StatutoryRiskType", "TotalPremium", "TotalClaims"
]


def load_data():
    file_path = "../data/raw/MachineLearningRating_v3.txt"
    df = pd.read_csv(file_path, delimiter='|', low_memory=False)

    return df
