from functools import lru_cache
import pandas as pd
import requests
from thefuzz import process


@lru_cache
def dicom_data(name):
    """Download the requested json data from the git and return as pandas DataFrame.

    Args:
        name (str): name of the json file without extenstion, e.g. attributes for attributes.json
    """
    json_base = (
        "https://raw.githubusercontent.com/innolitics/dicom-standard/master/standard"
    )
    json_data = requests.get(f"{json_base}/{name}.json").json()
    return pd.DataFrame(json_data)


def get_best_match(df, col, value, thres=50):
    """Search for a string value in a df column using fuzzy matching."""
    matsch, score, idx = process.extractOne(value, df[col], score_cutoff=thres)
    return matsch  # Adjust threshold as needed


def get_best_matches(df, col, value, limit=3, thres=50):
    """Search for a string value in a df column using fuzzy matching. Return top-k matches."""
    results = process.extractBests(value, df[col], limit=limit, score_cutoff=thres)
    if not results:
        return None
    matches, scores, indices = zip(*results)
    return matches


def find_details(attribute: str, domain: str = "MR Image"):
    """Find details for a Dicom attribute in a given CIOD domain

    Args:
        attribute (str): a dicom attribute name, e.g. Study Date
        domain (str): a dicom CIOD domain, e.g. MR Image

    Returns:
        pd.DataFrame: dataframe with best matches
    """
    attributes = dicom_data("attributes")
    modules = dicom_data("modules")
    ciods = dicom_data("ciods")
    module_to_attributes = dicom_data("module_to_attributes")
    ciod_to_modules = dicom_data("ciod_to_modules")

    attribute = get_best_match(attributes, "name", attribute)
    if not attribute:
        msg = f"No match found for attribute keyword {attribute}!"
        raise ValueError(msg)
    matched_attributes = attributes[attributes.name == attribute]

    domains = get_best_matches(ciods, "name", domain, thres=30)
    if not domains:
        msg = f"No match found for CIOD domain {domain}!"
        raise ValueError(msg)
    domain_ciods = ciods[ciods.name.isin(domains)].add_prefix("ciod_")

    details = pd.merge(
        matched_attributes,
        module_to_attributes[["moduleId", "tag", "linkToStandard", "description"]],
        on="tag",
    )
    details = pd.merge(
        details, modules.add_prefix("module_"), left_on="moduleId", right_on="module_id"
    ).drop(columns="module_id")
    details = pd.merge(details, ciod_to_modules[["moduleId", "ciodId"]], on="moduleId")
    details = pd.merge(
        details, domain_ciods, left_on="ciodId", right_on="ciod_id"
    ).drop(columns="ciod_id")

    return details


def get_ciods() -> list[str]:
    ciods = dicom_data("ciods")
    return ciods.name.to_list()


def get_modules(ciod: str = "common") -> list[str]:
    if ciod == "common":
        return common_modules().name.to_list()

    ciod_to_modules = dicom_data("ciod_to_modules")
    modules = dicom_data("modules")
    ciods = dicom_data("ciods")

    ciod = get_best_match(ciods, "name", ciod)
    ciodId = ciods[ciods.name == ciod].id.item()
    moduleIds = ciod_to_modules[ciod_to_modules.ciodId == ciodId].moduleId
    ciod_modules = modules[modules.id.isin(moduleIds)]
    return ciod_modules.name.to_list()


def get_attributes(ciod: str = "common") -> list[str]:
    if ciod == "common":
        return common_attributes().keyword.to_list()

    module_to_attributes = dicom_data("module_to_attributes")
    attributes = dicom_data("attributes")
    ciod_to_modules = dicom_data("ciod_to_modules")
    modules = dicom_data("modules")
    ciods = dicom_data("ciods")

    ciod = get_best_match(ciods, "name", ciod)
    ciodId = ciods[ciods.name == ciod].id.item()
    moduleIds = ciod_to_modules[ciod_to_modules.ciodId == ciodId].moduleId
    ciod_modules = modules[modules.id.isin(moduleIds)]
    ciod_tags = module_to_attributes[
        module_to_attributes.moduleId.isin(ciod_modules.id)
    ].tag
    ciod_attributes = attributes[attributes.tag.isin(ciod_tags)]
    return ciod_attributes.name.to_list()


def common_modules():
    modules = dicom_data("modules")
    ciod_to_modules = dicom_data("ciod_to_modules")

    module_counts = ciod_to_modules.moduleId.value_counts()
    sorted_modules = modules.copy()
    sorted_modules["id_count"] = sorted_modules.id.map(module_counts)
    sorted_modules = sorted_modules.sort_values(by="id_count", ascending=False)
    return sorted_modules[sorted_modules["id_count"] > 25].reset_index()


def common_attributes():
    module_to_attributes = dicom_data("module_to_attributes")
    attributes = dicom_data("attributes")

    tag_counts = module_to_attributes.tag.value_counts()
    common_tags = tag_counts[tag_counts > 50]
    filtered_attributes = attributes[attributes.tag.isin(common_tags.index)].copy()
    filtered_attributes["tag_count"] = filtered_attributes.tag.map(common_tags)
    sorted_attributes = filtered_attributes.sort_values(by="tag_count", ascending=False)
    return sorted_attributes.reset_index()


def find_sop_name(uid: str) -> str:
    sops = dicom_data("sops")
    matched_sops = sops[sops.id == uid]
    if len(matched_sops) == 0:
        return {"error": "SOP UID not found!"}
    else:
        return matched_sops.name.item()


def find_sop_uid(name: str) -> list:
    """Search for the SOP UID by a given name

    Args:
        name (str): search name

    Returns:
        list[str]: potential SOP UIDs sorted by relevance
    """
    sops = dicom_data("sops")
    matched_names = get_best_matches(sops, "name", name)
    if not matched_names:
        return {"error": f"No SOP ID found with name {name}"}
    return sops[sops.name.isin(matched_names)].id.to_list()
