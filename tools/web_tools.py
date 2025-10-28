from smolagents import Tool, DuckDuckGoSearchTool
from bs4 import BeautifulSoup
import pandas as pd
import json, requests
from typing import List, Dict, Optional

class UTU_events(Tool):
    name = "UTU_events_search"
    description = (
        "Search the local `events.csv` file for Utah Tech events."
        "Returns structured event records (date, start_time, end_time, title, location, category, description, url)."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "A keyword or phrase to search for in the events (case-insensitive).",
        },
    }
    output_type = "string"

    def __init__(self, csv_path: str = "events.csv"):
        super().__init__()
        self.csv_path = csv_path

    def forward(self, query: str) -> str:
        try:
            df = pd.read_csv(self.csv_path, on_bad_lines='skip')
            mask = df.astype(str).apply(
                lambda col: col.str.contains(query, case=False, na=False)
            ).any(axis=1)
            results_df = df[mask]
            if results_df.empty:
                return json.dumps({"message": f"No events found matching '{query}'."})
            return results_df.to_json(orient="records", indent=2)
        except FileNotFoundError:
            return json.dumps({"error": f"The event file was not found at {self.csv_path}"})
        
class UtahTechWebSearchTool(Tool):
    name = "Utah_Tech_University_website_search"
    description = (
        "Searches through all Utah Tech University's website for a query."
        "Course titles, URL's."
    )
    inputs = {"query": {"type":"string","description":"HTTP/HTTPS URL to fetch"}}
    output_type = "string"

    def __init__(self, sites: List[str] = None):
        super().__init__()
        self._ddgs = DuckDuckGoSearchTool()
        if sites is None:
            sites = ["utahtech.edu", "utahtechtrailblazers.edu", "cs.utahtech.edu"]
            self.sites = sites
        else:
            self.sites = sites

    def forward(self, query: str) -> str:
        site_filter = [f"site:{site}" for site in self.sites]
        site_query = f"({" OR ".join(site_filter)})"
        query = f"{site_query} {query}"
        return self._ddgs(query)