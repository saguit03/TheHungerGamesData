# Define los pesos de las relaciones
relationship_weights = {
    "ALLY_OF": 5,
    "APPEARS_IN": 10000,
    "BELONGS_TO": 50,
    "DIED_FROM": 5,
    "FROM_DISTRICT": 80,
    "KILLED": 2,
    "MENTOR": 1,
    "PARTICIPATED_IN": 5,
    "HANDMADE": 10,
    "GOVERNS": 10,
    "CONTROLS": 10
}
family_relationships_weights = {
    "LOVER": 0.1,
    "SIBLING": 0.5,
    "PARENT": 0.5,
    "CHILD": 0.5,
    "COUSIN": 3.0,
    "FRIEND": 1.0,
    "OTHER": 3.0,
    "ACQUAINTANCE": 5.0,
    "PET": 0.1
}

def build_relationship_string():
    all_rels = list(relationship_weights.keys()) + list(family_relationships_weights.keys())
    return '|'.join(all_rels)

inverse_relationships = {
    "PARENT": "CHILD",
    "CHILD": "PARENT",
    "LOVER": None,
    "SIBLING": None,
    "COUSIN": None,
    "FRIEND": None,
    "OTHER": None,
    "ACQUAINTANCE": None,
    "PET": "OWNER"
}

family_examples = {
    "Katniss Everdeen": {
        "Lover": ["Peeta Mellark"],
        "Sibling": ["Primrose Everdeen"],
        "Parent": ["Asterid Everdeen", "Burdock Everdeen"],
        "Child": ["None"],
        "Cousin": ["Gale Hawthorne"],
        "Friend": ["Cinna", "Madge Undersee", "Gale Hawthorne", "Finnick Odair", "Rue"],
        "Other": ["Boggs", "Greasy Sae", "Castor"],
        "ACQUAINTANCE": ["Plutarch Heavensbee"],
        "Pet": ["Buttercup", "Lady"],
        "Child": ["None"],
        "Pet": ["Buttercup", "Lady"],
        "Child": ["Babyboy Mellark Everdeen", "Babygirl Mellark Everdeen"],
    },
    "Peeta Mellark": {
        "Lover": ["Katniss Everdeen"],
        "Parent": ["Otho Mellark", "Mrs. Mellark"],
        "Child": ["Babyboy Mellark Everdeen", "Babygirl Mellark Everdeen"],
    },
    "Haymitch Abernathy": {
        "Sibling": ["Sid Abernathy", "Maysilee Donner"],
        "Parent": ["Willamae Abernathy"],
        "Friend": ["Effie Trinket", "Chaff", "Cecelia", "Maysilee Donner"],
        "Lover": ["Lenore Dove Baird"],
        "Other": ["Hattie Meeney"],
        "ACQUAINTANCE": ["Plutarch Heavensbee"]
    },
    "Willamae Abernathy": {
        "Child": ["Haymitch Abernathy", "Sid Abernathy"],
    },
    "Lenore Dove Baird": {
        "Sibling": ["None"],
        "Lover": ["Haymitch Abernathy"],
        "Other": ["Lucy Gray Baird"],
        "Parent": ["Clerk Carmine", "Maude Ivory", "Tam Amber"],
    },
    "Burdock Everdeen": {
        "Parent": ["Clerk Carmine"],
        "Child": ["Katniss Everdeen", "Primrose Everdeen"],
        "Lover": ["Asterid Everdeen"]
    },
    "Primrose Everdeen": {
        "Sibling": ["Katniss Everdeen"],
        "Parent": ["Asterid Everdeen", "Burdock Everdeen"],
        "Pet": ["Buttercup", "Lady"]
    },
    "Finnick Odair": {
        "Lover": ["Annie Cresta"],
        "Parent": ["None"],
        "Friend": ["Katniss Everdeen", "Peeta Mellark"],
        "Child": ["Baby Odair Cresta"],
    },
    "Annie Cresta": {
        "Lover": ["Finnick Odair"],
        "Child": ["Baby Odair Cresta"],
        "Friend": ["Katniss Everdeen", "Peeta Mellark"]
    },
    "Lucretius ""Lucky"" Flickerman": {
        "Pet": ["Jubilee"],
        "Other": ["Cesar Flickerman"]
    },
    "Coriolanus Snow": {
        "Parent": ["Crassus Snow"],
        "Cousin": ["Tigris"],
        "Friend": ["Sejanus Plinth"],
        "Lover": ["Lucy Gray Baird", "Livia Cardew"],
        "Other": ["Volumnia Gaul", "Grandma'am"],
        "Acquaintance": ["Plutarch Heavensbee"]
    },
    "Seneca Crane": {
        "Other": ["Arachne Crane"]
    },
    "Eddy": {
        "Sibling": ["Eddy's sister"]
    },
    "Beetee Latier": {
        "Child": ["Ampert Latier"],
        "Friend": ["Wiress"]
    },
    "Wiress": {
        "Friend": ["Beetee Latier", "Haymitch Abernathy"]
    },
    "Maysilee Donner": {
        "Sibling": ["Haymitch Abernathy", "Merrilee Undersee"],
        "Other": ["Madge Undersee"],
        "Friend": ["Haymitch Abernathy"]
    },
    "Merrilee Undersee": {
        "Sibling": ["Maysilee Donner"],
        "Lover": ["Mayor Undersee"],
        "Child": ["Madge Undersee"]
    },
    "Gale Hawthorne": {
        "Sibling": ["Rory Hawthorne", "Vick Hawthorne", "Posy Hawthorne"],
        "Parent": ["Hazelle Hawthorne"]
    },
    "Diana Ring": {
        "Sibling": ["Apolo Ring"],
    },
}
