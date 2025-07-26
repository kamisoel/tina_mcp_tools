#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "camelot-py",
#     "fastmcp",
#     "requests",
# ]
# ///

from typing import Optional
from fastmcp import FastMCP
import datetime as dt
from zoneinfo import ZoneInfo
import requests
import re
import io
from bs4 import BeautifulSoup
import camelot
from functools import lru_cache
from pydantic import BaseModel

mcp = FastMCP("UKSH Mensa 🌮")


class TimeResult(BaseModel):
    timezone: Optional[str]
    date: dt.date
    weekday: str


@mcp.tool
def todays_date(timezone: Optional[str] = None) -> TimeResult:
    """Return the current date, time and weekday

    Args:
        timezone (str, optional): A timezone name. Use None for local timezone.

    Returns:
        TimeResult: current date, time, weekday and timezone
    """
    if timezone:
        tz = ZoneInfo(timezone)
        today = dt.datetime.now(tz).date()
    else:
        today = dt.datetime.now().date()
    weekday = today.strftime("%A")
    return TimeResult(timezone=timezone, date=today, weekday=weekday)


@mcp.tool
def offset_date(date: dt.date, days: int = 0, weeks: int = 0) -> str:
    """
    Offset the specified date by X days and / or weeks.

    Args:
        date (datetime.date): The specified starting date.
        days (int, optional): Specifies how many days to offset. Defaults to 0.
        weeks (int, optional): Specifies how many weeks to offset. Defaults to 0.

    """
    offset_date = date + dt.timedelta(days=days, weeks=weeks)
    return offset_date.strftime("%A, %d.%m.%Y")


def get_mensa_plan_url(date: dt.date) -> str:
    """Return the URL of the UKSH weekly mensa plan pdf for the specified date."""

    mensa_url = "https://www.uksh.de/ssn/unser+speisenangebot/campus+kiel/uksh_bistro+kiel-p-368.html"
    base_url = "https://www.uksh.de/"
    pattern = (
        r"Bistro KW (\d+) .* (\d{1,2}\.\d{1,2}\.\d{2,4}) - (\d{1,2}\.\d{1,2}\.\d{2,4})"
    )

    response = requests.get(mensa_url)
    soup = BeautifulSoup(response.text, features="html.parser")
    for link in soup.find_all("a", href=True):
        # urllib.parse.unquote(link['href'])
        match = re.match(pattern, link.text)
        if match:
            # kw = match.group(1)
            start_date = dt.datetime.strptime(match.group(2), "%d.%m.%y").date()
            end_date = dt.datetime.strptime(match.group(3), "%d.%m.%y").date()
            if date >= start_date and date <= end_date:
                href = link["href"]
                return href if href.startswith("https") else base_url + href
    return None


@lru_cache
def get_mensa_plan_from_url(url):
    """Download and parse the weekly UKSH mensa plan from 'url'. Returns a pd.DataFrame."""
    pdf = requests.get(url).content
    tables = camelot.read_pdf(io.BytesIO(pdf), backend="pdfium")
    menu = tables[0].df
    menu = menu.rename(columns=menu.iloc[0]).drop(menu.index[0]).set_index("Wochentag")
    return menu


@mcp.tool
def get_mensa_plan(date: dt.date) -> str:
    """Get the UKSH mensa food plan for the specified date.

    Use tool "todays_date" first if you need todays date.
    To get other dates, use "offset_date" with todays date and the number of days to offset.
    e.g. if today is Monday, 2025/05/05, offset todays date by 4 days to get this Friday's date.

    Args:
        date (str): The iso formatted date

    Returns:
        str: mensa food plan as markup table for this day (columns=[dish station, menu])
    """
    weekday = date.weekday()
    date_url = get_mensa_plan_url(date)
    if date_url:
        menu = get_mensa_plan_from_url(date_url)
        day_menu = menu.iloc[weekday]
        markdown = day_menu.to_markdown()
        return markdown
    return "No plan found for the specified date!"


def main():
    mcp.run()


if __name__ == "__main__":
    mcp.run()
